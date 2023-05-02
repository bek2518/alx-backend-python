#!/usr/bin/env python3
'''
Asynchronous coroutine named wait_random that uses random module
'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    Asynchronous coroutine that takes in an integer argument
    max_delay with default value 10, awaits a random delay and returns
    the value
    '''
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return (i)
