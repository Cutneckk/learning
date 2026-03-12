import asyncio


async def countdown(name, seconds):
    for second in range(seconds, 0, -1):
        print(second)
        await asyncio.sleep(1)

    print(f"{name}: Пуск!")

async def main():
    await countdown("Таймер 1", 3)


if __name__ == '__main__':
    asyncio.run(main())