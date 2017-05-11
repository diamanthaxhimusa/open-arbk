import datetime


class MongoUtils(object):

    def __init__(self, mongo):
        self.mongo = mongo
        self.reg_businesses_collection = 'reg_businesses'
        self.municipalities = 'municipalities'
        self.activities = 'activities'

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

    def get_limit_businesses(self, num):
        result = self.mongo.db[self.reg_businesses_collection].find().limit(num)
        return result

    def get_municipalities(self):
        result = self.mongo.db[self.municipalities].find().sort("municipality", 1)
        return result

    def get_people(self, people_type, keyword):
        result = self.mongo.db[self.reg_businesses_collection].find({people_type: {"$regex": keyword}})
        return result

    def get_people_by_municipality(self, people_type, keyword, municipality):
        result = self.mongo.db[self.reg_businesses_collection].find(
            {people_type: {"$regex": keyword},
             "municipality.municipality": municipality})
        return result

    def get_by_owners_authorized(self, keyword):
        result = self.mongo.db[self.reg_businesses_collection].find(
            {'$or': [{"slugifiedOwners": {"$regex": keyword}},
                     {"slugifiedAuthorized": {"$regex": keyword}}]})
        return result
    def get_by_owners_authorized_municipality(self, keyword, municipality):
        result = self.mongo.db[self.reg_businesses_collection].find(
            {'$or': [{"slugifiedOwners": {"$regex": keyword}},
                     {"slugifiedAuthorized": {"$regex": keyword}}], "municipality.municipality":municipality})
        return result

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
    def map(self):
        result = self.mongo.db[self.reg_businesses_collection].aggregate([{'$group': {"_id":"$municipality.municipality", "count":{"$sum":1}}}])
        return result

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
