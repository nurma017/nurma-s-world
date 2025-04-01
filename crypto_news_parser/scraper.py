import asyncio
from playwright.async_api import async_playwright

allowed_cryptos = {
    "BTC": "bitcoin", "ETH": "ethereum", "ADA": "cardano", "XRP": "xrp",
    "DOGE": "dogecoin", "LTC": "litecoin", "BNB": "binancecoin",
    "SOL": "solana", "DOT": "polkadot", "AVAX": "avalanche"
}

async def get_news(symbol):
    symbol = symbol.upper()
    if symbol not in allowed_cryptos:
        raise ValueError(f"❌ '{symbol}' not supported")

    url = f"https://www.coingecko.com/en/coins/{allowed_cryptos[symbol]}/news"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, timeout=60000)
        await page.wait_for_timeout(5000)

        articles = await page.locator("a.tw-block").all()
        if not articles:
            print("❌ Статьи не найдены.")
            return []

        news_data = []
        for article in articles[:5]:
            title = await article.inner_text()
            href = await article.get_attribute("href")
            news_data.append({
                "title": title.strip(),
                "url": "https://www.coingecko.com" + href.strip()
            })

        await browser.close()
        return news_data