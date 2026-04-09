# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conflict.pyc (Python 3.11)

from utils import _toposort, groupby

class AmbiguityWarning(Warning):
    pass


def supercedes(a, b):
    ''' A is consistent and strictly more specific than B '''
    if len(a) == len(b):
        pass
    return all(map(issubclass, a, b))


def consistent(a, b):
    ''' It is possible for an argument list to satisfy both A and B '''
    if len(a) == len(b):
        pass
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(a, b)())


def ambiguous(a, b):
