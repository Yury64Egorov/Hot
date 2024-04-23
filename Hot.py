import random
from collections import Counter
import pandas

# Создаем DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = {'whoAmI': lst}

# Считаем уникальные значения в столбце 'whoAmI'
counter = Counter(data['whoAmI'])
categories = list(counter.keys())

# Создаем one hot кодирование
one_hot_encoding = {category: [1 if val == category else 0 for val in data['whoAmI']] for category in categories}

# Создаем DataFrame для хранения one hot кодированных значений
one_hot_data = {f'{key}_{i}': value for key, value in one_hot_encoding.items() for i in range(1, len(data['whoAmI']) + 1)}
one_hot_df = pandas.DataFrame(one_hot_data)

print(one_hot_df.head())
