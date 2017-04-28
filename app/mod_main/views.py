#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, json, jsonify, Response
from bson import json_util, ObjectId
import re

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


def slug_data(slug_string):
	# Slugifying each string and then updating new elements in 'formatted' docs with slugified strings
	slugified_string = slug_string
	if "ë" in slug_string or "Ë" in slug_string:
		slugified_string = slugified_string.lower().replace("ë", "e")
	elif "ç" in slug_string or "Ç" in slug_string:
		slugified_string = slugified_string.lower().replace("ç", "c")
	slugified_string = re.sub(r'[,|?|$|/|\|"]',r'', slugified_string)
	return slugified_string.lower()


def set_muni(given_city_bus):
	municipalities = mongo.db.municipalities.find()
	cities = {}
	found = False
	for place in municipalities:
		for city in place:
			if city != '_id':
				for village in place[city]:
					if village == given_city_bus:
						found = True
						cities = {
							"municipality": city,
							"place": given_city_bus
						}
	if found:
		return cities
	else:
		cities = {
			"municipality": "Unknown",
			"place": given_city_bus
		}
		return cities


# Script for slugifying owners
@mod_main.route('/slugify_owners')
def slugify_owners():
	# Getting all documnets from DB
	docs = mongo.db.businesses.find()
	# Looping through each doc
	for doc in docs:
		print doc['_id']
		Looping in owner array of 'formatted' JSON in docs
		for owner in doc['formatted']['owners']:
			slugified_owner_string = slug_data(owner)
			mongo.db.businesses.update({"_id": ObjectId(doc['_id'])}, { '$push': {"formatted.slugified_owners": slugified_owner_string}})
			gender_owner = gender_person(owner)
			mongo.db.businesses.update({"_id": ObjectId(doc['_id'])}, { '$push': {"formatted.gendered_owners": gender_owner}})

		slugified_company_string = re.sub(r'[,|?|$|/|\|"]',r'', doc['formatted']['name'])
		mongo.db.businesses.update({"_id": ObjectId(doc['_id'])}, { '$set': {"formatted.name": slugified_company_string }})

		for authorized in doc['formatted']['authorized']:
			slugified_authorized_string = slug_data(authorized)
			mongo.db.businesses.update({"_id": ObjectId(doc['_id'])}, { '$push': {"formatted.slugified_authorized": slugified_authorized_string }})

		try:
			city = set_muni(doc['formatted']['municipality'])
			mongo.db.businesses.update({"_id": ObjectId(doc['_id'])}, { '$set': {"formatted.municipality": city }})
		except Exception as e:
			continue
	return render_template('script_result.html')
