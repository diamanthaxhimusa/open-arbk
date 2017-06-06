#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import re, json, unidecode
from slugify import slugify
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

client = MongoClient("mongodb://localhost:27017")
db = client['arbk']
db.activities.drop()
with open("data-importer/activities.json","r") as data:
    activities = json.load(data)
    for activity in activities['activities']:
        db.activities.insert(activity)
