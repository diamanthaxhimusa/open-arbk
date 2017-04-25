#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, json, jsonify, Response
from bson import json_util, ObjectId

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

mod_main = Blueprint('main', __name__)

from app import mongo

@mod_main.route('/')
def index():
	return render_template('index.html')
	# doc = mongo.db.businesses.aggregate([{ '$match': { "formatted.registrationNum": 70002534 }}])
	# return Response(response=json_util.dumps(docs[0]['formatted']), status=200, mimetype='application/json')

# Script for slugifying owners
@mod_main.route('/slugify_owners')
def slugify_owners():

	# Getting all documnets from DB
	docs = mongo.db.businesses.find()

	# Looping through each doc
	for doc in docs:
		# Looping in owner array of 'formatted' JSON in docs
		for owner in doc['formatted']['owners']:
			# Slugifying each owner string and then updating new array in 'formatted' docs with slugified strings
			slugified_owner_string = owner.lower()
			if "ë" in owner or "Ë" in owner:
				slugified_owner_string = owner.lower().replace("ë", "e")
			elif "ç" in owner or "Ç" in owner:
				slugified_owner_string = owner.lower().replace("ç", "c")
			else:
				chars = ['?', '/', '\\', "*"]
				for ch in chars:
					if ch in owner:
						slugified_owner_string = owner.lower().replace(ch, "")

			mongo.db.businesses.update({"_id": ObjectId(doc['_id'])}, { '$push': {"formatted.slugified_owners": slugified_owner_string }})
	return render_template('script_result.html')
