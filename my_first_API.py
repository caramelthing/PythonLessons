import requests 

response = requests.get("https://randomfox.ca/floof")
print("Response code from the https://randomfox.ca/floof API: " + str(response.status_code))
print(response.text)
print("...................")
print(response.json())
#now will convert the pulled information into a python dictionary then I can work with it - mwhahaha

#below - runnin the .json() function (part of the requests library) means info pulled will be in json format and essentially a Python dictionary
fox = response.json()
print(fox['image']) #calling a specific key in the dictinary, to get it's value
print(fox['link']) #calling a specific key in the dictinary, to get it's value