import pandas as pd

df_scores = pd.DataFrame({
    'student': ['A', 'B', 'C', 'D', 'E'],
    'score': [85, 90, 78, 88, 92]
})

print(df_scores['score'].describe())
