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
