# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: runtests.pyc (Python 3.11)

from numba.testing._runtests import _main
if __name__ == '__main__':
    import sys
    from multiprocessing import freeze_support
    freeze_support()
    sys.exit(0 if _main(sys.argv) else 1)
    return None
