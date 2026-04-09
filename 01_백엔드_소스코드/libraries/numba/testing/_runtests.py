# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _runtests.pyc (Python 3.11)

import json
import re
import logging

def _main(argv, **kwds):
    run_tests = run_tests
    import numba.testing
    if '--log' in argv:
        logging.basicConfig(level = logging.DEBUG)
        argv.remove('--log')
    if '--failed-first' in argv:
        argv.remove('--failed-first')
        return _FailedFirstRunner().main(argv, kwds)
    if None in argv:
        argv.remove('--last-failed')
        return _FailedFirstRunner(last_failed = True).main(argv, kwds)
# WARNING: Decompyle incomplete


def main(*argv, **kwds):
    '''keyword arguments are accepted for backward compatibility only.
    See `numba.testing.run_tests()` documentation for details.'''
    pass
# WARNING: Decompyle incomplete


class _FailedFirstRunner(object):
    '''
    Test Runner to handle the failed-first (--failed-first) option.
    '''
    cache_filename = '.runtests_lastfailed'
    
    def __init__(self, last_failed = (False,)):
        self.last_failed = last_failed

    
    def main(self, argv, kwds):
        pass
    # WARNING: Decompyle incomplete

    
    def save_failed_tests(self, result, all_tests):
        print('Saving failed tests to {}'.format(self.cache_filename))
        cache = []
        failed = set()
        for case in result.errors + result.failures:
            failed.add(case[0].id())
            for t in all_tests:
                if t in failed:
                    cache.append(t)
                fout = open(self.cache_filename, 'w')
                json.dump(cache, fout)
                None(None, None)
                return None
                with None:
                    if not None:
                        pass

    
    def find_last_failed(self, argv):
        pass
    # WARNING: Decompyle incomplete
