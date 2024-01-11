#!/usr/bin/env python3
'''correcting the code'''
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''return the first element of lst or none'''
    if lst:
        return lst[0]
    else:
        return None
