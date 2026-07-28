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
