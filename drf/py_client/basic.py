import requests


endpoint = "http://127.0.0.1:8000/api/"

#get_response = requests.get(endpoint, params={"abc":123}, json = {"query": "Hello Wrold"})#HTTP request
#get_response = requests.get(endpoint, json = {'product_id':123})

get_response = requests.post(endpoint, json = {'title':'hello world'})

#print(get_response.headers)
#print(get_response.text)# print raw text response


print(get_response.json())


#print (get_response.status_code)