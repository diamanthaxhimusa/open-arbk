from pymongo import MongoClient
import os, os.path, re, json, datetime, sys, csv, time, subprocess, shutil
import zipfile
from bson import json_util
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
def download_biz_by_year( year):
    result = db.reg_businesses.find(
        {"establishmentDate":
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

def make_json(download_dir, range_download_year):
    for year in range_download_year:
        cursor = download_biz_by_year(year)
        print 'creating file: arbk-%s.json'%year
        filename_json = '%s/arbk-%s.json'%(download_dir, year)
        with open(filename_json, 'w') as jsonfile:
            jsonfile.write(json_util.dumps(cursor))
def make_csv(download_dir, range_download_year):
    for year in range_download_year:
        cursor = download_biz_by_year(year)
        print 'creating file: arbk-%s.csv'%year
        filename_csv = '%s/arbk-%s.csv'%(download_dir, year)
        with open(filename_csv, 'w') as csvfile:
            fieldnames = ['Emri i biznesit', 'Statusi','Tipi i biznesit','Kapitali', 'Pronar'u'\xeb''','Data e fillimit','Data e aplikimit', 'Linku n'u'\xeb'' arbk', 'Numri i regjistrimit', 'Vendi', 'Aktivitetet']
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
                row = {'Emri i biznesit': doc['name'], 'Statusi':doc['status'],'Tipi i biznesit':doc['type'] , 'Kapitali':doc['capital'],'Pronar'u'\xeb''':owners,'Data e fillimit': doc['establishmentDate'],'Data e aplikimit': doc['applicationDate'], 'Linku n'u'\xeb'' arbk': doc['arbkUrl'], 'Numri i regjistrimit': doc['registrationNum'], 'Vendi':doc['municipality']['place'], 'Aktivitetet':acts}
                writer.writerow(DictUnicodeProxy(row))
def make_all_data_zip(download_dir):
    cursor = db.reg_businesses.find()
    filename_json = "arbk-data.json"
    try:
        import zlib
        compression = zipfile.ZIP_DEFLATED
    except:
        compression = zipfile.ZIP_STORED

    modes = { zipfile.ZIP_DEFLATED: 'deflated',
              zipfile.ZIP_STORED:   'stored',
              }

    zf = zipfile.ZipFile('%s/arbk-data.zip'%download_dir, mode='w')
    try:
        print 'adding arbk-data.zip', modes[compression]
        zf.writestr(filename_json, json_util.dumps(cursor))
    finally:
        print 'closing'
        zf.close()

download_dir = 'app/static/downloads'
range_download_year = range(2002,2018)
# make_json(download_dir, range_download_year)
# make_csv(download_dir, range_download_year)
make_all_data_zip(download_dir)
# query = "{"'"establishmentDate"'":{"'"$gt"'": ISODate("'"%s-01-01T00:00:00.000Z"'"),"'"$lte"'": ISODate("'"%s-01-01T00:00:00.000Z"'")}}"%(str(year),str(year+1))
# cmd="mongoexport -d arbk -c reg_businesses -q '%s' --out app/static/downloads/arbk-%s.json"%(query,year)
# print subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
# cmd="mongoexport -d arbk -c reg_businesses -q '%s' --type=csv --fields registrationNum,name,status,owners,authorized,capital,municipality.municipality,municipality.place,arbkUrl,activities --out app/static/downloads/arbk-%s.csv"%(query,year)
# print subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
