import pandas as pd

df_grades = pd.DataFrame({
    'student': ['A', 'B', 'C', 'D', 'E'],
    'grade': ['B', 'A', 'C', 'B', 'A']
})

grade_category = pd.CategoricalDtype(categories=['A', 'B', 'C'], ordered=True)
df_grades['grade'] = df_grades['grade'].astype(grade_category)
print(df_grades['grade'])
