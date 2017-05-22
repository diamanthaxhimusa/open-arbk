from pymongo import MongoClient
import os, os.path, re, json, datetime, sys, csv
import time
import subprocess
import shutil

reload(sys)
sys.setdefaultencoding('utf-8')

client = MongoClient("mongodb://localhost:27017")
db = client['arbk']

# # DOWNLOADS
# def download_biz_by_year( year):
#     result = db.reg_businesses.find(
#         {"establishmentDate":
#             {"$gt": datetime.datetime(year, 1, 1),
#              "$lte": datetime.datetime(year+1, 1, 1)}})
#     return result

for year in range(2002,2018):
    query = "{"'"establishmentDate"'":{"'"$gt"'": ISODate("'"%s-01-01T00:00:00.000Z"'"),"'"$lte"'": ISODate("'"%s-01-01T00:00:00.000Z"'")}}"%(str(year),str(year+1))
    cmd="mongoexport -d arbk -c reg_businesses -q '%s' --type=csv --fields registrationNum,name,status,owners,authorized,capital,municipality.municipality,municipality.place,arbkUrl,activities --out app/static/downloads/arbk-%s.csv"%(query,year)
    print subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
    cmd="mongoexport -d arbk -c reg_businesses -q '%s' --out app/static/downloads/arbk-%s.json"%(query,year)
    print subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
    # cursor = download_biz_by_year(year)
    # filename = 'app/static/downloads/arbk-%s.json'%year
    # with open(filename, 'w') as f:
    #     for doc in cursor:
    #         f.write('%s\n'%doc)
# def set_name_to_activities(given_code):
#     activities_collection =db.activities.find()
#     name = ''
#     for activity in activities_collection:
#         if str(given_code) == activity['code']:
#             name = activity['activity']
#         else:
#             continue
#     return name
# for year in range(2002,2018):
#     cursor = download_biz_by_year(year)
#     with open('app/static/downloads/arbk-%s.csv'%year, 'w') as csvfile:
#         fieldnames = ['Emri i biznesit', 'Statusi', 'Pronare', 'Linku ne arbk', 'Numri i regjistrimit', 'Komuna', 'Vendi', 'Aktivitetet']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         for doc in cursor:
#             acts = ''
#             owners = ''
#             for i in doc['activities']:
#                 dc = set_name_to_activities(i)
#                 acts += '%s-%s\n'%(str(i),dc)
#             for owner in doc['owners']:
#                 owners += '%s\n'%owner['name']
#             writer.writerow({'Emri i biznesit': doc['name'], 'Statusi':doc['status'], 'Pronare':owners, 'Linku ne arbk': doc['arbkUrl'], 'Numri i regjistrimit': doc['registrationNum'], 'Komuna': doc['municipality']['municipality'], 'Vendi':doc['municipality']['place'], 'Aktivitetet':acts})
