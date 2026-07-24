def print_report(users):
	user = [] 
	for usr in users:
		user.append(usr)
	return user

def main():
	users = [
			{
				"name":"Rishi",
				"age" : "30"
			},
			{
				"name":"Austin",
				"age" : "40"
			}
		]
	for user in users:
		print("Name:",user["name"])
		print("Age:",user["age"])
if __name__ == "__main__":
	main()
