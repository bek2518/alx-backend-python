#!/usr/bin/env python3
'''
Add type annotations to the given function
'''
from typing import Union, Any, TypeVar, Type, Mapping


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), Type[None]] = None)\
                     -> Union[Any, TypeVar('T')]:
    '''
    Added annotations to the function
    '''
    if key in dct:
        return dct[key]
    else:
        return default
