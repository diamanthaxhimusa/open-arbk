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
        search_person = request.form['person']
        municipality = request.form['municipality']
        if keyword == '':
            result = mongo_utils.get_limit_businesses(100)
        elif search_person == 'owner':
            if municipality == 'any':
                result = mongo_utils.get_people("slugifiedOwners", keyword)
            else:
                result = mongo_utils.get_people_by_municipality("slugifiedOwners", keyword, municipality)
        elif search_person == 'auth':
            if municipality == 'any':
                result = mongo_utils.get_people("slugifiedAuthorized", keyword)
            else:
                result = mongo_utils.get_people_by_municipality("slugifiedAuthorized", keyword, municipality)
        else:
            result = mongo_utils.get_by_owners_authorized(keyword)
    return render_template('index.html', result=result, municipalities=municipalities)


@mod_main.route('/search/<string:status>/<string:person>')
def profile(status, person):
    person_to_lower = person.lower()
    if status == 'owner':
        person_data = mongo_utils.get_profiles("slugifiedOwners", person_to_lower)
    else:
        person_data = mongo_utils.get_profiles("slugifiedAuthorized", person_to_lower)
    return render_template('search.html', profile_data=person_data, status=status, person=person)


@mod_main.route('/visualization', methods=['GET', 'POST'])
def visualization():
    komunat = mongo_utils.get_municipalities()
    if request.method == 'GET':
        top = mongo_utils.get_top_ten_by_capital()
        return render_template('visualizations.html', top=top, komunat=komunat)
    if request.method == 'POST':
        city = request.form['city_id']
        status = request.form['status']
        if status == 'any' and city == 'any':
            top = mongo_utils.get_top_ten_by_capital()
            return Response(response=json_util.dumps(top), status=200, mimetype='application/json')
        elif status is not 'any' and city == 'any':
            top = mongo_utils.get_top_ten_capital_by_status(status)
            return Response(response=json_util.dumps(top), status=200, mimetype='application/json')
        elif status == 'any' and city is not 'any':
            top = mongo_utils.get_top_ten_capital_by_city(city)
            return Response(response=json_util.dumps(top), status=200, mimetype='application/json')
        else:
            top = mongo_utils.get_top_ten_capital_by_city_status(status, city)
            return Response(response=json_util.dumps(top), status=200, mimetype='application/json')


@mod_main.route('/through-years')
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


@mod_main.route('/businesses-type')
def businesses_type():
    doc = mongo_utils.business_type_count()
    docs_count = mongo_utils.docs_count()
    api = {'total': docs_count, 'doc': doc}
    return Response(response=json_util.dumps(api), status=200, mimetype='application/json')


def set_activity(given_code):
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


@mod_main.route('/top_activities')
def activities():
    activity_items = []
    businesses_activities = mongo_utils.get_most_used_activities()
    for activity in businesses_activities['result']:
        activity_set = set_activity(activity['_id'])
        if len(activity_set) != 0:
            activity_items.append({
                "total_businesses": activity['totali'],
                "details": activity_set
            })
    activities_api = {'activities': activity_items}
    return Response(response=json_util.dumps(activities_api), status=200, mimetype='application/json')


@mod_main.route('/active_inactive', methods=['GET', 'POST'])
def active_inactive():
    docs = mongo_utils.get_total_by_status()
    api = {
            'total': mongo_utils.docs_count(),
            'docs': docs
    }
    return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
