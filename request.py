import requests

# r is a response object 
r = requests.get('https://api.github.com/events')

print('Status code',r.status_code)
print('Headers content type:',r.headers['content-type'])
print('Encoding:',r.encoding)
print('Text:',r.text)
print('JSON:',r.json())

# basic features provided by request module to fetch content , etc from particular url.