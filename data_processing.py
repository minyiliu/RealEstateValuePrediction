import pandas as pd


def data_processing_by_yr(year):
    data_dir = 'data/'

    for month in range(1,13):
        filename = data_dir + str(year) + '-%02d' % month + '.csv'
        df = pd.read_csv(filename, usecols=['bathstotal', 'beds', 'latitude', 'longitude', 'propclass', 'proptype', 'yearbuilt',
                     'universalsize', 'saleTransDate', 'saleamt'],
            parse_dates=['saleTransDate'])
        df = df[(df.saleamt > 0) & (df.universalsize > 0) & (df.yearbuilt > 0)]
        df.dropna(axis=0, how='any', inplace=True)
        df.loc[:, 'age_year'] = 2016 - df.loc[:, 'yearbuilt']
        if month == 1:
            res = df
        else:
            res = res.append(df)
    return res

