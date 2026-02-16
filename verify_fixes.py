import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f'file://{os.getcwd()}/formaciones.html')
        await page.set_viewport_size({"width": 1280, "height": 800})

        # Capture Comparativa
        comparativa = await page.query_selector('section:has-text("¿Por qué elegir")')
        if comparativa:
            await comparativa.screenshot(path='comparativa_fixed.png')

        # Capture Hero
        hero = await page.query_selector('section.relative.min-h-\[85vh\]')
        if hero:
            await hero.screenshot(path='hero_fixed.png')

        await browser.close()

import os
asyncio.run(main())
