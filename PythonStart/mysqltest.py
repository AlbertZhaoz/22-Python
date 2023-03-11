import asyncio

async def Print():
    print("Hello world")
    r = await asyncio.sleep(1)
    print("Hello again")

if __name__ == "__main__":
    # 获取 EventLoop
    loop = asyncio.get_event_loop()
    # 执行 coroutine
    loop.run_until_complete(Print())
    # 关闭 loop
    loop.close()
