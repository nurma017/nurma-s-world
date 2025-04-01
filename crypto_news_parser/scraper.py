import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.coingecko.com/en/news", timeout=90000)

        await page.wait_for_load_state('networkidle')

        articles = await page.locator("a.tw-block").all()
        print(f"✅ Найдено статей: {len(articles)}\n")

        for article in articles[:10]:
            title = await article.inner_text()
            link = await article.get_attribute('href')
            print(f"{title.strip()}\nhttps://www.coingecko.com{link.strip()}\n")

        await browser.close()

asyncio.run(main())