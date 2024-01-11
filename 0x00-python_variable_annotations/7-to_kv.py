#!/usr/bin/env python3
'''takes two arguments and returns tuple'''
from typing import Tuple, Mapping, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''function that return tuple'''
    return (k, v ** 2)
