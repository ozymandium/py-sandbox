#!/usr/bin/env python
from __future__ import print_function

def stopwatch(fn):
    """decorator that prints the time it takes for a function to execute"""
    from time import clock
    # before = float()

    def wrapper(*args, **kwargs):
        before = clock()
        fn_output = fn(*args, **kwargs)
        print('Elapsed time - ' + fn.__name__ + ' : %.6f s' % (clock()-before))
        return fn_output

    return wrapper


# def stopwatch(func):
#     """
#     A decorator that prints the time a function takes
#     to execute.
#     """
#     import time
#     def wrapper(*args, **kwargs):
#         t = time.clock()
#         res = func(*args, **kwargs)
#         print func.__name__, time.clock()-t
#         return res
#     return wrapper


# Example
@stopwatch
def crunch(x):
    y = []
    for z in range(x):
        y.append(z**5)
    return sum(y)**5


if __name__ == '__main__':
    m = crunch(1000000)