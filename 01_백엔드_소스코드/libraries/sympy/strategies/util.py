# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from sympy.core.basic import Basic
new = Basic.__new__

def assoc(d, k, v):
    d = d.copy()
    d[k] = v
    return d

basic_fns = {
    'op': type,
    'new': Basic.__new__,
    'leaf': (lambda x:
