import asyncio


async def long_running_task():
    print('Фоновая задача начала работу')
    await asyncio.sleep(5)
    print('Фоновая задача завершила работу')


async def main():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(0)
    print('Основная задача продолжает работу')

    for i in range(3):
        print('Основная программа работает')
        await asyncio.sleep(1)

    await task


if __name__ == '__main__':
    asyncio.run(main())