#use/bin/env python3
#-*- coding: utf-8 -*-

def abs(n):
    '''
    Fcuntion to get absolute value
    Example:
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)