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
