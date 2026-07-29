import requests
import json

def get_github_data():

    response = requests.get(
        "https://api.github.com"
    )

    return response.json()


data = get_github_data()

with open("github.json","w") as file:
	json.dump(data,file)
