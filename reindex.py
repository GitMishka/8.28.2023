import pandas as pd

df_items = pd.DataFrame({
    'items': ['item1', 'item2', 'item3'],
    'quantity': [10, 15, 20]
})

new_index = ['item1', 'item2', 'item3', 'item4']
df_items = df_items.set_index('items').reindex(new_index).fillna(0).reset_index()
print(df_items)
