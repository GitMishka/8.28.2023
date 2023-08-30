import pandas as pd

def generate_profile_report(df):
    profile = {
        "Missing Values": df.isnull().sum(),
        "Mean": df.mean(),
        "Median": df.median(),
        "Standard Deviation": df.std()
    }
    for column in df.columns:
        if df[column].dtype == 'object':  # Checks if column type is non-numeric
            profile[f"{column} Unique Count"] = df[column].nunique()

    return profile

df = pd.DataFrame({
    'A': [1, 2, 3, None],
    'B': [4, 5, 6, 7],
    'C': [8, 9, 10, None],
    'D': ['a', 'b', 'a', 'c']
})

report = generate_profile_report(df)
print(report)
