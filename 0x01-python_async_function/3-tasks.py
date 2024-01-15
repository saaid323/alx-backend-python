#!/usr/bin/env python3
'''returns a asyncio.Task'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    '''returns a asyncio.Task'''
    async def delay():
        m = await wait_random(max_delay)
        return m
    return asyncio.create_task(delay())
