from pymongo import MongoClient
import os, os.path, re, json, datetime, sys, csv, time, subprocess, shutil, zipfile
from bson import json_util
from cStringIO import StringIO
reload(sys)
sys.setdefaultencoding('utf-8')

client = MongoClient("mongodb://localhost:27017")
db = client['arbk']

if not os.path.exists('app/static/downloads'):
    try:
        print 'creating downloads folder'
        os.makedirs('app/static/downloads')
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

# DOWNLOADS
def download_biz_by_year(type_of_date,year):
    result = db.reg_businesses.find(
        {type_of_date:
            {"$gt": datetime.datetime(year, 1, 1),
             "$lte": datetime.datetime(year+1, 1, 1)}})
    return result

def set_name_to_activities(given_code):
    activities_collection =db.activities.find()
    name = ''
    for activity in activities_collection:
        if str(given_code) == activity['code']:
            name = activity['activity']
        else:
            continue
    return name

def make_json(download_dir, range_download_year, type_of_date):
    for year in range_download_year:
        print 'creating %s documents: arbk-%s.json'%(type_of_date, year)
        if year == 2017:
            if type_of_date == "applicationDate":
                filename_json = '%s/arbk-%s(dataAplikimit)(pakompletuar).json'%(download_dir, year)
            else:
                filename_json = '%s/arbk-%s(dataFillimit)(pakompletuar).json'%(download_dir, year)
        else:
            if type_of_date == "applicationDate":
                filename_json = '%s/arbk-%s(dataAplikimit).json'%(download_dir, year)
            else:
                filename_json = '%s/arbk-%s(dataFillimit).json'%(download_dir, year)
        if os.path.isfile(filename_json):
            print 'json exitsts: %s' % filename_json
        else:
            cursor = download_biz_by_year(type_of_date,year)
            with open(filename_json, 'w') as jsonfile:
                jsonfile.write(json_util.dumps(cursor))

def make_csv(download_dir, range_download_year, type_of_date):
    for year in range_download_year:
        print 'creating %s documents: arbk-%s.csv'%(type_of_date, year)
        if year == 2017:
            if type_of_date == "applicationDate":
                filename_csv = '%s/arbk-%s(dataAplikimit)(pakompletuar).csv'%(download_dir, year)
            else:
                filename_csv = '%s/arbk-%s(dataFillimit)(pakompletuar).csv'%(download_dir, year)
        else:
            if type_of_date == "applicationDate":
                filename_csv = '%s/arbk-%s(dataAplikimit).csv'%(download_dir, year)
            else:
                filename_csv = '%s/arbk-%s(dataFillimit).csv'%(download_dir, year)
        if os.path.isfile(filename_csv):
            print 'csv exitsts: %s' % filename_csv
        else:
            cursor = download_biz_by_year(type_of_date,year)
            with open(filename_csv, 'w') as csvfile:
                fieldnames = ['Emri i biznesit', 'Statusi','Tipi i biznesit','Kapitali', 'Pronar'u'\xeb''','Data e fillimit','Data e aplikimit', 'Linku n'u'\xeb'' arbk', 'Numri i regjistrimit', 'Vendi', 'Aktivitetet', 'Data e marrjes s'u'\xeb'' t'u'\xeb'' dh'u'\xeb''nave']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for doc in cursor:
                    acts = ''
                    owners = ''
                    for i in doc['activities']:
                        dc = set_name_to_activities(i)
                        acts += '%s-%s\n'%(str(i),dc.encode('utf-8'))
                    for owner in doc['owners']:
                        owners += '%s\n'%owner['name'].encode('utf-8')
                    row = {'Emri i biznesit': doc['name'], 'Statusi':doc['status'],'Tipi i biznesit':doc['type'] , 'Kapitali':doc['capital'],'Pronar'u'\xeb''':owners,'Data e fillimit': doc['establishmentDate'],'Data e aplikimit': doc['applicationDate'], 'Linku n'u'\xeb'' arbk': doc['arbkUrl'], 'Numri i regjistrimit': doc['registrationNum'], 'Vendi':doc['municipality']['place'], 'Aktivitetet':acts, 'Data e marrjes s'u'\xeb'' t'u'\xeb'' dh'u'\xeb''nave': doc['dataRetrieved']}
                    writer.writerow(DictUnicodeProxy(row))

def make_all_data_zip_csv(download_dir):
    filename_csv = '%s/arbk-data.csv'%download_dir
    if os.path.isfile(filename_csv):
        print 'arbk-data(csv).zip exitsts. Skipping'
    else:
        cursor = db.reg_businesses.find()
        print 'creating file: arbk-data(csv).zip'
        with open(filename_csv, 'w') as csvfile:
            fieldnames = ['Emri i biznesit', 'Statusi','Tipi i biznesit','Kapitali', 'Pronar'u'\xeb''','Data e fillimit','Data e aplikimit', 'Linku n'u'\xeb'' arbk', 'Numri i regjistrimit', 'Vendi', 'Aktivitetet', 'Data e marrjes s'u'\xeb'' t'u'\xeb'' dh'u'\xeb''nave']
            csvwriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
            csvwriter.writeheader()
            try:
                for doc in cursor:
                    print 'printing doc: [%s]'%doc['name']
                    acts = ''
                    owners = ''
                    for i in doc['activities']:
                        dc = set_name_to_activities(i)
                        acts += '%s-%s\n'%(str(i),dc.encode('utf-8'))
                    for owner in doc['owners']:
                        owners += '%s\n'%owner['name'].encode('utf-8')
                    row = {'Emri i biznesit': doc['name'], 'Statusi':doc['status'],'Tipi i biznesit':doc['type'] , 'Kapitali':doc['capital'],'Pronar'u'\xeb''':owners,'Data e fillimit': doc['establishmentDate'],'Data e aplikimit': doc['applicationDate'], 'Linku n'u'\xeb'' arbk': doc['arbkUrl'], 'Numri i regjistrimit': doc['registrationNum'], 'Vendi':doc['municipality']['place'], 'Aktivitetet':acts, 'Data e marrjes s'u'\xeb'' t'u'\xeb'' dh'u'\xeb''nave': doc['dataRetrieved']}
                    csvwriter.writerow(DictUnicodeProxy(row))
            except Exception as e:
                print str(e)

class DictUnicodeProxy(object):
    def __init__(self, d):
        self.d = d
    def __iter__(self):
        return self.d.__iter__()
    def get(self, item, default=None):
        i = self.d.get(item, default)
        if isinstance(i, unicode):
            return i.encode('utf-8')
        return i

download_dir = 'app/static/downloads'
range_download_year = range(2002,2018)
make_json(download_dir, range_download_year, "establishmentDate")
make_json(download_dir, range_download_year, "applicationDate")
make_csv(download_dir, range_download_year, "establishmentDate")
make_csv(download_dir, range_download_year, "applicationDate")
make_all_data_zip_csv(download_dir)
