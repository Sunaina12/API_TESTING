import requests

payload={
    'name':'Sunaina',
    'job':'Engineer'
}

resp=requests.post('https://reqres.in/api/user',data=payload)
print(resp.status_code)
print(resp.json())
assert resp.json()['job']=='QA', 'Fail'