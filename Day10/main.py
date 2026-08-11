import pandas as pd
from pathlib import Path

def extract_data():
	employees = pd.read_csv("employees.csv")
	departments = pd.read_csv("departments.csv")
	return employees,departments

def transform_data(employees,departments):
	df = pd.merge(employees,departments, on="DepartmentID",how="left")
	df = df.drop_duplicates()
	df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
	df["Department"] = df["Department"].fillna("Unknown")
	df["Name"] = df["Name"].fillna("Unknown")
	df["Age"] = df["Age"].fillna(0)
	df["Bonus"] = df["Salary"] * 0.1
	df["Level"] = df["Salary"].apply(classify)
	df2 = df.groupby("Department")["Salary"].mean()	
	return df,df2

def load_data(df,df2):
	output_dir = Path("output_dir")
	output_dir.mkdir(exist_ok=True)
	df.to_csv(output_dir/"employee_report.csv",index=False)
	df2.to_csv(output_dir/"department_summary.csv",index=False)

def classify(salary):
	if salary < 70000:
		return 'Junior'
	elif salary <= 85000:
		return 'Mid'
	else:
		return 'Senior'

def main():
	employees, departments = extract_data()
	#print(employees,departments)
	df,df2 = transform_data(employees,departments)
	#print(df)
	load_data(df,df2)

if __name__=="__main__":
	main()
