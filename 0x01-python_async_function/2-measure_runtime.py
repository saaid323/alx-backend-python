#!/usr/bin/env python3
'''measures the total execution time for wait_n(n, max_delay), and
returns total_time / n'''
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''function that measures the total execution time for
    wait_n(n, max_delay) and returns total_time / n. Your function
    should return a float'''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total = end - start
    return total / n
