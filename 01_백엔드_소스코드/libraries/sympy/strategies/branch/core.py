# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

''' Generic SymPy-Independent Strategies '''

def identity(x):
    pass
# WARNING: Decompyle incomplete


def exhaust(brule):
    ''' Apply a branching rule repeatedly until it has no effect '''
    pass
# WARNING: Decompyle incomplete


def onaction(brule, fn):
    pass
# WARNING: Decompyle incomplete


def debug(brule, file = (None,)):
    ''' Print the input and output expressions at each rule application '''
    pass
# WARNING: Decompyle incomplete


def multiplex(*brules):
    ''' Multiplex many branching rules into one '''
    pass
# WARNING: Decompyle incomplete


def condition(cond, brule):
    ''' Only apply branching rule if condition is true '''
    pass
# WARNING: Decompyle incomplete


def sfilter(pred, brule):
    ''' Yield only those results which satisfy the predicate '''
    pass
# WARNING: Decompyle incomplete


def notempty(brule):
    pass
# WARNING: Decompyle incomplete


def do_one(*brules):
    ''' Execute one of the branching rules '''
    pass
# WARNING: Decompyle incomplete


def chain(*brules):
    '''
    Compose a sequence of brules so that they apply to the expr sequentially
    '''
    pass
# WARNING: Decompyle incomplete


def yieldify(rl):
    ''' Turn a rule into a branching rule '''
    pass
# WARNING: Decompyle incomplete
