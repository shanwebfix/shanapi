# browser_test.py
import os
from pathlib import Path

# চেক করুন playwright এর ক্যাশ ফোল্ডার
home = Path.home()
cache_path = home / ".cache" / "ms-playwright"

if cache_path.exists():
    print(f"✓ Playwright cache found at: {cache_path}")
    browsers = list(cache_path.glob("*"))
    print(f"Installed browsers: {[b.name for b in browsers]}")
else:
    print("✗ Playwright cache not found")
    print("Run: playwright install chromium")

# ব্রাউজার লঞ্চ করার চেষ্টা
try:
    from playwright.sync_api import sync_playwright
    print("\nTrying to launch browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        print("✓ Browser launched successfully!")
        browser.close()
except Exception as e:
    print(f"✗ Failed to launch browser: {e}")