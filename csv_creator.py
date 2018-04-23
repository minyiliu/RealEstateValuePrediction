import json
import csv

s = 'accuracy,apn,apnOrig,bathstotal,beds,country,countrySubd,distance,elevation,fips,geoid,lastModified,latitude,line1,line2,locality,longitude,lotSize1,matchCode,obPropId,oneLine,postal1,postal2,postal3,priceperbed,pricepersizeunit,propIndicator,propLandUse,propclass,proptype,pubDate,saleTransDate,saleamt,saledisclosuretype,saledocnum,salerecdate,salesearchdate,saletranstype,universalsize,yearbuilt'

fieldnames = s.split(',')

def get_leaves(item, key=None):
    if isinstance(item, dict):
        leaves = []
        for i in item.keys():
            leaves.extend(get_leaves(item[i], i))
        return leaves
    elif isinstance(item, list):
        leaves = []
        for i in item:
            leaves.extend(get_leaves(i, key))
        return leaves
    else:
        return [(key, item)]

month = '2016-06'

with open(month, newline='') as f_input, open(month + '.csv', 'w', newline='') as f_output:
    csv_output = csv.DictWriter(f_output, fieldnames=fieldnames)
    csv_output.writeheader()
    data = json.load(f_input)
    for entry in data['property']:
        leaf_entries = get_leaves(entry)
        d = {}
        for k, v in leaf_entries:
            d[k] = v

        csv_output.writerow(d)
