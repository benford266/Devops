import requests
import json
 
# get response from API
response = requests.get("http://api.open-notify.org/astros.json")
 

# function to print api content to json
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
 

# gets one of the nested keys
peoplelist = response.json()['people']
 
# defining list for just people
justpeople = []
 
# Prints full value of peoples nested key
jprint(peoplelist)
 
# Gets all nested people from this dict and puts just there name in a var
for d in peoplelist:
    person = d['name']
    justpeople.append(person)
 
#print out just users name
print(justpeople)