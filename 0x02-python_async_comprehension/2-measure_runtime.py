#!/usr/bin/env python3
'''measure the total runtime and return it.'''
import asyncio
import time
from typing import Generator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> Generator[float, None, None]:
    '''function measure the total runtime and return it.'''
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.time()
    return end - start
