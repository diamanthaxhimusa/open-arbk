#! /usr/bin/env bash

source ./venv/bin/activate
python document-prepare.py
echo `mongoexport --db arbk --collection reg_businesses --out app/static/downloads/arbk-data.json`
