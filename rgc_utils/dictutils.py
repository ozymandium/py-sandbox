#!/usr/bin/env python
"""collection of utils for dictionaries"""

def extract_keyvals(dictin, dictout):
    """ get lowest level key, value pairs from nested dictionaries and put them
        into a specified output dictionary"""
    for key, value in dictin.iteritems():
        if isinstance(value, dict): # If value itself is dictionary
            extract_keyvals(value, dictout)
        elif isinstance(value, list): # If value itself is list
            for i in value:
                extract_keyvals(i, dictout)
        else:
            dictout[key] = value