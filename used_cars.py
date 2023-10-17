import pandas as pd
import numpy

data = pd.read_csv(r'D:\Uzair\Programming\Python\used_cars.csv', low_memory=False)

print(data.head())

def convert_price(price_str):
    parts = price_str.split()
    if len(parts) == 3:
        amount = float(parts[1])
        unit = parts[2]
        if unit == 'lacs':
            return amount * 100000
        elif unit == 'crore':
            return amount * 10000000
    return None


data['Price_Updated'] = data['Price'].apply(convert_price)

print('\n\n\n')
print(data.head())

data['Price_Updated'] = data['Price_Updated'].fillna('Call')

data.to_csv(r'D:\Uzair\Programming\Python\Data Science\updated_used_cars1.csv', index=False)