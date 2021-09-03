import requests
import json

#Enter Bearer Token in between empty quotes below. Make sure to include the word "Bearer"
headers = {"Authorization": "","Content-Type":"application/json; charset=utf-8","Accept":"application/json, text/plain, */*"}
url = "http://34.34.34.34/api/security/addToBlacklist"


with open('filebog.txt') as file:
    lines = file.readlines()
    for line in lines:
        data = json.dumps({"domainName": line})
        response = requests.post(url,headers=headers,data=data)
        if response.status_code == 200:
            print("Added " + '\'' + line + '\'' + ' to the blacklist')
        if response.status_code != 200:
            print(line)
            break
