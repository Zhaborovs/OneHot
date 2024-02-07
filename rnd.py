import pandas as pd
import random

# Ваш исходный код
random.seed(42)  # Чтобы результат был воспроизводимым
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one-hot
one_hot_data = pd.get_dummies(data['whoAmI'], prefix='whoAmI')

# Объединение исходного DataFrame с one-hot представлением
data_one_hot = pd.concat([data, one_hot_data], axis=1)

# Вывод результата
print(data_one_hot.head())

