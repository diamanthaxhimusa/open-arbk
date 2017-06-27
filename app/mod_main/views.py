#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, Response, request, send_file, send_from_directory
from app import mongo_utils, download_folder
from bson import json_util
from slugify import slugify
import re, unidecode, urllib
import sys, csv, json, math
reload(sys)

mod_main = Blueprint('main', __name__)

@mod_main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # Get the search values from url
        items_per_page = 10
        search_keyword = request.args.get('person', default="", type=str)
        business_keyword = request.args.get('business', default="", type=str)
        status = request.args.get('person-status', default="any", type=str)
        city = request.args.get('municipality', default="any", type=str)
        biz_status = request.args.get('biz-status', default="any", type=str)
        page = request.args.get('page', default=1, type=int)
        business = slugify(business_keyword.lower())
        person = slugify(search_keyword.lower())
        person_status = ""
        if status == "auth":
            person_status = "slugifiedAuthorized"
        elif status == "owner":
            person_status = "slugifiedOwners"
        else:
            person_status = "any"
        municipalities = mongo_utils.get_municipalities()
        # Call the search_engine function from mongo_utils
        result = mongo_utils.search_engine(page, items_per_page, business, biz_status, person, person_status, city)
        # docs_count is the number of the documents that are found without limits, for pagination.
        docs_count = result['count']
        return render_template('index.html',search_result=result['result'], count=docs_count, items_per_page=items_per_page, municipalities = municipalities)

@mod_main.route('/kerko/<string:status>/<string:person>', methods=['GET', 'POST'])
def profile(status, person):
    items_per_page = 10
    page = request.args.get('page', default=1, type=int)
    person_to_lower = slugify(person.lower())
    municipalities = mongo_utils.get_municipalities()
    if status == 'owner':
        person_data = mongo_utils.get_profiles("slugifiedOwners", person_to_lower, page, items_per_page)
    else:
        person_data = mongo_utils.get_profiles("slugifiedAuthorized", person_to_lower, page, items_per_page)
    return render_template('profile.html', profile_data=person_data['result'], count=person_data['count'],
                           municipalities=municipalities, status=status, person=person, items_per_page=items_per_page)

@mod_main.route('/rekomandimet', methods=['GET'])
def recommendation():
   if request.method == 'GET':
       return render_template('recommendationPage.html')

@mod_main.route('/vizualizimet', methods=['GET', 'POST'])
def visualization():
    if request.method == 'GET':
        activities = mongo_utils.get_activities()
        top = mongo_utils.get_top_ten_businesses("any","any")
        komunat = mongo_utils.get_municipalities()
        return render_template('visualizations.html', top=top, komunat=komunat, activities=activities)
    if request.method == 'POST':
        city = request.form['city_id']
        status = request.form['status']
        top = mongo_utils.get_top_ten_businesses(status, city)
        return Response(response=json_util.dumps(top), status=200, mimetype='application/json')

@mod_main.route('/through-years', methods=['GET', 'POST'])
def start_date():
    api = {}
    y = 3
    for i in range(2003, 2017):
        year = "d" + str(y)
        y += 1
        data = mongo_utils.businesses_through_years(i)
        if len(data['result']) == 1:
            if data['result'][0]['_id'] == "Aktiv":
                data['result'].append({"_id": "Shuar", "count": 0})
            else:
                data['result'].append({"_id": "Aktiv", "count": 0})
        res = {data['result'][0]['_id']: data['result'][0]['count'],data['result'][1]['_id']: data['result'][1]['count']}
        api.update({year: res})
    return Response(response=json_util.dumps(api), status=200, mimetype='application/json')

@mod_main.route('/activities-years', methods=['GET', 'POST'])
def activity_years():
    if request.method == 'POST':
        activity = request.form['activity']
        api = {}
        y = 3
        for i in range(2003, 2017):
            year = "d" + str(y)
            y += 1
            data = mongo_utils.activity_years(i, activity)
            if len(data['result']) == 0:
                data['result'].append({"_id": "Shuar", "count": 0})
                data['result'].append({"_id": "Aktiv", "count": 0})
            elif len(data['result']) == 1:
                if data['result'][0]['_id'] == "Aktiv":
                    data['result'].append({"_id": "Shuar", "count": 0})
                else:
                    data['result'].append({"_id": "Aktiv", "count": 0})
            res = {data['result'][0]['_id']: data['result'][0]['count'],data['result'][1]['_id']: data['result'][1]['count']}
            api.update({year: res})
        return Response(response=json_util.dumps(api), status=200, mimetype='application/json')

@mod_main.route('/businesses-type', methods=['GET', 'POST'])
def businesses_type():
    if request.method == 'GET':
        doc = mongo_utils.get_business_types("any","any")
        docs_count = mongo_utils.docs_count()
        api = {'total': docs_count, 'doc': doc}
        return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
    if request.method == 'POST':
        city = request.form['biz_city_id']
        status = request.form['biz_status']
        docs_count = mongo_utils.get_count_biz_types(status, city)
        doc = mongo_utils.get_business_types(city, status)
        api = {'total': docs_count['result'][0]['all'], 'doc': doc}
        return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
    return 'error'

