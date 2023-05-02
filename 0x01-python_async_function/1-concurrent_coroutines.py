#!/usr/bin/env python3
'''

'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Async routine takes int arguments n and max_delay, spawns wait_random
    n times with specified max_delay and returns list of the delays in
    ascending order without using sort()
    '''
    sortedList: List[float] = []

    listOfDelay = [wait_random(max_delay) for i in range(0, n)]

    for delay in asyncio.as_completed(listOfDelay):
        delayed = await delay
        sortedList.append(delayed)

    return sortedList
