import pandas as pd
df_dates = pd.DataFrame({
    'date': ['2022-01-15', '2022-05-20', '2023-07-10']
})

df_dates['date'] = pd.to_datetime(df_dates['date'])
df_dates['month'] = df_dates['date'].dt.month
df_dates['year'] = df_dates['date'].dt.year
print(df_dates)