def set_name_to_activities(given_code):
    activities_collection = mongo_utils.get_all_activities()
    docs = {}
    for activity in activities_collection:
        if str(given_code) == activity['code']:
            docs = {
                "code": given_code,
                "activity": activity['activity']
            }
        else:
            continue
    return docs

def prepare_activity_api(activities_collection):
    activity_items = []
    for activity in activities_collection['result']:
        activity_set = set_name_to_activities(activity['_id'])
        if len(activity_set) != 0:
            activity_items.append({
                "total_businesses": activity['totali'],
                "details": activity_set
            })
    activities_api = {'activities': activity_items}
    return activities_api

@mod_main.route('/top-activities', methods=['GET', 'POST'])
def activities():
    if request.method == 'GET':
        all_businesses_activities = mongo_utils.get_most_used_activities("any","any")
        result = prepare_activity_api(all_businesses_activities)
        return Response(response=json_util.dumps(result), status=200, mimetype='application/json')
    elif request.method == 'POST':
        city = request.form['city']
        status = request.form['status']
        business_activities = mongo_utils.get_most_used_activities(status, city)
        result = prepare_activity_api(business_activities)
        return Response(response=json_util.dumps(result), status=200, mimetype='application/json')
    return "Error"

@mod_main.route('/active-inactive', methods=['GET', 'POST'])
def active_inactive():
    docs = mongo_utils.get_total_by_status()
    api = {
            'total': mongo_utils.docs_count(),
            'docs': docs
    }
    return Response(response=json_util.dumps(api), status=200, mimetype='application/json')

@mod_main.route('/harta', methods=['GET', 'POST'])
def activity_map():
    activities = mongo_utils.get_activities()
    return render_template('activity-map.html', activities=activities)

@mod_main.route('/mapi', methods=['GET', 'POST'])
def mapi():
    if request.method == 'GET':
        agg = mongo_utils.mapi_all()
        return Response(response=json_util.dumps(agg), status=200, mimetype='application/json')
    if request.method == 'POST':
        activity = request.form['activity_name']
        status = request.form['status']
        if activity != "all":
            if status == "Aktiv" or status == "Shuar":
                agg = mongo_utils.mapi_status(activity, status)
            else:
                agg = mongo_utils.mapi(activity)
        else:
            if status == "Aktiv" or status == "Shuar":
                agg = mongo_utils.mapi_all_status(status)
            else:
                agg = mongo_utils.mapi_all()
        return Response(response=json_util.dumps(agg), status=200, mimetype='application/json')
    return Response(response='Error', status=404, mimetype='application/json')

@mod_main.route('/gender-owners', methods=['GET', 'POST'])
def gender_owners():
    if request.method == 'GET':
        docs = mongo_utils.get_gender_owners_data("any","any")
        total = mongo_utils.get_gender_owners_data_count("any","any")
        api = {
            'total': total['result'][0]['all'],
            'doc': docs
        }
        return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
    if request.method == 'POST':
        city = request.form['biz_city_id']
        status = request.form['biz_status']
        docs_count = mongo_utils.get_gender_owners_data_count(status, city)
        doc = mongo_utils.get_gender_owners_data(status, city)
        api = {
            'total': docs_count['result'][0]['all'],
            'doc': doc
        }
        return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
    return 'error'

@mod_main.route('/top-10-gender-activities', methods=['GET', 'POST'])
def top_gender_acts():
    if request.method == 'GET':
        docs_females = mongo_utils.get_top_ten_activities_by_gender("female")
        docs_males = mongo_utils.get_top_ten_activities_by_gender("male")
        result_females = prepare_activity_api(docs_females)
        result_males = prepare_activity_api(docs_males)
        result = {"females":result_females, "males":result_males}
        return Response(response=json_util.dumps(result), status=200, mimetype='application/json')
    return 'error'

@mod_main.route('/employees', methods=['GET'])
def employee():
    result = mongo_utils.get_puntor()
    return Response(response=json_util.dumps(result), status=200, mimetype='application/json')


@mod_main.route('/shkarko', methods=['GET', 'POST'])
def download_page():
    return render_template('downloads.html')

@mod_main.route('/shkarko/<string:doc_type>/<string:doc_date_type>/<string:year>', methods=['GET'])
def download_doc_year(doc_type, doc_date_type, year):
    if year == "2017":
        return send_from_directory(download_folder, "arbk-%s(%s)(pakompletuar).%s"%(year,doc_date_type, doc_type), as_attachment=True)
    return send_from_directory(download_folder, "arbk-%s(%s).%s"%(year,doc_date_type, doc_type), as_attachment=True)

@mod_main.route('/shkarko/<string:doc_type>/all-zip', methods=['GET'])
def download_doc_all(doc_type):
    return send_from_directory(download_folder, "arbk-data-%s.zip"%doc_type, as_attachment=True)
