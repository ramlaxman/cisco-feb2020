#!/usr/bin/env python3

import asyncio


async def hello():
    for i in range(5):
        print(f"{i} Hello!")


loop = asyncio.get_event_loop()
loop.create_task(hello())
loop.run_forever()
