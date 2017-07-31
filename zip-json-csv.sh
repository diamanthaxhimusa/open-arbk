#! /usr/bin/env bash

echo `cd app/static/downloads/; zip -r arbk-data-json.zip arbk-data\(\sq\)\.json`
echo `cd app/static/downloads/; zip -r arbk-data-csv.zip arbk-data\(\sq\)\.csv`
echo `cd app/static/downloads/; zip -r arbk-data-json.zip arbk-data\(\en\)\.json`
echo `cd app/static/downloads/; zip -r arbk-data-csv.zip arbk-data\(\en\)\.csv`
