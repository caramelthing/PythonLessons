#this API will pull information from a site which track crypto currency, mock data
#info found here: https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide
#made an account on the site - neeed to generate an API key
#in file - secrets.api - to be set into the header
import requests
import secrets
from pprint import pprint as pp

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
headers = {                                   #taken from their site - swapping in API-KEY variable in Secrets.py file
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': secrets.API_KEY,
}
r = requests.get(url, headers=headers)
#pasted all the above into interpreter via linux shell. 
#>>> r.status_code
#200
pp(r.json()["data"][1])