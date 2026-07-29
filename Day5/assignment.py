class User:
	def __init__(self,name,age,weight,height,goal):
		self.name = name
		self.age = age
		self.weight = weight
		self.height = height
		self.goal = goal
		self.category = None
		self.recommendation = None 

	def calculate_bmi(self):
		self.bmi = round(self.weight / (self.height ** 2),2)
		return self.bmi
	
	def classify_bmi(self):
		underweight = 18.5
		normal = 25
		overweight = 30
		if self.bmi < underweight:
			self.category = 'Underweight'
			self.recommendation = 'Increase calorie intake'
		elif self.bmi < normal:
			self.category = 'Normal'
			self.recommendation = 'Maintain lifestyle'
		elif 25 <= self.bmi <= overweight:
			self.category = 'overweight'
			self.recommendation = 'Exercise regularly'
		else:
			self.category = 'obese'
			self.recommendation = 'Focus on weight management'
		return self.category

	def generate_report(self):
		return f'''
			******************
			Fitness Report
			******************
			Name:{self.name}
			Age:{self.age}
			BMI:{self.bmi}
			Category:{self.category}
			Recommendation:{self.recommendation}
			'''


user = [
		User("Rishi",30,76,1.75,"A"),
		User("Meghu",27,99,1.6,"B")
	]
for users in user:
	users.calculate_bmi()
	users.classify_bmi()
	print(users.generate_report())	
	
