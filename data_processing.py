import pandas as pd

for month in range(1,13):
    filename = 'data/2016-%02d.csv'%month
    df = pd.read_csv(filename, usecols=['bathstotal', 'beds', 'latitude', 'longitude', 'propclass', 'proptype', 'yearbuilt',
                 'universalsize', 'saleTransDate', 'saleamt'],
        parse_dates=['saleTransDate'])
    # df = df[['bathstotal', 'beds', 'latitude', 'longitude', 'propclass', 'proptype', 'yearbuilt', 'propLandUse',
    #              'universalsize', 'saleTransDate', 'saleamt']]
    df = df[(df.saleamt > 0) & (df.universalsize > 0) & (df.yearbuilt > 0)]
    df.dropna(axis=0, how='any', inplace=True)
    if month == 1:
        res = df
    else:
        res = res.append(df)

res.loc[:, 'age_year'] = 2016-df.loc[:, 'yearbuilt']

print(res.dtypes)

type = res.loc[:, ['propclass', 'proptype']]
