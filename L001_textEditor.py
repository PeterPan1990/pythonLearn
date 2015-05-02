# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:59:51 2015

@author: young
"""

def log(func):
    def wrapper(*args, **kw):
        print 'call %s()' % func.__name__
        return func(*argc, **kw)
    return wrapper
    
@log
def now():
    print '2013-12-25'