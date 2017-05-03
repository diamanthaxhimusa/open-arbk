#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import os, os.path, re, json, datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

client = MongoClient("mongodb://localhost:27017")
db = client['arbk']

with open("data-importer/activities.json","r") as data:
    activities = json.load(data)
    for activity in activities['activities']:
        db.activities.insert(activity)

with open("data-importer/komunat.json","r") as data:
    municipalities = json.load(data)
    for municipality in municipalities:
        place = []
        for muni_place in municipalities[municipality]:
            place.append(muni_place)
        db.municipalities.insert({"municipality":municipality, "districts":place})
def slug_data(slug_string):
	# Slugifying each string and then updating new elements in 'formatted' docs with slugified strings
    slugified_string = slug_string
    if "ë" in slug_string or "Ë" in slug_string:
    	slugified_string = slugified_string.lower().replace("ë", "e").decode('utf-8')
    elif "ç".decode('utf-8') in slug_string.decode('utf-8') or "Ç".decode('utf-8') in slug_string.decode('utf-8'):
    	slugified_string = slugified_string.lower().replace("ç", "c").decode('utf-8')
    slugified_string = re.sub(r'[,|?|$|/|\|"]',r'', slugified_string)
    return slugified_string.lower()

def set_muni(given_city_bus):
    with open("data-importer/komunat.json","r") as data:
        municipalities = json.load(data)
    	cities = {}
    	found = False
    	for place in municipalities:
            for city in municipalities[place]:
                if city != '_id':
        			for village in municipalities[place]:
        				if village == given_city_bus:
        					found = True
        					cities = {
        						"municipality": place,
        						"place": given_city_bus
        					}
    	if found:
    		return cities
    	else:
    		cities = {
    			"municipality": "Unknown",
    			"place": given_city_bus
    		}
    		return cities

def gender_person(person):
    with open("data-importer/gender_people.json","r") as data2:
        names = json.load(data2)
        owner = {}
        divide = person.split(" ")
        # for gender in names:
    	if divide[0].title() in names['females']:
    		owner = {"name":person, "gender" : "female"}
    	elif divide[0].title() in names['males']:
    		owner = {"name":person, "gender" : "male"}
    	else:
    		owner = {"name":person, "gender" : "unknown"}
        return owner

def main():
    docs = db.businesses.find()
    # Looping through each doc
    for doc in docs:
        sluged_owners = []
        gender_owners = []
        slug_auth = []
        gen_auth = []
        city = {}
        epl_nr = 0
        capi = 0
        # Looping in owner array of 'formatted' JSON in docs
        for owner in doc['formatted']['owners']:
            slugified_owner_string = slug_data(owner)
            sluged_owners.append(slugified_owner_string)
            gender_owner = gender_person(owner)
            gender_owners.append(gender_owner)
            slugified_company_string = re.sub(r'[,|?|$|/|\|"]',r'', doc['formatted']['name'])
        for authorized in doc['formatted']['authorized']:
            slugified_authorized_string = slug_data(authorized)
            gender_authorized = gender_person(authorized)
            slug_auth.append(slugified_authorized_string)
            gen_auth.append(gender_authorized)

        try:
            city = set_muni(doc['formatted']['municipality'])
        except Exception as e:
            pass
        try:
            establishmentDate = doc['formatted']['establishmentDate']
        except Exception as e:
            pass
        try:
            reg_num = doc['formatted']['registrationNum']
        except Exception as e:
            continue
        try:
            atkStatus = doc['formatted']['atkStatus']
        except Exception as e:
            atkStatus = '//'
        try:
            buss_type = doc['formatted']['type']
        except Exception as e:
            buss_type = ''
        try:
            applicationDate = doc['formatted']['applicationDate']
        except Exception as e:
            applicationDate = None
        try:
            arbkUrl = doc['formatted']['arbkUrl']
        except Exception as e:
            arbkUrl = None
        try:
            status = doc['formatted']['status']
        except Exception as e:
            status = ''
        try:
            if doc['formatted']['capital'] is None:
                capi = 0
            else:
                capi = int(doc['formatted']['capital'])
        except Exception as e:
            pass

        try:
            if doc['formatted']['employeeCount'] is None:
                epl_nr = 0
            else:
                epl_nr = doc['formatted']['employeeCount']
        except Exception as e:
            pass
        db.reg_businesses.insert({
        "registrationNum": reg_num,
        "type": buss_type,
        "employeeCount": epl_nr,
        "applicationDate": applicationDate,
        "capital": capi,
        "atkStatus": atkStatus,
        "status": status,
        "arbkUrl": arbkUrl,
        "activities": doc['formatted']['activities'],
        "slugifiedOwners": sluged_owners,
        "establishmentDate": establishmentDate,
        "owners": gender_owners,
        "name": slugified_company_string,
        "slugifiedAuthorized": slug_auth,
        "authorized": gen_auth,
        "municipality": city,
        "timestamp": datetime.datetime.now()
        })

main()
