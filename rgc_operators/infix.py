#!/usr/bin/env python
# Infix operator class for 2 inputs


class Infix:
    """
    definition:
        op = Infix(lambda ....)
    
    calling sequence for the infix is either:
            x |op| y
    or:
            x <<op>> y
    """
    def __init__(self, function):
        self.function = function
    
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    
    def __or__(self, other):
        return self.function(other)
    
    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    
    def __rshift__(self, other):
        return self.function(other)

    def __call__(self, value1, value2):
        return self.function(value1, value2)


# an infixed operator for the partial class in functools
# used for currying
from functools import partial
part = Infix(partial)


if __name__ == '__main__':
    # Examples:
    add = Infix(lambda x,y: x+y)
    print 2 |add| 3


    def f(x,y):
        return x+y
    F = Infix(f)
    print 2 |F| 3


    @Infix
    def add(x,y):
        return x+y
    print 2 |add| 3


    def add(x,y,z):
        return x+y+z
    f = add |part| 2 |part| 3 |part| 4
    print f()

