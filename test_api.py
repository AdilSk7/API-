import requests

url = "http://127.0.0.1:5000/bfhl"

# This is the test input
payload = {"data": ["a","1","334","4","R","$"]}

# Send POST request
response = requests.post(url, json=payload)

# Print the results
print("Status code:", response.status_code)
print("Response JSON:", response.json())
