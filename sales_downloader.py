#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import csv
import datetime as dt

# curl -X GET --header 'Accept: application/json' --header 'apikey: 9d078487e223b1c4d54c3f3a3f628803' 'https://search.onboard-apis.com/propertyapi/v1.0.0/sale/snapshot?geoid=CO06075&startsalesearchdate=2016-07-01&endsalesearchdate=2016-09-30'

def download_data_by_yr(year, geoid='CO06075'):
    with open('obDevId') as f:
        readfile = f.read()
    apikey = readfile.strip()

    headers = {}
    headers['apikey'] = apikey
    headers['Accept'] = "application/json"

    hierachy = {}
    resource = "sale"
    package = "snapshot"
    hierachy['resource'] = resource
    hierachy['package'] = package

    endpoint = "https://search.onboard-apis.com/propertyapi/v1.0.0/{resource}/{package}".format(**hierachy)

    payload = {}
    payload['geoid'] = geoid
    payload['pagesize'] = 10000

    data_dir = 'data/'

    for month in range(1, 13):
        startsalesearchdate = str(dt.date(year, month, 1))
        if month != 12:
            endsalesearchdate = str(dt.date(year, month + 1, 1) - dt.timedelta(days=1))
        else:
            endsalesearchdate = str(dt.date(year, month, 31))
        payload['startsalesearchdate'] = startsalesearchdate
        payload['endsalesearchdate'] = endsalesearchdate

        r = requests.get(endpoint, params=payload, headers=headers)

        text_file = open(data_dir + startsalesearchdate[:-3], "w")
        text_file.write(r.text)
        text_file.close()

download_data_by_yr(2017)
