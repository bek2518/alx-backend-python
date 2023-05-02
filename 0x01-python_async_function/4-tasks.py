#!/usr/bin/env python3
'''
Async that imports task 3 and returns list of delays, identical to
wait_n except it calls for task_wait_random
'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Async routine takes int arguments n and max_delay, spawns task_wait_random
    n times with specified max_delay and returns list of the delays in
    ascending order without using sort()
    '''
    sortedList: List[float] = []

    listOfDelay = [task_wait_random(max_delay) for i in range(0, n)]

    for delay in asyncio.as_completed(listOfDelay):
        delayed = await delay
        sortedList.append(delayed)

    return sortedList
