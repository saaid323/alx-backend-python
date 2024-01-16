#!/usr/bin/env python3
'''return list of 10 floats'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''function that returns list of 10 floats'''
    lis = [i async for i in async_generator()]
    return lis
