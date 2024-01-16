#!/usr/bin/env python3
'''The coroutine will loop 10 times'''
import asyncio
import random
from typing import List


async def async_generator():
    '''function that yield a random number between 0 and 10'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
