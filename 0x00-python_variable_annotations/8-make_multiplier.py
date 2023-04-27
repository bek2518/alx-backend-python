#!/usr/bin/env python3
'''
Writes a type-annotated function make_multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Function that takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier
    '''
    def multiply_function(value: float):
        return (value * multiplier)

    return (multiply_function)
