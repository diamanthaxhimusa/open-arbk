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
db.municipalities.drop()
with open("data-importer/komunat.json","r") as data:
    municipalities = json.load(data)
    for municipality in municipalities:
        place = []
        for muni_place in municipalities[municipality]:
            place.append(muni_place)
        db.municipalities.insert({"municipality":municipality, "districts":place, 'slug':slugify(municipality) })
