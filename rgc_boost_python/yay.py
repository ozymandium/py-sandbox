#!/usr/bin/env python
"""Some usage examples in python
    since only the c++ library is installed (this file not part of an installed module),
    you will not be able to install/import this file
"""
import libyay
from pprint import pprint as pp

pp(vars(libyay))

a_string = libyay.yay()
print a_string

hello = libyay.World()
hello.set('This is a struct!!')
print hello.greet()

hello_ = libyay.WorldClass()
print hello_.greet()
hello_.set('yay for C++ and Python!')
print hello_.greet()