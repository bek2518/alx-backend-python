#!/usr/bin/env python3
'''
Using mypy to validate the given code
'''
from typing import Tuple, List, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
    Function that accepts a tuple lst and an int factor with default
    value of 2 and returns a list
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
