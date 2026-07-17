#Define global variables

def get_user_input():
	name = input('whats your name:')
	age = int(input('whats your age:'))
	gender =  input('Whats your gender(Male,Female):')
	goal =  input('Whats your fitness goal:')
	height =  float(input('Whats your height in meters:'))
	weight =  int(input('Whats your weight in KG:'))
	return name,age,gender,goal,height,weight

def validate_input(weight,height):
	if weight <=0 or height <= 0:
		return False
	return True

def calculate_bmi(weight,height):
	return weight / (height ** 2)

def classify_bmi(BMI):
	if BMI <= 18.5:
		return 'Underweight','Increase calorie intake and strength training'
	elif 18.5<=BMI<=24.9:
		return 'Normal','Maintain current lifestyle.'
	elif 25<=BMI<=29.9:
		return 'Overweight', 'Focus on balanced diet and exercise.'
	elif BMI >= 30.0:
		return 'Obese','Focus on weight management and consult a healthcare professional.'
	else:
		return 'Error in Code','Check your values and try again' 
  

def print_report(name,age,gender,goal,height,weight,bmi,category,recommendation):
	return f'------------------------------\nBMI REPORT\n------------------------------\nName: {name}\nAge: {age}\nGender: {gender}\nGoal: {goal}\nHeight: {height}m\nWeight: {weight}kg\nBmi: {bmi:.2f}\ncategory: {category}\nrecommendation: {recommendation}'

def main():
	name,age,gender,goal,height,weight = get_user_input()
	
	if(validate_input(weight,height)) == False:
		print('Invalid Input for Height or Weight')
		exit()
	
	bmi = calculate_bmi(weight,height)
	category,recommendation = classify_bmi(bmi)
	print(print_report(name,age,gender,goal,height,weight,bmi,category,recommendation))	

if __name__ == "__main__":
	main()
