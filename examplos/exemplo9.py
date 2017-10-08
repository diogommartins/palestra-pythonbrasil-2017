import asyncio


async def soma(x, y):
    print(f"Calulando {x} + {y} ...")
    await asyncio.sleep(1.0)
    return x + y

async def print_soma(x, y):
    result = await soma(x, y)
    print(f"{x} + {y} = {result}")

loop = asyncio.get_event_loop()
loop.run_until_complete(print_soma(1, 666))
loop.close()
