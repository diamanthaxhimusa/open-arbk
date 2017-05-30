#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, Response, request, send_file, send_from_directory
from app import mongo_utils, download_folder
from bson import json_util
import sys, csv, json
reload(sys)

mod_main = Blueprint('main', __name__)


def search_engine(business, biz_status, person, person_status, municipality):
    if business == "" and person == "":
        result = mongo_utils.get_limit_businesses(100)
        return result
    elif business == "" and person != "":
        if person_status == "any" and biz_status == "any" and municipality == "any":
            result = mongo_utils.search_people(person)
            return result
        elif person_status == "any" and biz_status == "any" and municipality != "any":
            result = mongo_utils.search_people_municipality(person, municipality)
            return result
        elif person_status == "any" and biz_status != "any" and municipality == "any":
            result = mongo_utils.search_people_biz_stat(biz_status, person)
            return result
        elif person_status == "any" and biz_status != "any" and municipality != "any":
            result = mongo_utils.search_people_municipality_biz_stat(biz_status, person, municipality)
            return result
        elif person_status != "any" and biz_status == "any" and municipality == "any":
            result = mongo_utils.search_people_status(person, person_status)
            return result
        elif person_status != "any" and biz_status == "any" and municipality != "any":
            result = mongo_utils.search_people_status_municipality(person, person_status, municipality)
            return result
        elif person_status != "any" and biz_status != "any" and municipality == "any":
            result = mongo_utils.search_people_status_biz_stat(biz_status, person, person_status)
            return result
        elif person_status != "any" and biz_status != "any" and municipality != "any":
            result = mongo_utils.search_people_status_municipality_biz_stat(biz_status, person, person_status, municipality)
            return result
        return 'error'
    elif business != "" and person == "":
        if municipality == "any" and biz_status == "any":
            result = mongo_utils.get_biz(business)
            return result
        elif municipality == "any" and biz_status != "any":
            result = mongo_utils.search_biz_by_status(business, biz_status)
            return result
        elif municipality !="any" and biz_status == "any":
            result = mongo_utils.get_biz_by_municipality(business, municipality)
            return result
        elif municipality !="any" and biz_status != "any":
            result = mongo_utils.get_biz_by_municipality_status(business, municipality, biz_status)
            return result
        return 'error'
    elif business !="" and person != "":
        if person_status == "any" and biz_status == "any" and municipality == "any":
            result = mongo_utils.search_biz_people(business, person)
            return result
        elif person_status == "any" and biz_status == "any" and municipality != "any":
            result = mongo_utils.search_biz_people_municipality(business, person, municipality)
            return result
        elif person_status == "any" and biz_status != "any" and municipality == "any":
            result = mongo_utils.search_biz_status_people(business, biz_status, person)
            return result
        elif person_status == "any" and biz_status != "any" and municipality != "any":
            result = mongo_utils.search_biz_status_people_municipality(business, biz_status, person, municipality)
            return result
        elif person_status != "any" and biz_status == "any" and municipality == "any":
            result = mongo_utils.search_biz_people_status(business, person, person_status)
            return result
        elif person_status != "any" and biz_status == "any" and municipality != "any":
            result = mongo_utils.search_biz_people_status_municipality(business, person, person_status, municipality)
            return result
        elif person_status != "any" and biz_status != "any" and municipality == "any":
            result = mongo_utils.search_biz_status_people_status(business, biz_status, person, person_status)
            return result
        elif person_status != "any" and biz_status != "any" and municipality != "any":
            result = mongo_utils.search_biz_status_people_status_municipality(business, biz_status, person, person_status, municipality)
            return result
        return result
    else:
        result = "error"
    return result

@mod_main.route('/', methods=['GET', 'POST'])
def index():
    municipalities = mongo_utils.get_municipalities()
    return render_template('index.html', municipalities = municipalities)
