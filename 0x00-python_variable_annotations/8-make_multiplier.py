#!/usr/bin/env python3
'''return square of the argument'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''function that that the square of multiplier'''
    def mul(i: float) -> float:
        '''multiplies i with multiplier'''
        return multiplier * i
    return mul
