import asyncio


async def f():
	await asyncio.sleep(1.0)
	return 42


async def main():
	result = await f()
	print(result)


if __name__ == '__main__':
	asyncio.run(main())