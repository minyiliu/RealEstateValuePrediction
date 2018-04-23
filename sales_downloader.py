#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import csv

# curl -X GET --header 'Accept: application/json' --header 'apikey: 9d078487e223b1c4d54c3f3a3f628803' 'https://search.onboard-apis.com/propertyapi/v1.0.0/sale/snapshot?geoid=CO06075&startsalesearchdate=2016-07-01&endsalesearchdate=2016-09-30'

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
# cityname = "San Francisco"
geoid = 'CO06075'
month = '2016-06'
startsalesearchdate = '{month}-01'.format(month=month)
endsalesearchdate = '{month}-30'.format(month=month)
payload['geoid'] = geoid
payload['startsalesearchdate'] = startsalesearchdate
payload['endsalesearchdate'] = endsalesearchdate
payload['pagesize'] = 10000

r = requests.get(endpoint, params=payload, headers = headers)

text_file = open(month, "w")
text_file.write(r.text)
text_file.close()
