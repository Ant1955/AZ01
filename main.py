import pandas as pd

# https://www.kaggle.com/datasets
# загрузка данных
df = pd.read_csv('Free-to-play games.csv')
# что есть в таблице
print(df.describe())
print(df.info())
# первые 5 строк
print(df.head())

df = pd.read_csv('dz.csv')  # как требует задание

# что есть в таблице
print(df.describe())
# первые 5 строк
print(df.head())
# сортировка по столбцу
group = df.groupby('City')['Salary'].mean()
# вывод результата
print(group)