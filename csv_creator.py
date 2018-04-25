import json
import csv


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


def create_csv_from_json(filename):
    s = 'accuracy,apn,apnOrig,bathstotal,beds,country,countrySubd,distance,elevation,fips,geoid,lastModified,latitude,line1,line2,locality,longitude,lotSize1,matchCode,obPropId,oneLine,postal1,postal2,postal3,priceperbed,pricepersizeunit,propIndicator,propLandUse,propclass,proptype,pubDate,saleTransDate,saleamt,saledisclosuretype,saledocnum,salerecdate,salesearchdate,saletranstype,universalsize,yearbuilt,propsubtype'

    fieldnames = s.split(',')

    with open(filename, newline='') as f_input, open(filename + '.csv', 'w', newline='') as f_output:
        csv_output = csv.DictWriter(f_output, fieldnames=fieldnames)
        csv_output.writeheader()
        data = json.load(f_input)
        for entry in data['property']:
            leaf_entries = get_leaves(entry)
            d = {}
            for k, v in leaf_entries:
                d[k] = v

            csv_output.writerow(d)


def create_csv_by_year(year):
    data_dir = 'data/'
    for month in range(1, 13):
        filename = data_dir + str(year) + '-%02d'%month
        create_csv_from_json(filename)


create_csv_by_year(2017)
