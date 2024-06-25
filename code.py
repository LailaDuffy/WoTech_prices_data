import pandas as pd

data = pd.read_csv('/content/prices.txt', header=None, delimiter = ' ')
data.columns = ['Price, EUR']

df = pd.DataFrame(data)
filtered_df = df[df.apply(lambda row: any(any(char.isdigit() for char in str(element)) for element in row), axis=1)] # filter out NaN values

total_price = (pd.to_numeric(filtered_df['Price, EUR'])).sum() # make sure numbers are numeric values
print(f'The total price off all items is {total_price}EUR')

items_count = filtered_df['Price, EUR'].count()
print(f'There are {items_count} items on the list.')
