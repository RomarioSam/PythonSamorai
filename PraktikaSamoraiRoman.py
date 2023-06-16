# В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

data = data.rename(columns={'whoAmI' : 'whoAmI_human'})
data['whoAmI_robot'] = 0
for i in range(len(data)):
    if data.loc[i, 'whoAmI_human'] == 'human':
        data.loc[i, 'whoAmI_human'] = 1
    else:
        data.loc[i, 'whoAmI_human'] = 0
        data.loc[i, 'whoAmI_robot'] = 1
print(data)

