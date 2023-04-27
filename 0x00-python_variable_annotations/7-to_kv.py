#!/usr/bin/env python3
'''
Writes a type-annotated function to_kv
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Function that takes a string k and an int OR float v as argument
    and returns a tuple with the second element is a square of the int/float
    annotated as float
    '''

    return ((k, v*v))
