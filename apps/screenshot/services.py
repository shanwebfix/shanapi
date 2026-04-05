from playwright.sync_api import sync_playwright
import base64

async def capture_screenshot_logic(url: str):
    # sync কে async এ রান করার জন্য
    import asyncio
    return await asyncio.to_thread(_sync_capture, url)

def _sync_capture(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        page.goto(url, wait_until="domcontentloaded", timeout=30000)

        viewports = {
            "desktop": {"width": 1920, "height": 1080},
            "tablet": {"width": 768, "height": 1024},
            "mobile": {"width": 375, "height": 812}
        }

        results = {}
        for device, size in viewports.items():
            page.set_viewport_size(size)
            page.wait_for_timeout(500)
            screenshot_bytes = page.screenshot(full_page=True)
            results[device] = base64.b64encode(screenshot_bytes).decode('utf-8')

        browser.close()
        return results