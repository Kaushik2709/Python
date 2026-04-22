import asyncio

async def foo():
    print("foo")

async def main():
    await foo()
    await asyncio.sleep(1)
    print("main")

asyncio.run(main())