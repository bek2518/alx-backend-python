#!/usr/bin/env python3
'''
Writes a type-annotated function sum_mixed_list
'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''
    Function that takes a list of integers and floats mxd_list as an argument
    and returns their sum as a float
    '''
    return (sum(mxd_list))
