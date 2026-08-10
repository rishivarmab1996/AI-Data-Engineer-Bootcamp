import pandas as pd


df = pd.read_csv("employees.csv")
average_salary = df["Salary"].mean()
df["Age"] = df["Age"].fillna(0)
df["Salary"] = df["Salary"].fillna(average_salary)
df["Department"] = df["Department"].fillna("Unknown")
df["Experience"] = df["Experience"].fillna(0)
#print(df)
#print(df.dtypes)
df = df.drop_duplicates()
df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(int)
#print(df)
#print(df.dtypes)

print(df.groupby("Department")["Salary"].mean())

df.to_csv("cleaned_employees.csv",index=False)

#print(df.info())
#print(df.describe())
#print(df.isnull().sum())
