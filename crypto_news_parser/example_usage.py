import asyncio
from scraper import get_news
from utils import filter_news, save_news

async def main():
    symbol = "BTC"
    news = await get_news(symbol)

    print(f"✅ Найдено по фильтру {symbol}: {len(news)} новостей")

    filtered = filter_news(news, keyword="bitcoin")
    print(f"🔍 Отфильтровано по 'bitcoin': {len(filtered)}")

    save_news(filtered, filename="btc_news", filetype="json")
    print("💾 Сохранено в файл btc_news.json")

asyncio.run(main())