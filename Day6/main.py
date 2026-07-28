from models.user import User
from utils.bmi import classify_bmi
from utils.report import generate_report

users = [User("Rishi",30,76,1.75,"A"),User("Meghu",27,99,1.6,"B")]

for user in users:
	user.calculate_bmi()
	classify_bmi(user)
	print(generate_report(user))
