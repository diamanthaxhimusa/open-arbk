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

    # Search people queries
    def index_create(self):
        result = self.mongo.db[self.reg_businesses_collection].create_index("formatted.slugifiedOwners", 1)
        return result

    def get_limit_search(self, page, items):
        result = self.mongo.db[self.reg_businesses_collection].find().skip(items*(page-1)).limit(items)
        count = self.mongo.db[self.reg_businesses_collection].find().count()
        return {"result":result, "count":count}

    def search_docs_by_municipality(self, municipality, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find(
            {"slugifiedMunicipality": municipality}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({"slugifiedMunicipality": municipality}).count()
        return {"result":result, "count":count}
    def search_docs_by_biz_status(self, status, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            "status": status})
        final_result = result.skip(items_per_page*(page-1)).limit(items_per_page)
        count = result.count()
        return {"result":final_result, "count":count}
    def search_docs_by_biz_status_municipality(self, status, municipality, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find(
            {"slugifiedMunicipality": municipality,
             "status":status}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find(
            {"slugifiedMunicipality": municipality,
             "status":status}).count()
        return {"result":result, "count":count}

    def search_biz_people_status_municipality(self, business, person, person_status, municipality, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            person_status: {"$regex": person},
            "slugifiedMunicipality": municipality}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            person_status: {"$regex": person},
            "slugifiedMunicipality": municipality}).count()
        return {"result":result, "count":count}
    def search_biz_people_status(self, business, person, status, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            status: {"$regex": person}}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            status: {"$regex": person}}).count()
        return {"result":result, "count":count}
    def search_biz_status_people_status_municipality(self, business, biz_status, person, person_status, municipality, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            person_status: {"$regex": person},
            "status": biz_status,
            "slugifiedMunicipality": municipality}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            person_status: {"$regex": person},
            "status": biz_status,
            "slugifiedMunicipality": municipality}).count()
        return {"result":result, "count":count}
    def search_biz_status_people_status(self, business, biz_status, person, person_status, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            person_status: {"$regex": person},
            "status": biz_status}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            person_status: {"$regex": person},
            "status": biz_status}).count()
        return {"result":result, "count":count}
    def search_biz_status_people_municipality(self, business, biz_status, person, municipality, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            '$or': [{"slugifiedOwners": {"$regex": person}},
                    {"slugifiedAuthorized": {"$regex": person}}],
            "status": biz_status,
            "slugifiedMunicipality": municipality}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            '$or': [{"slugifiedOwners": {"$regex": person}},
                    {"slugifiedAuthorized": {"$regex": person}}],
            "status": biz_status,
            "slugifiedMunicipality": municipality}).count()
        return {"result":result, "count":count}
    def search_biz_people_municipality(self, business, person, municipality, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            '$or': [{"slugifiedOwners": {"$regex": person}},
                     {"slugifiedAuthorized": {"$regex": person}}],
            "slugifiedMunicipality": municipality}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            '$or': [{"slugifiedOwners": {"$regex": person}},
                     {"slugifiedAuthorized": {"$regex": person}}],
            "slugifiedMunicipality": municipality}).count()
        return {"result":result, "count":count}
    def search_biz_status_people(self, business, biz_status, person, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            '$or': [{"slugifiedOwners": {"$regex": person}},
                     {"slugifiedAuthorized": {"$regex": person}}],
            "status":biz_status}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            '$or': [{"slugifiedOwners": {"$regex": person}},
                     {"slugifiedAuthorized": {"$regex": person}}],
            "status":biz_status}).count()
        return {"result":result, "count":count}
    def search_biz_people(self, business, person, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            '$or': [{"slugifiedOwners": {"$regex": person}},
                     {"slugifiedAuthorized": {"$regex": person}}]}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            '$or': [{"slugifiedOwners": {"$regex": person}},
                     {"slugifiedAuthorized": {"$regex": person}}]}).count()
        return {"result":result, "count":count}

    def search_people_status_municipality(self, person, status, municipality, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            status: {"$regex": person},
            "slugifiedMunicipality": municipality}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            status: {"$regex": person},
            "slugifiedMunicipality": municipality}).count()
        return {"result":result, "count":count}
    def search_people_status(self, person, status, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            status: {"$regex": person}}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            status: {"$regex": person}}).count()
        return {"result":result, "count":count}
    def search_people_status_municipality_biz_stat(self, biz_status, person, person_status, municipality, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            person_status: {"$regex": person},
            "status": biz_status,
            "slugifiedMunicipality": municipality}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            person_status: {"$regex": person},
            "status": biz_status,
            "slugifiedMunicipality": municipality}).count()
        return {"result":result, "count":count}
    def search_people_status_biz_stat(self, biz_status, person, person_status, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            person_status: {"$regex": person},
            "status": biz_status}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            person_status: {"$regex": person},
            "status": biz_status}).count()
        return {"result":result, "count":count}
    def search_people_municipality_biz_stat(self, biz_status, person, municipality, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            '$or': [{"slugifiedOwners": {"$regex": person}},
                    {"slugifiedAuthorized": {"$regex": person}}],
            "status": biz_status,
            "slugifiedMunicipality": municipality}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            '$or': [{"slugifiedOwners": {"$regex": person}},
                    {"slugifiedAuthorized": {"$regex": person}}],
            "status": biz_status,
            "slugifiedMunicipality": municipality}).count()
        return {"result":result, "count":count}
    def search_people_municipality(self, person, municipality, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            '$or': [{"slugifiedOwners": {"$regex": person}},
                     {"slugifiedAuthorized": {"$regex": person}}],
            "slugifiedMunicipality": municipality}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            '$or': [{"slugifiedOwners": {"$regex": person}},
                     {"slugifiedAuthorized": {"$regex": person}}],
            "slugifiedMunicipality": municipality}).count()
        return {"result":result, "count":count}
    def search_people_biz_stat(self, biz_status, person, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            '$or': [{"slugifiedOwners": {"$regex": person}},
                     {"slugifiedAuthorized": {"$regex": person}}],
            "status":biz_status}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            '$or': [{"slugifiedOwners": {"$regex": person}},
                     {"slugifiedAuthorized": {"$regex": person}}],
            "status":biz_status}).count()
        return {"result":result, "count":count}
    def search_people(self, person, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            '$or': [{"slugifiedOwners": {"$regex": person}},
                     {"slugifiedAuthorized": {"$regex": person}}]}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            '$or': [{"slugifiedOwners": {"$regex": person}},
                     {"slugifiedAuthorized": {"$regex": person}}]}).count()
        return {"result":result, "count":count}
    def search_biz_by_status(self, business, biz_status, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            "status": biz_status}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            "status": biz_status}).count()
        return {"result":result, "count":count}


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
    def get_biz_by_municipality_status(self, business, municipality, biz_status, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            "slugifiedMunicipality": municipality,
            "status": biz_status}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find({
            "slugifiedBusiness": {"$regex": business},
            "slugifiedMunicipality": municipality,
            "status": biz_status}).count()
        return {"result":result, "count":count}
    def get_biz_by_municipality(self, business, municipality, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find(
            {"slugifiedBusiness": {"$regex": business},
             "slugifiedMunicipality": municipality}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find(
            {"slugifiedBusiness": {"$regex": business},
             "slugifiedMunicipality": municipality}).count()
        return {"result":result, "count":count}
    def get_biz(self, business, page, items_per_page):
        result = self.mongo.db[self.reg_businesses_collection].find(
            {"slugifiedBusiness": {"$regex": business}}).skip(items_per_page*(page-1)).limit(items_per_page)
        count = self.mongo.db[self.reg_businesses_collection].find(
            {"slugifiedBusiness": {"$regex": business}}).count()
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
    def get_profiles(self, people_type, person):
        result = self.mongo.db[self.reg_businesses_collection].find({people_type: {"$in": [person]}})
        return result

    # Top ten capital businesses
    def get_top_ten_by_capital(self):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([{'$sort': {"capital": -1}}, {'$limit': 10}])
        return result

    def get_top_ten_capital_by_status(self, business_status):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"status": business_status}},
            {'$sort': {"capital": -1}},
            {'$limit': 10}])
        return result

    def get_top_ten_capital_by_city(self, city):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"municipality.municipality": city}},
            {'$sort': {"capital": -1}},
            {'$limit': 10}])
        return result

    def get_top_ten_capital_by_city_status(self, business_status, city):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"status": business_status, "municipality.municipality": city}},
            {'$sort': {"capital": -1}},
            {'$limit': 10}])
        return result

    # Businesses through years queries
    def businesses_through_years(self, iteration):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"establishmentDate": {"$gt": datetime.datetime(iteration, 1, 1),
                                              "$lte": datetime.datetime(iteration+1, 1, 1)}}},
            {'$group': {"_id": "$status", "count": {"$sum": 1}}}])
        return result

    # Businesses type
    def get_biz_types_by_status(self, business_status):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"status":business_status}},
            {'$group': {"_id": "$type", "total": {"$sum": 1}}},
            {'$sort': {'total': -1}}
        ])
        return result

    def get_biz_types_by_city(self, city):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"municipality.municipality":city}},
            {'$group': {"_id": "$type", "total": {"$sum": 1}}},
            {'$sort': {'total': -1}}
        ])
        return result

    def get_biz_types_by_city_status(self, city, status):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"municipality.municipality":city, "status":status}},
            {'$group': {"_id": "$type", "total": {"$sum": 1}}},
            {'$sort': {'total': -1}}
        ])
        return result
    def get_biz_types_all(self):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$group': {"_id": "$type", "total": {"$sum": 1}}},
            {'$sort': {'total': -1}}
        ])
        return result
    def get_count_biz_types_city(self, city):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
        {'$match': {"municipality.municipality":city}},
        {'$count':"all"}
        ])
        return result
    def get_count_biz_types_status(self, status):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
        {'$match': {"status":status}},
        {'$count':"all"}
        ])
        return result
    def get_count_biz_types_city_status(self, status, city):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
        {'$match': {"municipality.municipality":city, "status":status}},
        {'$count':"all"}
        ])
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
                {'$unwind': "$activities"},
                {'$match': {"activities":int(code), "municipality.municipality":i}},
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
            muni.append(i['municipality'])
        result = {}
        for i in muni:
            res = self.mongo.db[self.reg_businesses_collection].aggregate([
                {'$unwind': "$activities"},
                {'$match': {"activities":int(code), "municipality.municipality":i, "status":status}},
                {'$count':"all"}
            ])
            try:
                result.update({i:res['result'][0]['all']})
            except Exception as e:
                result.update({i:0})
        return result

    def get_activities(self):
        acts = self.mongo.db[self.activities].find()
        activs = []
        for act in acts:
            activs.append({"activity":act['activity'],"code":act['code']})
        return activs
    # activities queries
    def get_most_used_activities(self):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$unwind': "$activities"},
            {'$group': {"_id": "$activities", 'totali': {'$sum': 1}}},
            {'$sort': {"totali": -1}}
        ])
        return result

    def get_activities_by_status(self, status):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {'status': status}},
            {'$unwind': "$activities"},
            {'$group': {"_id": "$activities", 'totali': {'$sum': 1}}},
            {'$sort': {"totali": -1}}
        ])
        return result

    def get_activities_by_municipality(self, city):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {'municipality.municipality': city}},
            {'$unwind': "$activities"},
            {'$group': {"_id": "$activities", 'totali': {'$sum': 1}}},
            {'$sort': {"totali": -1}}])
        return result

    def get_activities_by_status_municipality(self, status, city):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {'municipality.municipality': city, 'status': status}},
            {'$unwind': "$activities"},
            {'$group': {"_id": "$activities", 'totali': {'$sum': 1}}},
            {'$sort': {"totali": -1}}])
        return result

    # Get total businesses by status
    def get_total_by_status(self):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$group': {"_id": "$status", "total": {"$sum": 1}}},
            {'$sort':  {'total': -1}}])
        return result

    #Get owners count by gender
    def get_total_by_gender(self):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$unwind': "$owners"},
            {'$group': {"_id":"$owners.gender", "all":{"$sum":1}}},
            {'$sort': {"all":-1}}
        ])
        return result
    def get_count_total_gender(self):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$unwind': "$owners"},
            {'$count': "all"}
        ])
        return result
    def get_count_gen_types_status(self, status):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"status":status}},
            {'$unwind': "$owners"},
            {'$count':"all"}
        ])
        return result
    def get_gen_types_by_status(self, status):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"status":status}},
            {'$unwind': "$owners"},
            {'$group': {"_id":"$owners.gender", "all":{"$sum":1}}},
            {'$sort': {"all":-1}},
        ])
        return result
    def get_count_gen_types_city(self, city):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"municipality.municipality":city}},
            {'$unwind': "$owners"},
            {'$count':"all"}
        ])
        return result
    def get_gen_types_by_city(self, city):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"municipality.municipality":city}},
            {'$unwind': "$owners"},
            {'$group': {"_id":"$owners.gender", "all":{"$sum":1}}},
            {'$sort': {"sum":-1}}
        ])
        return result
    def get_count_gen_types_city_status(self, status, city):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"municipality.municipality":city, "status":status}},
            {'$unwind': "$owners"},
            {'$count':"all"}
        ])
        return result
    def get_gen_types_by_city_status(self, status, city):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([
            {'$match': {"municipality.municipality":city, "status":status}},
            {'$unwind': "$owners"},
            {'$group': {"_id":"$owners.gender", "all":{"$sum":1}}},
            {'$sort': {"sum":-1}}
        ])
        return result
