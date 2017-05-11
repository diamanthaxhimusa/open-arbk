#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, Response, request
from app import mongo_utils
from bson import json_util
import sys
reload(sys)

mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET', 'POST'])
def index():
    mongo_utils.index_create()
    municipalities = mongo_utils.get_municipalities()
    result = mongo_utils.get_limit_businesses(100)
    if request.method == 'POST':
        search_keyword = request.form['search']
        keyword = search_keyword.lower()
        status = request.form['person']
        city = request.form['municipality']
        if len(keyword) <= 2:
            result = mongo_utils.get_limit_businesses(100)
        elif status == 'any' and city == 'any':
            result = mongo_utils.get_by_owners_authorized(keyword)
        elif status != 'any' and city == 'any':
            if status == 'owner':
                result = mongo_utils.get_people("slugifiedOwners", keyword)
            else:
                result = mongo_utils.get_people("slugifiedAuthorized", keyword)
        elif status != 'any' and city != 'any':
            if status == 'owner':
                result = mongo_utils.get_people_by_municipality("slugifiedOwners", keyword, city)
            else:
                result = mongo_utils.get_people_by_municipality("slugifiedAuthorized", keyword, city)
        elif status == 'any' and city != 'any':
            result = mongo_utils.get_by_owners_authorized_municipality(keyword, city)
        else:
            result = mongo_utils.get_limit_businesses(100)
    return render_template('index.html', result=result, municipalities=municipalities)


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
        print city
        print status
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
        res = {
                data['result'][0]['_id']: data['result'][0]['count'],
                data['result'][1]['_id']: data['result'][1]['count']
        }
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


@mod_main.route('/top_activities', methods=['GET', 'POST'])
def activities():
    if request.method == 'GET':
        all_businesses_activities = mongo_utils.get_most_used_activities()
        result = prepare_activity_api(all_businesses_activities)
        return Response(response=json_util.dumps(result), status=200, mimetype='application/json')
    elif request.method == 'POST':
        city = request.form['city']
        status = request.form['status']
        if status == 'any' and city == 'any':
            print "first"
            business_activities = mongo_utils.get_most_used_activities()
            result = prepare_activity_api(business_activities)
            return Response(response=json_util.dumps(result), status=200, mimetype='application/json')
        elif status != 'any' and city == 'any':
            print 'second'
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


@mod_main.route('/active_inactive', methods=['GET', 'POST'])
def active_inactive():
    docs = mongo_utils.get_total_by_status()
    api = {
            'total': mongo_utils.docs_count(),
            'docs': docs
    }
    return Response(response=json_util.dumps(api), status=200, mimetype='application/json')


@mod_main.route('/activitymap', methods=['GET', 'POST'])
def activity_map():
    activities = mongo_utils.get_activities()
    return render_template('activity-map.html', activities=activities)

@mod_main.route('/mapi', methods=['GET', 'POST'])
def mapi():
    if request.method == 'POST':
        activity = request.form['activity_name']
        agg = mongo_utils.mapi(activity)
        return Response(response=json_util.dumps(agg), status=200, mimetype='application/json')
    return Response(response='hello', status=404, mimetype='application/json')
@mod_main.route('/gender_owners', methods=['GET', 'POST'])
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
