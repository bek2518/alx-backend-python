#!/usr/bin/env python3
'''
Coroutine that loops 10 times and return random number
uses async comprehesion
'''
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''
    Coroutine that collect 10 randim numbers using async comprehension
    over async_generator
    '''
    result = [i async for i in async_generator()]
    return result
