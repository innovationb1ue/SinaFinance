import asyncio
import time
import aiohttp

async def main():
    task1 = asyncio.create_task(p1r())
    task2 = asyncio.create_task(pr())

    # await task1
    await task2
    # print(task1.result())
    # loop.close()

async def p1r():
    print('调用p1r',time.time())
    await asyncio.sleep(1)
    print('完成p1r')
    return 'p1r返回值'
async def pr():
    print('调用pr',time.time())
    return 1


if __name__ == '__main__':
    asyncio.run(main())
