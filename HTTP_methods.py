import requests

# Sends data to the server to create a new resource. In your code, it sends the form data {'key': 'value'} to the server.
r = requests.post('https://httpbin.org/post', data={'key': 'value'}) 
print("Post status code:",r.status_code)

# Sends data to update or replace an existing resource entirely.
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
print("Put status code:",r.status_code)

# Instructs the server to remove a specific resource.
r = requests.delete('https://httpbin.org/delete')
print("Delete status code:",r.status_code)

# Asks for the exact same headers that a GET request would return, but without the actual body content (HTML or data).
r = requests.head('https://httpbin.org/get')
print("Head status code:",r.status_code)

# Asks the server to list which HTTP methods (GET, POST, etc.) and security policies it permits for that URL.
r = requests.options('https://httpbin.org/get')
print("Options status code:",r.status_code)
print(r.connection)