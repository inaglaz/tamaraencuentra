import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f'file://{os.getcwd()}/index.html')
        await page.set_viewport_size({"width": 1280, "height": 800})

        # Capture Hero
        hero = await page.query_selector('section')
        if hero:
            await hero.screenshot(path='index_hero.png')

        await browser.close()

import os
asyncio.run(main())
