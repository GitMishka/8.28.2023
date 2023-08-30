import pandas as pd

df1 = pd.DataFrame({
    'user_id': [1, 2, 3],
    'username': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'user_id': [2, 3, 4],
    'email': ['bob@email.com', 'charlie@email.com', 'david@email.com']
})

merged_df = pd.merge(df1, df2, on='user_id', how='outer')
print(merged_df)