@mod_main.route('/search-result', methods=['GET', 'POST'])
def search_result():
    if request.method == 'GET':
        mongo_utils.index_create()
        municipalities = mongo_utils.get_municipalities()
        result = mongo_utils.get_limit_businesses(100)
        return Response(response=json_util.dumps(result), status=200, mimetype='application/json')
    if request.method == 'POST':
        mongo_utils.index_create()
        municipalities = mongo_utils.get_municipalities()
        search_keyword = request.form['person']
        business_keyword = request.form['business']
        business = business_keyword.lower()
        person = search_keyword.lower()
        status = request.form['person_status']
        city = request.form['municipality']
        biz_status = request.form['biz_status']
        person_status = ""
        if status == "auth":
            person_status = "slugifiedAuthorized"
        elif status == "owner":
            person_status = "slugifiedOwners"
        else:
            person_status = "any"
        result = search_engine(business, biz_status, person, person_status, city)
        print result
        return Response(response=json_util.dumps(result), status=200, mimetype='application/json')

@mod_main.route('/search/<string:status>/<string:person>', methods=['GET', 'POST'])
def profile(status, person):
    person_to_lower = person.lower()
    municipalities = mongo_utils.get_municipalities()
    if status == 'owner':
        person_data = mongo_utils.get_profiles("slugifiedOwners", person_to_lower)
    else:
        person_data = mongo_utils.get_profiles("slugifiedAuthorized", person_to_lower)
    return render_template('profile.html', profile_data=person_data,
                           municipalities=municipalities, status=status, person=person)

@mod_main.route('/visualization', methods=['GET', 'POST'])
def visualization():
    if request.method == 'GET':
        top = mongo_utils.get_top_ten_by_capital()
        komunat = mongo_utils.get_municipalities()
        return render_template('visualizations.html', top=top, komunat=komunat)
    if request.method == 'POST':
        city = request.form['city_id']
        status = request.form['status']
        if status == 'any' and city == 'any':
            top = mongo_utils.get_top_ten_by_capital()
            return Response(response=json_util.dumps(top), status=200, mimetype='application/json')
        elif status != 'any' and city == 'any':
            top = mongo_utils.get_top_ten_capital_by_status(status)
            return Response(response=json_util.dumps(top), status=200, mimetype='application/json')
        elif status == 'any' and city != 'any':
            top = mongo_utils.get_top_ten_capital_by_city(city)
            return Response(response=json_util.dumps(top), status=200, mimetype='application/json')
        else:
            top = mongo_utils.get_top_ten_capital_by_city_status(status, city)
            return Response(response=json_util.dumps(top), status=200, mimetype='application/json')

@mod_main.route('/through-years', methods=['GET', 'POST'])
def start_date():
    api = {}
    y = 1
    for i in range(2002, 2018):
        y += 1
        year = "d" + str(y)
        data = mongo_utils.businesses_through_years(i)
        if len(data['result']) == 1:
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
        doc = mongo_utils.get_biz_types_all()
        docs_count = mongo_utils.docs_count()
        api = {'total': docs_count, 'doc': doc}
        return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
    if request.method == 'POST':
        city = request.form['biz_city_id']
        status = request.form['biz_status']
        if status != 'any' and city == 'any':
            docs_count = mongo_utils.get_count_biz_types_status(status)
            doc = mongo_utils.get_biz_types_by_status(status)
            api = {'total': docs_count['result'][0]['all'], 'doc': doc}
            return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
        elif status == 'any' and city != 'any':
            docs_count = mongo_utils.get_count_biz_types_city(city)
            doc = mongo_utils.get_biz_types_by_city(city)
            api = {'total': docs_count['result'][0]['all'], 'doc': doc}
            return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
        elif status == 'any' and city == 'any':
            docs_count = mongo_utils.docs_count()
            doc = mongo_utils.get_biz_types_all()
            api = {'total': docs_count, 'doc': doc}
            return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
        else:
            docs_count = mongo_utils.get_count_biz_types_city_status(status, city)
            doc = mongo_utils.get_biz_types_by_city_status(city, status)
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
        all_businesses_activities = mongo_utils.get_most_used_activities()
        result = prepare_activity_api(all_businesses_activities)
        return Response(response=json_util.dumps(result), status=200, mimetype='application/json')
    elif request.method == 'POST':
        city = request.form['city']
        status = request.form['status']
        if status == 'any' and city == 'any':
            business_activities = mongo_utils.get_most_used_activities()
            result = prepare_activity_api(business_activities)
            return Response(response=json_util.dumps(result), status=200, mimetype='application/json')
        elif status != 'any' and city == 'any':
            business_activities = mongo_utils.get_activities_by_status(status)
            result = prepare_activity_api(business_activities)
            return Response(response=json_util.dumps(result), status=200, mimetype='application/json')
        elif status == 'any' and city != 'any':
            business_activities = mongo_utils.get_activities_by_municipality(city)
            result = prepare_activity_api(business_activities)
            return Response(response=json_util.dumps(result), status=200, mimetype='application/json')
        else:
            business_activities = mongo_utils.get_activities_by_status_municipality(status, city)
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

