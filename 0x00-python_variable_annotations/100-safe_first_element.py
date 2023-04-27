#!/usr/bin/env python3
'''
Augment the given code with correct duck-typed annotations
'''
from typing import Union, Any, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Function to be augmented with lst argument which is a sequence of any type
    and returns either an any type or nonetype
    '''
    if lst:
        return lst[0]
    else:
        return None
