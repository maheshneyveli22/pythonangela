import requests
import os
os.environ['no_proxy'] = '*'

proxies = {
   'http': 'devproxy01.chq.ei:8080',
   'https': 'devproxy01.chq.ei:8080',
}

os.system("echo $http_proxy")
#response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response = requests.get(url = "https://reqres.in/api/users?page=2")
#response = requests.get(url = "https://api.kanye.rest")

print(response.json())
# print(response.json()["iss_position"])