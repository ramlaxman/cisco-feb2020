#!/usr/bin/env python3

import asyncio


async def hello():
    for i in range(5):
        await asyncio.sleep(1)
        print(f"{i} Hello!")


async def goodbye():
    for i in range(5):
        await asyncio.sleep(1)
        print(f"{i} Goodbye!")


loop = asyncio.get_event_loop()
loop.create_task(hello())
loop.create_task(goodbye())
loop.run_forever()
