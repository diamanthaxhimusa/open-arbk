import datetime


class MongoUtils(object):

    def __init__(self, mongo):
        self.mongo = mongo
        self.reg_businesses_collection = 'reg_businesses'
        self.municipalities = 'municipalities'
        self.activities = 'activities'

    def get_all_docs(self):
        result = self.mongo.db[self.reg_businesses_collection].find()
        return result
    def docs_count(self):
        result = self.mongo.db[self.reg_businesses_collection].count()
        return result

    def get_all_activities(self):
        result = self.mongo.db[self.activities].find()
        return result

    def get_employees(self, current_lang):
        db = self.mongo.db[self.reg_businesses_collection]
        result_micro = db.aggregate([
            {'$match': {"employeeCount": {"$gte": 1,"$lte": 9}}}, {'$group':{"_id":"$status", "count":{'$sum':1}}}
        ])
        for res in result_micro['result']:
            if res['_id'] == "":
                result_micro['result'].remove(res)
        result_mini = db.aggregate([
            {'$match': {"employeeCount": {"$gte": 10,"$lte": 49}}}, {'$group':{"_id":"$status", "count":{'$sum':1}}}
        ])
        result_middle = db.aggregate([
            {'$match': {"employeeCount": {"$gte": 50,"$lte": 249}}}, {'$group':{"_id":"$status", "count":{'$sum':1}}}
        ])
        result_big = db.aggregate([
            {'$match': {"employeeCount": {"$gte": 250}}}, {'$group':{"_id":"$status", "count":{'$sum':1}}}
        ])
        total = db.count()
        return {
            "micro":{
                "total":result_micro['result'][0]['count']+result_micro['result'][1]['count'],
                result_micro['result'][1]['_id'][current_lang]:result_micro['result'][1]['count'],
                result_micro['result'][0]['_id'][current_lang]:result_micro['result'][0]['count']
            },
            "mini":{
                "total":result_mini['result'][0]['count']+result_mini['result'][1]['count'],
                result_mini['result'][1]['_id'][current_lang]:result_mini['result'][1]['count'],
                result_mini['result'][0]['_id'][current_lang]:result_mini['result'][0]['count']
            },
            "middle":{
                "total":result_middle['result'][0]['count']+result_middle['result'][1]['count'],
                result_middle['result'][1]['_id'][current_lang]:result_middle['result'][1]['count'],
                result_middle['result'][0]['_id'][current_lang]:result_middle['result'][0]['count']
            },
            "big":{
                "total":result_big['result'][0]['count']+result_big['result'][1]['count'],
                result_big['result'][1]['_id'][current_lang]:result_big['result'][1]['count'],
                result_big['result'][0]['_id'][current_lang]:result_big['result'][0]['count']
            },
            "total":total}

    # Search engine
    def search_engine(self, page, items_per_page, business, status, person, person_status, municipality):
        search = {}
        search_person = {
            '$or':[
                    {"slugifiedOwners": {"$regex": person}},
                    {"slugifiedAuthorized": {"$regex": person}}
                ]
            }
        search_person_status = {
            person_status: {"$regex": person}
            }
        search_bussiness = {
            "slugifiedBusiness": {"$regex": business}
            }
        search_bussiness_status = {
            "status.sq": status
            }
        search_municipality = {
            "slugifiedMunicipality": municipality
            }
        if person != "":
            if person_status != "any":
                search.update(search_person_status)
            else:
                search.update(search_person)
        if business != "":
            search.update(search_bussiness)
        if status != "any":
            search.update(search_bussiness_status)
        if municipality != "any":
            search.update(search_municipality)
        result = self.mongo.db[self.reg_businesses_collection].find(search)
        final_result = result.skip(items_per_page*(page-1)).limit(items_per_page)
        count = result.count()
        return {"result":final_result, "count":count}

    def index_create(self):
        result = self.mongo.db[self.reg_businesses_collection].create_index("formatted.slugifiedOwners", 1)
        return result

    def get_limit_businesses(self, num):
        result = self.mongo.db[self.reg_businesses_collection].find().limit(num)
        return result

    def get_municipalities(self):
        result = self.mongo.db[self.municipalities].find().sort("municipality", 1)
        return result
    def get_people(self, people_type, keyword, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({people_type: {"$regex": keyword}}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({people_type: {"$regex": keyword}}).count()
        return {"result":result, "count":count}
    def get_people_by_municipality(self, people_type, keyword, municipality, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find(
            {people_type: {"$regex": keyword},
             "slugifiedMunicipality": municipality}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find(
            {people_type: {"$regex": keyword},
             "slugifiedMunicipality": municipality}).count()
        return {"result":result, "count":count}

    # Profile queries
    def get_profiles(self, people_type, person, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({people_type: {"$in": [person]}})
        final_result = result.skip(items_per_page*(page-1)).limit(items_per_page)
        count = result.count()
        return {"result":final_result, "count":count}

    # Top ten capital businesses
    def get_top_ten_businesses(self, biz_status, municipality):
        query = []
        limit = {'$limit': 10}
        capital_sort = {'$sort': {"capital": -1}}
        status = {'$match': {"status": biz_status}}
        muni = {'$match': {"municipality.municipality": municipality}}
        query.append({'$match': {"applicationDate": {"$gte": datetime.datetime(2000, 1, 1),"$lt": datetime.datetime(2017, 1, 1)}}})
        if biz_status != "any":
            query.append(status)
        if municipality != "any":
            query.append(muni)
        query.append(capital_sort)
        query.append(limit)
        result = self.mongo.db[self.reg_businesses_collection].aggregate(query)
        return result

    # Businesses through years queries
    def businesses_through_years(self, date_type, year):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': { date_type: {"$gte": datetime.datetime(year, 1, 1),
                                              "$lte": datetime.datetime(year+1, 1, 1)}}},
            {'$group': {"_id": "$status", "count": {"$sum": 1}}}])
        for i in result['result']:
            if i['_id'] == "":
                result['result'].remove(i)
        return result

    # Businesses type
    def get_business_types(self, municipality, business_status):
        query = []
        sort_biz = {'$sort': {'total': -1}}
        group = {'$group': {"_id": "$type", "total": {"$sum": 1}}}
        match_status = {'$match': {"status":business_status}}
        match_muni = {'$match': {"municipality.municipality":municipality}}
        query.append({'$match': {"applicationDate": {"$gte": datetime.datetime(2000, 1, 1),"$lt": datetime.datetime(2017, 1, 1)}}})
        if business_status != "any":
            query.append(match_status)
        if municipality != "any":
            query.append(match_muni)
        query.append(group)
        query.append(sort_biz)
        result = self.mongo.db[self.reg_businesses_collection].aggregate(query)
        return result
    def get_count_biz_types(self, business_status, municipality):
        query = []
        match_status = {'$match': {"status":business_status}}
        match_muni = {'$match': {"municipality.municipality":municipality}}
        count = {'$count':"all"}
        query.append({'$match': {"applicationDate": {"$gte": datetime.datetime(2000, 1, 1),"$lt": datetime.datetime(2017, 1, 1)}}})
        if business_status != "any":
            query.append(match_status)
        if municipality != "any":
            query.append(match_muni)
        query.append(count)
        result = self.mongo.db[self.reg_businesses_collection].aggregate(query)
        return result

    # MAP Activities
    def mapi(self, activity):
        act = self.mongo.db[self.activities].find({"activity":activity})
        munis = self.mongo.db[self.municipalities].find()
        code = 0
        for doc in act:
            code = doc['code']
        muni = []
        for i in munis:
            muni.append(i['municipality'])
        result = {}
        for i in muni:
            res = self.mongo.db[self.reg_businesses_collection].aggregate([
                {'$match': {"applicationDate": {"$gt": datetime.datetime(2000, 1, 1),"$lt": datetime.datetime(2017, 1, 1)}}},
                {'$unwind': "$activities"},
                {'$match': {"activities":int(code), "municipality.municipality":i}},
                {'$count':"all"}
            ])
            try:
                result.update({i:res['result'][0]['all']})
            except Exception as e:
                result.update({i:0})
        return result
    def mapi_all(self):
        munis = self.mongo.db[self.municipalities].find()
        muni = []
        for i in munis:
            muni.append(i['municipality']['sq'])
        result = {}
        for i in muni:
            res = self.mongo.db[self.reg_businesses_collection].aggregate([
                {'$match': {"applicationDate": {"$gte": datetime.datetime(2000, 1, 1),"$lt": datetime.datetime(2017, 1, 1)},
                            "municipality.municipality.sq":i}},
                {'$count':"all"}
            ])
            try:
                result.update({i:res['result'][0]['all']})
            except Exception as e:
                result.update({i:0})
        return result
    def mapi_all_status(self, status):
        munis = self.mongo.db[self.municipalities].find()
        muni = []
        for i in munis:
            muni.append(i['municipality']['sq'])
        result = {}
        for i in muni:
            res = self.mongo.db[self.reg_businesses_collection].aggregate([
                {'$match': {"applicationDate": {"$gte": datetime.datetime(2000, 1, 1),"$lt": datetime.datetime(2017, 1, 1)},
                            "municipality.municipality.sq":i, "status":status}},
                {'$count':"all"}
            ])
            try:
                result.update({i:res['result'][0]['all']})
            except Exception as e:
                result.update({i:0})
        return result
    def mapi_status(self, activity, status):
        act = self.mongo.db[self.activities].find({"activity":activity})
        munis = self.mongo.db[self.municipalities].find()
        code = 0
        for doc in act:
            code = doc['code']
        muni = []
        for i in munis:
            muni.append(i['municipality']['sq'])
        result = {}
        for i in muni:
            res = self.mongo.db[self.reg_businesses_collection].aggregate([
                {'$match': {"applicationDate": {"$gte": datetime.datetime(2000, 1, 1),"$lt": datetime.datetime(2017, 1, 1)}}},
                {'$unwind': "$activities"},
                {'$match': {"activities":int(code), "municipality.municipality.sq":i, "status":status}},
                {'$count':"all"}
            ])
            try:
                result.update({i:res['result'][0]['all']})
            except Exception as e:
                result.update({i:0})
        return result

    # Get activities from db
    def get_activities(self):
        acts = self.mongo.db[self.activities].find()
        activs = []
        for act in acts:
            activs.append({"activity":act['activity'],"code":act['code']})
        return activs

    # top 10 activity divided in genders
    def get_top_ten_activities_by_gender(self, gender):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"applicationDate": {"$gte": datetime.datetime(2000, 1, 1),"$lt": datetime.datetime(2017, 1, 1)}}},
            {'$unwind': "$activities"},
            {'$unwind': "$owners"},
            {'$match' : {"owners.gender":gender}},
            {'$group': {"_id": "$activities",'totali': {'$sum': 1}}},
            {'$sort': {"totali": -1}},
            {'$limit' : 10}
        ])
        return result

    # activities queries
    def activity_years(self, year, activity, current_lang):
        act = self.mongo.db[self.activities].find({"activity.%s"%current_lang:activity})
        code = 0
        for doc in act:
            code = doc['code']
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"applicationDate": {"$gte": datetime.datetime(year, 1, 1),
                                              "$lte": datetime.datetime(year+1, 1, 1)}}},
            {'$unwind': "$activities"},
            {'$match': {"activities":int(code)}},
            {'$group': {"_id": "$status", "count": {"$sum": 1}}}])
        return result

    # top used activities
    def get_most_used_activities(self, status, municipality):
        query = []
        unwind = {'$unwind': "$activities"}
        group = {'$group': {"_id": "$activities", 'totali': {'$sum': 1}}}
        sort_activities = {'$sort': {"totali": -1}}
        match_muni = {'$match': {'municipality.municipality': municipality}}
        match_status = {'$match': {'status': status}}
        query.append({'$match': {"applicationDate": {"$gte": datetime.datetime(2000, 1, 1),"$lt": datetime.datetime(2017, 1, 1)}}})
        if status != "any":
            query.append(match_status)
        if municipality != "any":
            query.append(match_muni)
        query.append(unwind)
        query.append(group)
        query.append(sort_activities)
        result = self.mongo.db[self.reg_businesses_collection].aggregate(query)
        return result

    # Get total businesses by status
    def get_total_by_status(self):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"applicationDate": {"$gte": datetime.datetime(2000, 1, 1),"$lt": datetime.datetime(2017, 1, 1)}}},
            {'$group': {"_id": "$status", "total": {"$sum": 1}}},
            {'$sort':  {'total': -1}}])
        return result
    def get_stats_by_status(self):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$group': {"_id": "$status", "total": {"$sum": 1}}},
            {'$sort':  {'total': -1}}])
        return result
    #Get owners count by gender
    def get_gender_owners_data(self, status, city):
        query = []
        unwind = {'$unwind': "$owners"}
        sort_owners = {'$sort': {"all":-1}}
        group = {'$group': {"_id":"$owners.gender", "all":{"$sum":1}}}
        match_status = {'$match': {"status":status}}
        match_muni = {'$match': {"municipality.municipality":city}}
        query.append({'$match': {"applicationDate": {"$gte": datetime.datetime(2000, 1, 1),"$lt": datetime.datetime(2017, 1, 1)}}})
        if status != "any":
            query.append(match_status)
        if city != "any":
            query.append(match_muni)
        query.append(unwind)
        query.append(group)
        query.append(sort_owners)
        result = self.mongo.db[self.reg_businesses_collection].aggregate(query)
        return result
    def get_gender_owners_data_count(self, status, city):
        query = []
        unwind = {'$unwind': "$owners"}
        sort_owners = {'$sort': {"all":-1}}
        group = {'$group': {"_id":"$owners.gender", "all":{"$sum":1}}}
        match_status = {'$match': {"status":status}}
        match_muni = {'$match': {"municipality.municipality":city}}
        count = {'$count':"all"}
        query.append({'$match': {"applicationDate": {"$gte": datetime.datetime(2000, 1, 1),"$lt": datetime.datetime(2017, 1, 1)}}})
        if status != "any":
            query.append(match_status)
        if city != "any":
            query.append(match_muni)
        query.append(unwind)
        query.append(group)
        query.append(sort_owners)
        query.append(count)
        result = self.mongo.db[self.reg_businesses_collection].aggregate(query)
        return result
