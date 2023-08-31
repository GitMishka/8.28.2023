import pandas as pd

df_students = pd.DataFrame({
    'student_id': [1, 2, 3, 2, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'Bob', 'David']
})

df_students.drop_duplicates(subset='student_id', inplace=True)
print(df_students)
