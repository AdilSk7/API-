import requests
resp = requests.get("https://bfhl-api-z1tv.onrender.com/")
print(resp.status_code)
print(resp.text)
