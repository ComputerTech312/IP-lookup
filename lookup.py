import requests
import json

while True:
    print('Enter the IP to lookup')
    ip = input('IP: ')
    break

url = 'http://ipwho.is/' + ip
response = requests.get(url)
data = json.loads(response.text)

print(data)