#!/usr/bin/env python3
'''
Annotate a give function's parameter and return values with appropriate types
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Given function to be annotated which takes an argument lst which is
    an Iterable of Sequence and returns a list of tuple with elements being
    a sequence and an int
    '''
    return [(i, len(i)) for i in lst]
