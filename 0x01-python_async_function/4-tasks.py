#!/usr/bin/env python3
'''return the list of all the delays (float values)'''
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    '''return the list of all the delays (float values)'''
    lis = []
    for i in range(n):
        lis.append(await task_wait_random(max_delay))
    return lis
