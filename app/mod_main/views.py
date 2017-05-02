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
