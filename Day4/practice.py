import json

'''
users = [
    {
        "name": "Rishi",
        "age": 30,
        "weight": 73
    }
]
'''

#writing into file

#file = open("report.txt","w")
#file.write("Hello Rishi\n")
#file.write("Welcome to Day 4")
#file.close()

#reading the file

#with open("report.txt","r") as file:
#	content = file.read()
#print(content)

#writing into json file
#with open("users.json","w") as file:
#	json.dump(users,file,indent = 4)

#read json file

with open("users.json","r") as file:
	users = json.load(file)
print(users)
