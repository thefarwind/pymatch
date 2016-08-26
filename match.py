from inspect import signature
from collections import OrderedDict

class Match(OrderedDict):
    @staticmethod
    def _call(func, *args, **kwds):
        if len(signature(func).parameters):return func(*args, **kwds)
        else:return func()
    @staticmethod
    def _guard(case, *args, **kwds):
        try:return case(*args, **kwds)
        except:return False
    def __call__(self, *args, **kwds):
        for case in self: 
            if Match._guard(case, *args, **kwds):
                return Match._call(self[case], *args, **kwds)
        raise IndexError('match case out of range')
