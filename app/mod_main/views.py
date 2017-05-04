#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, json, jsonify, Response, request, redirect
from bson import json_util, ObjectId
import re
import datetime
from app import mongo

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

mod_main = Blueprint('main', __name__)

@mod_main.route('/', methods=['GET','POST'])
def index():
	db = mongo.db.reg_businesses
	db.create_index("formatted.slugifiedOwners",1)
	if request.method == 'POST':
		keyword = request.form['search']
		result = db.find({"slugifiedOwners": {"$regex": keyword}}, {'owners':1,'name': 1, 'status': 1, 'arbkUrl': 1})
		return render_template('index.html', result=result)
	return render_template('index.html')

@mod_main.route('/profile/<string:person>')
def profile(person):
	db = mongo.db.reg_businesses
	person_data = db.find({'owners.name' : person})
	return render_template('profile.html', profile_data=person_data)

@mod_main.route('/visualization', methods=['GET','POST'])
def visualization():
	db = mongo.db.reg_businesses
	dbm = mongo.db.municipalities
	if request.method == 'GET':
		top = db.aggregate([{'$sort': {"capital":-1}},{ '$limit' : 10 }])
		komunat = dbm.find()
		return render_template('visualizations.html', top=top, komunat=komunat)
	if request.method == 'POST':
		city = request.form['city_id']
		status = request.form['status']
		if status == 'any' and city == 'any':
			top = db.aggregate([{'$sort': {"capital":-1}},{ '$limit' : 10 }])
			komunat = dbm.find()
			return Response(response=json_util.dumps(top), status=200, mimetype='application/json')
		elif status is not 'any' and city == 'any':
			top = db.aggregate([{'$match': {"status": status}},{'$sort': {"capital":-1}},{ '$limit' : 10 }])
			komunat = dbm.find()
			return Response(response=json_util.dumps(top), status=200, mimetype='application/json')
		elif status == 'any' and city is not 'any':
			top = db.aggregate([{'$match': {"municipality.municipality": city}},{'$sort': {"capital":-1}},{ '$limit' : 10 }])
			komunat = dbm.find()
			return Response(response=json_util.dumps(top), status=200, mimetype='application/json')
		else:
			top = db.aggregate([{'$match': {"status":status ,"municipality.municipality": city}},{'$sort': {"capital":-1}},{ '$limit' : 10 }])
			komunat = dbm.find()
			return Response(response=json_util.dumps(top), status=200, mimetype='application/json')


@mod_main.route('/through-years')
def start_date():
	db = mongo.db.reg_businesses
	api = {}
	y = 1
	for i in range(2002,2018):
		y+=1
		year = "d"+str(y)
		data = db.aggregate([{'$match': {"establishmentDate":{"$gt":datetime.datetime(i,1,1), "$lte":datetime.datetime(i+1,1,1)}}},{'$group': {"_id":"$status", "count":{"$sum":1}}}])
		rr = {}
		if len(data['result']) == 1:
			if data['result'][0]['_id'] == "Aktiv":
				data['result'].append({"_id":"Shuar","count":0})
			else:
				data['result'].append({"_id":"Aktiv","count":0})
		res = {data['result'][0]['_id']:data['result'][0]['count'], data['result'][1]['_id']:data['result'][1]['count']}
		api.update({year:res})
	return Response(response=json_util.dumps(api), status=200, mimetype='application/json')

@mod_main.route('/businesses-type')
def businesses_type():
	db = mongo.db.reg_businesses
	doc = db.aggregate([{'$group': {"_id" : "$type", "total": {"$sum": 1}}},{'$sort': {'total': -1}}])
	api = { 'total': mongo.db.reg_businesses.count(), 'doc': doc }
   	return Response(response=json_util.dumps(api), status=200, mimetype='application/json')

@mod_main.route('/active_inactive', methods=['GET', 'POST'])
def active_inactive():
	db = mongo.db.reg_businesses
	docs = db.aggregate([{'$group': {"_id" : "$status","total": {"$sum": 1}}},{'$sort': {'total': -1}}])
	api = {'total': mongo.db.reg_businesses.count(), 'docs': docs}
   	return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
