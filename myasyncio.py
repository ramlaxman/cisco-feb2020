#!/usr/bin/env python3

import asyncio


def hello():
    print("Hello!")


loop = asyncio.get_event_loop()
loop.create_task(hello())
loop.run_forever()
