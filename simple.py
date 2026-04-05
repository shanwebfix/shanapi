import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # headless=False রাখুন
        page = await browser.new_page()
        await page.goto("https://google.com")
        print("সফল!")
        await browser.close()

asyncio.run(test())