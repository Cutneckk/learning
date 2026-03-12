import asyncio
import time


async def prepare_ingredients():
    await asyncio.sleep(2)
    print('Vegetables ready')


async def fry_meat():
    await asyncio.sleep(4)
    print('Meat ready')


async def boil_rice():
    await asyncio.sleep(3)
    print('Rise ready')


async def main():
    start_time = time.time()
    await prepare_ingredients()
    await asyncio.gather(fry_meat(), boil_rice())
    end_time = time.time()
    result_time = end_time - start_time
    print(f'Full cooking time: {result_time}')


if __name__ == '__main__':
    asyncio.run(main())