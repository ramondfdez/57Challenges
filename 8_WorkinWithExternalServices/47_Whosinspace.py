import requests

response = requests.get("http://api.open-notify.org/astros.json")

json = response.json()

print("Name                 |   Craft")
print("---------------------|--------")
for i in json['people']:
    name = i["name"]
    craft = i["craft"]
    print('{name:20} | {craft:20}'.format(name=name, craft = craft))