def calculate_bmi(weight,height):
    if weight <= 0 or height <=0:
        exit()
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi <= 18.5:
        return {
            'category':'Underweight',
            'recommendation':'Increase calorie intake and strength training'
               }
    elif 18.5<=bmi<=24.9:
        return {
            'category':'Normal',
            'recommendation':'Maintain current lifestyle.'
               }
    elif 25<=bmi<=29.9:
        return {
            'category':'Overweight', 
            'recommendation':'Focus on balanced diet and exercise.'
               }
    elif bmi >= 30.0:
        return {
            'category':'Obese',
            'recommendation':'Focus on weight management and consult a healthcare professional.'
               }
    else:
        return 'Error in Code *** Check your values and try again'

def usersRankedByBMI(users):
    ranks = sorted(users, key=lambda x:x["bmi"], reverse=True)
    sortedList = ''
    for rank in ranks:
        sortedList += f'{rank["name"]} - {rank["bmi"]}\n'
    return sortedList
                
    
def print_report(users,highest_bmi,lowest_bmi,average_bmi,users_bmi_above_25):
#	user = "\n".join(usr["name"] for usr in users)
    above_25_names = "\n".join(users_bmi_above_25)	
    report = ''
    for user in users:
        report += (
                f'Name:{user["name"]}\n'
                f'BMI:{user["bmi"]}\n'
                f'Category:{user["category"]}\n'
                f'Recommendation:{user["recommendation"]}\n\n'
               )
        #report += "BMI:"+str(user["bmi"])+'\n'
        #report += "Category:"+str(user["category"])+'\n\n' 
    return f'------------------------\nFITNESS REPORT\n------------------------\n{report}\nAverage_BMI: {average_bmi}\nHighest_BMI:{highest_bmi}\nLowest_BMI:{lowest_bmi}\nUsers Above BMI 25\n--------------------\n{above_25_names}\n'	

def main():
    import json
    from pathlib import Path
    
    pathOfUsersFile = Path("users.json")
    users = []
    moreUsers = ''
    if pathOfUsersFile.exists():
        with open("users.json","r") as file:
            users = json.load(file)
        
        while True:
            moreUsers = input('Do you want to add users(Y/N):')
            if moreUsers == 'Y':
                try:
                    users.append(
                    {
                        "name":str(input('Whats your Name:')),
                        "age":int(input('Whats your age:')),
                        "height":float(input('Whats your height in meters:')),
                        "weight":int(input('Whats your weight in KG:')),
                        "goal":str(input('Whats your goal:'))
                    }
                    )
                except ValueError:
                    print("Enter valid values for Name, Age, Height, Weight and Goal")
                with open("users.json","w") as file:
                    json.dump(users,file,indent=4)
            elif moreUsers == 'N':
                break
            break
    else:
        while True:
            moreUsers = input('Do you want to add users(Y/N/QUIT):')
            if moreUsers == 'Y':
                users.append(
                {
                    "name":str(input('Whats your Name:')),
                    "age":int(input('Whats your age:')),
                    "height":float(input('Whats your height in meters:')),
                    "weight":int(input('Whats your weight in KG:')),
                    "goal":str(input('Whats your goal:'))
                }
                )
                with open("users.json","w") as file:
                    json.dump(users,file,indent=4)
            elif moreUsers == 'N':
                with open("users.json","r") as file:
                    users = json.load(file)
                break
            else:
                break
            
   
    for user in users:
        bmi = calculate_bmi(user["weight"],user["height"])
        user["bmi"] = round(bmi,2)
        #bmilist.append(round(bmi,2))
    
    for user in users:
        classification = classify_bmi(user["bmi"])
        user['category'] = classification['category']
        user['recommendation'] = classification['recommendation']
    
    highest_bmi = max(user['bmi'] for user in users)
    lowest_bmi = min(user['bmi'] for user in users)
    average_bmi = sum(user['bmi'] for user in users) / len(users)
    
    users_bmi_above_25 = []
    for user in users:
        if user["bmi"] >= 25:
            users_bmi_above_25.append(user["name"])
    
    report = print_report(users,highest_bmi,lowest_bmi,average_bmi,users_bmi_above_25)
    with open("report.txt","w") as file:
        file.write(report)
    
    #print(usersRankedByBMI(users))
    
if __name__ == "__main__":
    main()
