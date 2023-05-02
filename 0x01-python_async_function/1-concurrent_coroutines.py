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
    listOfDelay: list = []
    sortedList: list = []
    i: int = 0
    while (i < n):
        delay = await wait_random(max_delay)
        listOfDelay.append(delay)
        i += 1

    def recurseSort(listOfDelay, sortedList):
        '''
        Function to sort the list in ascending order
        '''
        if (len(listOfDelay) != 0):
            minimum = min(listOfDelay)
            sortedList.append(minimum)
            listOfDelay.remove(minimum)
            return recurseSort(listOfDelay, sortedList)
        else:
            return sortedList

    recurseSort(listOfDelay, sortedList)

    return sortedList
