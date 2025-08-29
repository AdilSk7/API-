import requests

# Your hosted API endpoint
url = "https://bfhl-api-z1tv.onrender.com/bfhl"

# The JSON payload we want to send (just like in the examples)
payload = {
    "data": ["a", "1", "334", "4", "R", "$"]
}

# Send a POST request with JSON data
response = requests.post(url, json=payload)

# Print results
print("Status code:", response.status_code)
print("Response JSON:", response.json())
