import pandas as pd

"""Создание Series из списка"""

data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

"""Создание Series с явным указанием индексов"""

index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)
print(series)


"""Доступ по меткам индекса"""

series.loc['a']

"""Доступ по числовому индексу"""

series.iloc[1]

"""Загрузим данные с сайта https://www.kaggle.com/datasets"""

df = pd.read_csv("C:\\Users\\marat\\Downloads\\archive\\Stats survey.csv")
df.info()
print(df)