import pandas as pd

df = pd.read_csv("employees.csv")
df["Age"] = df["Age"].fillna(0,inplace=True)
df["Department"] = df["Department"].fillna("Unknown",inplace=True)
df["Salary"] = df["Salary"].fillna(0,inplace=True)
df["Experience"] = df["Experience"].fillna(0,inplace=True)



