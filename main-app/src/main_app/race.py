import asyncio


async def racer(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} финишировал!")


async def main():
    await asyncio.gather(
        racer('lightning', 2), racer('arrow', 1.5)
    )


if __name__ == '__main__':
    asyncio.run(main())