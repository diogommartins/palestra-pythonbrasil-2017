import asyncio
from aiohttp import ClientSession


urls = (
    'http://www.americanas.com', 'http://www.submarino.com',
    'http://www.shoptime.com', 'http://www.soubarato.com',
)


async def get_and_print(session, url):
    async with session.get(url) as response:
        await response.text()
        print(url)


async def fetch(urls):
    async with ClientSession() as session:
        tasks = (get_and_print(session, url) for url in urls)
        await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(fetch(urls))
