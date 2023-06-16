# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

import pandas as pd

df = pd.read_csv('california_housing_train.csv')
print(df[df['population'] < 500]['median_house_value'].mean())

# Узнать какая максимальная households в зоне минимального значения population

print(df[df['population'] == df['population'].min()]['households'].max())
