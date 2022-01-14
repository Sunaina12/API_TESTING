import json

import requests

mydata=open('data.json','r').read()

resp=requests.post('https://reqres.in/api/user',data=json.loads(mydata))


print(resp.status_code)
print(resp.json())