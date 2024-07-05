import pandas as pd
# https://www.kaggle.com/datasets

df = pd.read_csv('Free-to-play games.csv')
print(df.head())
print(df.describe())

df = pd.read_csv('dz.csv')
print(df.head())
print(df.describe())

