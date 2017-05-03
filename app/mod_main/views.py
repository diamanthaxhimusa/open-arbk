#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, json, jsonify, Response, request, redirect
from bson import json_util, ObjectId
import re
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


@mod_main.route('/visualization')
def visualization():
	return render_template('visualizations.html')


@mod_main.route('/businesses-type')
def businesses_type():
	db = mongo.db.reg_businesses
	doc = db.aggregate([{'$group': {"_id" : "$type", "total": {"$sum": 1}}},{'$sort': {'total': -1}}])
	api = { 'total': mongo.db.reg_businesses.count(), 'doc': doc }
   	return Response(response=json_util.dumps(api), status=200, mimetype='application/json')
