#!/usr/bin/env python3
'''
Executes async_comprehension and measure total runtime
'''
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    '''
    Coroutinr that executes async_comprehesion 4 times in parallel using
    asyncio.gather and measures the runtime
    '''
    start = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end = time.time()
    return (end - start)
