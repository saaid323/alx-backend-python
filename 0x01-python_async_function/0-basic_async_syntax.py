#!/usr/bin/env python3
'''module that  waits for a random delay between 0 and max_delay'''
import asyncio
import random


async def wait_random(max_delay=10):
    '''return random number between 0 and 10'''
    ran = random.uniform(0, max_delay)
    await asyncio.sleep(ran)
    return ran
