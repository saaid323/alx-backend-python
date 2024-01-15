#!/usr/bin/env python3
'''spawn wait_random n times with the specified max_delay'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''return sorted array of '''
    lis = []
    for i in range(n):
        lis.append(await wait_random(max_delay))
    return sorted(lis)
