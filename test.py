import requests

response = requests.post(
    "http://127.0.0.1:8000/screenshot/generate",
    json={"url": "https://google.com"}
)

print("Status:", response.status_code)
if response.status_code == 200:
    print("Success!")
    data = response.json()
    print("Screenshots:", list(data.get("screenshots", {}).keys()))
else:
    print("Error:", response.text)