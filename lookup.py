import socket
import nmap
import requests
import json

while True:
    print('Enter the IP to lookup')
    ip = input('IP: ')
    break

url = 'http://ipwho.is/' + ip
response = requests.get(url)
data = json.loads(response.text)
nm = nmap.PortScanner()
nm = nmap.PortScanner()


print(data)
print(nm.scan(ip, '22'))# this is just in beta/testing