@mod_main.route('/activity-map', methods=['GET', 'POST'])
def activity_map():
    activities = mongo_utils.get_activities()
    return render_template('activity-map.html', activities=activities)

@mod_main.route('/mapi', methods=['GET', 'POST'])
def mapi():
    if request.method == 'GET':
        agg = mongo_utils.mapi("Aktivitetet e tjera p.k.t.")
        return Response(response=json_util.dumps(agg), status=200, mimetype='application/json')
    if request.method == 'POST':
        activity = request.form['activity_name']
        status = request.form['status']
        if status == "Aktiv" or status == "Shuar":
            agg = mongo_utils.mapi_status(activity, status)
        else:
            agg = mongo_utils.mapi(activity)
        return Response(response=json_util.dumps(agg), status=200, mimetype='application/json')
    return Response(response='hello', status=404, mimetype='application/json')
@mod_main.route('/gender-owners', methods=['GET', 'POST'])
def gender_owners():
    if request.method == 'GET':
        docs = mongo_utils.get_total_by_gender()
        total = mongo_utils.get_count_total_gender()
        api = {
        'total': total['result'][0]['all'],
        'doc': docs
        }
        return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
    if request.method == 'POST':
        city = request.form['biz_city_id']
        status = request.form['biz_status']
        if status != 'any' and city == 'any':
            docs_count = mongo_utils.get_count_gen_types_status(status)
            doc = mongo_utils.get_gen_types_by_status(status)
            api = {'total': docs_count['result'][0]['all'], 'doc': doc}
            return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
        elif status == 'any' and city != 'any':
            docs_count = mongo_utils.get_count_gen_types_city(city)
            doc = mongo_utils.get_gen_types_by_city(city)
            api = {'total': docs_count['result'][0]['all'], 'doc': doc}
            return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
        elif status == 'any' and city == 'any':
            docs_count = mongo_utils.get_count_total_gender()
            doc = mongo_utils.get_total_by_gender()
            api = {'total': docs_count['result'][0]['all'], 'doc': doc}
            return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
        else:
            docs_count = mongo_utils.get_count_gen_types_city_status(status, city)
            doc = mongo_utils.get_gen_types_by_city_status(status, city)
            api = {'total': docs_count['result'][0]['all'], 'doc': doc}
            return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
    return 'error'

@mod_main.route('/download', methods=['GET', 'POST'])
def download_page():
    return render_template('downloads.html')

@mod_main.route('/download/<string:doc_type>/<string:year>', methods=['GET'])
def download_doc_year(doc_type, year):
    return send_from_directory(download_folder, "arbk-%s.%s"%(year,doc_type), as_attachment=True)

@mod_main.route('/download/all-zip', methods=['GET'])
def download_doc_all():
    return send_from_directory(download_folder, "arbk-data.zip", as_attachment=True)
