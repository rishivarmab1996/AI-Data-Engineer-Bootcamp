import pandas as pd

employees = pd.read_csv("employees.csv")
departments = pd.read_csv("departments.csv")

merged = pd.merge(employees,
		 departments,
		 on="DepartmentID",
		 how="left")


merged["Bonus"] = merged["Salary"] * 0.10
merged["Bonus"] = merged["Bonus"].astype(int)

def classify(salary):
	if salary < 70000:
		return 'Junior'
	elif  salary <= 85000:
		return 'Mid'
	else:
		return 'Senior'

merged["Level"] = merged["Salary"].apply(classify)

#fetching output based on condition
high_salary = merged [(merged["Salary"] > 75000) & (merged["Experience"] > 5)]
print(high_salary)

#Sorting Values in Descending order
merged = merged.sort_values("Salary",ascending=False)

#Calculate Average Salary By Department
average_salary = merged.groupby("Department")["Salary"].mean()
print(average_salary)
merged.to_csv("employee_report.csv",index=False)


