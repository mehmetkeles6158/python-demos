import requests

response = requests.get("http://api.open-notify.org/astros.json")

json1 = response.json()

print(json1)


for person in json1['people']:
    print(person['name'])
