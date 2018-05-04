import pandas as pd


def data_processing_by_yr(year):
    data_dir = 'data/'

    for month in range(1,13):
        filename = data_dir + str(year) + '-%02d' % month + '.csv'
        df = pd.read_csv(filename, usecols=['bathstotal', 'beds', 'latitude', 'longitude', 'postal1', 'propclass', 'yearbuilt',
                     'universalsize', 'saleTransDate', 'saleamt'],
            parse_dates=['saleTransDate'])
        df = df[(df.saleamt > 0) & (df.universalsize > 0) & (df.yearbuilt > 0)]
        df.dropna(axis=0, how='any', inplace=True)
        df.loc[:, 'age_year'] = year - df.loc[:, 'yearbuilt']
        df = df[df.propclass.isin(['"Duplex, Triplex, Quadplex)"', 'Apartment', 'Condominium (residential)',
                                   'Single Family Residence / Townhouse'])]
        df['price'] = df['saleamt'] / df['universalsize']

        df = df.join(pd.get_dummies(df['propclass']))
        df.rename(index=str, columns={'"Duplex, Triplex, Quadplex)"': 'duplex', 'Condominium (residential)': 'condo',
                                      'Single Family Residence / Townhouse': 'townhouse', 'postal1': 'zipcode'}, inplace=True)

        df.drop(['propclass', 'saleTransDate', 'saleamt', 'yearbuilt'], axis=1)
        df.reset_index(drop=True, inplace=True)

        if month == 1:
            res = df
        else:
            res = res.append(df)
    return res

df=data_processing_by_yr(2016)
df.to_csv('cleaned_data.csv')
