import pandas as pd
df_sales = pd.DataFrame({
    'product_name': ['A', 'B', 'A', 'B', 'C', 'A', 'C'],
    'sales_amount': [10, 15, 5, 20, 10, 10, 15]
})

grouped_sales = df_sales.groupby('product_name').agg(total_sales=('sales_amount', 'sum'))
print(grouped_sales)
