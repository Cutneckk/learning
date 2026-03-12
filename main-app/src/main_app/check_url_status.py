import asyncio
import aiohttp


async def check_status(session, url):
    try:
        async with session.get(url) as response:
            if response.status != 200:
                print(f"{url}: Ошибка {response.status}")
            else:
                print(f"{url}: OK")
    except Exception as e:
        print(f"{url}: Не удалось подключиться", e)


async def main():
    urls = [
        'https://www.python.org',
        'https://www.google.com',
        'https://non-existent-domain-12345.org'
            ]

    async with aiohttp.ClientSession() as session:
        tasks = [check_status(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print('')


if __name__ == '__main__':
    asyncio.run(main())