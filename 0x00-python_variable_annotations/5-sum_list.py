#!/usr/bin/env python3
'''
Writes a type-annotated function sum_list
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Function that takes a list of floats input_list as an argument
    and returns their sum as a float
    '''
    return (sum(input_list))
