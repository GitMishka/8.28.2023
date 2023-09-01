import pandas as pd


df_weather = pd.DataFrame({
    'day': [1, 2, 3, 4, 5],
    'temperature': [22, None, 24, None, 26]
})

df_weather['temperature'] = df_weather['temperature'].interpolate()
print(df_weather)
