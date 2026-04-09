# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: calculus.pyc (Python 3.11)


class CalculusMethods(object):
    pass


def defun(f):
    setattr(CalculusMethods, f.__name__, f)
    return f
