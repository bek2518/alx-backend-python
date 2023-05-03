#!/usr/bin/env python3
'''
Coroutine that loops 10 times and return random number
'''
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Coroutine that takes no arguments, which loops 10 times asynchronously
    waits 1 second then yield a random number between 0 and 10
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
