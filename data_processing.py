import pandas as pd

df = pd.read_csv('data/2016-01.csv')
print(df.shape)
df = df[df.saleamt != 0]
print(df.shape)