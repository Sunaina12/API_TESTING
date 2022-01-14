import requests

#resp=requests.get('https://reqres.in/api/users?page=2')
# print(resp)
# print(type(resp))
# print(dir(resp))
# code=resp.status_code
#assert code==200, 'Code doesnt match'
# print(resp.text)
# print(resp.content)
# print(resp.json())
# print(resp.headers)
# print(resp.cookies)
# print(resp.encoding)
# print(resp.url)

# json_response=resp.json()
# total=json_response['total']
# print(total)
#
# assert total == 12
# total_pages=json_response['total_pages']
# print(total_pages)
#
# #assert total_pages!=2 , 'Not Valid'
#
# print(json_response['data'][0]['email'])
#
# assert (json_response['data'][0]['email']).endswith('reqre.in'), 'Invalid Email'
p={'page':2}
resp=requests.get('https://reqres.in/api/users',params=p)
print(resp.url)