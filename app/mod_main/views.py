#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, json, jsonify, Response
from bson import json_util, ObjectId
from slugify import slugify

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

mod_main = Blueprint('main', __name__)

from app import mongo

@mod_main.route('/')
def index():
	return render_template('index.html')

@mod_main.route('/slugify_owners')
def slugify_owners():
	# slug test
	# city1 = "Ritë"
	# slugied = slugify(city1)

	docs = mongo.db.businesses.find().limit(100)
	# json_object = json.load(docs)

	for doc in docs:
		for owner in doc['formatted']['owners']:
			print slugify(owner).replace("-", " ")


	# for doc 																																																																																			# return all_owners
	# doc = mongo.db.businesses.aggregate([{ '$match': { "formatted.registrationNum": 70002534 }}])
	return "Success Slugified owners, see your server activity in terminal for results"
	# return Response(response=json_util.dumps(docs), status=200, mimetype='application/json')
