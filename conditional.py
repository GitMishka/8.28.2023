import pandas as pd


df_products = pd.DataFrame({
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'price': [1000, 25, 50, 150]
})

average_price = df_products['price'].mean()
selected_products = df_products[df_products['price'] > average_price]
print(selected_products)
