import requests

url = "https://bfhl-api-z1tv.onrender.com/bfhl"

payload = {
    "data": ["a", "1", "334", "4", "R", "$"]
}

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Response JSON:", response.json())
