import requests

payload = {'key1': 'value1', 'key2': ['value2','value3']}
r = requests.get('https://httpbin.org/get', params=payload)

print(r.url)