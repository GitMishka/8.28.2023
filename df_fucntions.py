import pandas as pd

df_prices = pd.DataFrame({
    'product': ['Apple', 'Banana', 'Cherry'],
    'price': [1.2, 0.5, 2.5]
})

df_prices['discounted_price'] = df_prices['price'].apply(lambda x: x * 0.9)
print(df_prices)
