import asyncio


@asyncio.coroutine
def soma(x, y):
    print("Calulando {x} + {y} ...".format(x=x, y=y))
    yield from asyncio.sleep(1.0)
    return x + y


@asyncio.coroutine
def print_soma(x, y):
    result = yield from soma(x, y)
    print("{x} + {y} = {result}".format(x=x,
                                        y=y,
                                        result=result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_soma(1, 2))
loop.close()
