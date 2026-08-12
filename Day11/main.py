import logging
import pandas as pd
from pathlib import Path

logging.basicConfig(
	filename="etl.log",
	filemode="w",
	level=logging.INFO,
	format="%(asctime)s | %(levelname)s | %(message)s"
	)

logging.info("ETL pipeline started....")

def load_csv(csvFile):
	try:
		csv_file = pd.read_csv(csvFile)
		logging.info(f"data extracted successfully from {csvFile} | rows = {len(csv_file)}")
		return csv_file
	except FileNotFoundError:
		logging.error(f"{csvFile} not found")
		return None

def classify(salary):
	if salary < 70000:
		return 'Junior'
	elif salary <=85000:
		return 'Mid'
	else:
		return 'Senior'

def extract_data():
	logging.info("Starting Data Extraction...")
	employees = load_csv("employees.csv")
	departments = load_csv("departments.csv")	
	return employees,departments

def transform_data(employees,departments):
	logging.info("Starting data transformation...")
	try:
		df = pd.merge(employees,departments,on="DepartmentID",how="left")
		logging.info(f"Data Merged Successfully | rows={len(df)}")
		df = df.drop_duplicates()
		logging.info("Duplicate records removed")
		df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
		df["Department"] = df["Department"].fillna("Unknown")
		df["Name"] = df["Name"].fillna("Unknown")
		df["Age"] = df["Age"].fillna(0)
		logging.info("missing values handled")
		df["Bonus"] = df["Salary"] * 0.1
		logging.info("Employee Bonus Calculated")
		df["Level"] = df["Salary"].apply(classify)
		logging.info("Employee levels created")
		df2 = df.groupby("Department")["Salary"].mean()
		logging.info("Department summary created")
		logging.info("Data Transformation Completed")	
		return df,df2
	except KeyError as e:
		logging.error(f"Transformation Failed. Missing Column {e}")
		return None 


def load_data(df,df2):
	try:
		output_dir = Path("output_dir")
		output_dir.mkdir(exist_ok=True)
		df.to_csv(output_dir/"employee_report.csv",index=False)
		df2.to_csv(output_dir/"department_summary.csv",index=False)
		logging.info(f"Data loaded successfully into {output_dir} directory")
	except PermissionError:
		logging.error(f"Insufficient permissions to write to {output_dir}")
		return None
def main():
	employees,departments = extract_data()
	if employees is None or departments is None:
		logging.error("Data Extraction Failed. Stopping ETL process...")
		return
	result = transform_data(employees,departments)
	if result is None:
		logging.error("Data Transformation Failed. Stopping ETL...")
		return
	df,df2 = result
	load_data(df,df2)
	logging.info("ETL pipeline completed successfully...")

if __name__ == "__main__":
	main()
	
