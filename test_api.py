import requests

url = "https://bfhl-api-z1tv.onrender.com/bfhl"  # ensure this is exact

payload = {"data": ["a","1","334","4","R","$"]}

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Response text:", response.text)  # show raw response first

try:
    data = response.json()
    print("Response JSON:", data)
except Exception as e:
    print("Could not parse JSON:", e)
