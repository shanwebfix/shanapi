# save_screenshot.py
import base64
import requests

# API কল করুন
response = requests.post(
    "http://127.0.0.1:8000/screenshot/generate",
    json={"url": "https://toolex.vercel.app"}
)

# রেসপন্স চেক করুন
if response.status_code == 200:
    screenshots = response.json()["screenshots"]
    
    # প্রতিটি ডিভাইসের জন্য স্ক্রিনশট সেভ করুন
    for device, img_data in screenshots.items():
        img_bytes = base64.b64decode(img_data)
        with open(f"{device}.png", "wb") as f:
            f.write(img_bytes)
        print(f"{device}.png সেভ হয়েছে!")
else:
    print(f"Error: {response.status_code}")