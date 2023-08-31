import pandas as pd

df_names = pd.DataFrame({
    'full_name': ['John Doe', 'Jane Smith', 'Bill Gates']
})

df_names[['first_name', 'last_name']] = df_names['full_name'].str.split(' ', expand=True)
print(df_names)
