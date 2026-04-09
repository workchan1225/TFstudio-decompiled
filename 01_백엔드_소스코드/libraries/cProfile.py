# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cProfile.pyc (Python 3.11)

"""Python interface for the 'lsprof' profiler.
   Compatible with the 'profile' module.
"""
__all__ = [
    'run',
    'runctx',
    'Profile']
import _lsprof
import io
import profile as _pyprofile

def run(statement, filename, sort = (None, -1)):
    return _pyprofile._Utils(Profile).run(statement, filename, sort)


def runctx(statement, globals, locals, filename, sort = (None, -1)):
    return _pyprofile._Utils(Profile).runctx(statement, globals, locals, filename, sort)

run.__doc__ = _pyprofile.run.__doc__
runctx.__doc__ = _pyprofile.runctx.__doc__

class Profile(_lsprof.Profiler):
    '''Profile(timer=None, timeunit=None, subcalls=True, builtins=True)

    Builds a profiler object using the specified timer function.
    The default timer is a fast built-in one based on real time.
    For custom timer functions returning integers, timeunit can
    be a float specifying a scale (i.e. how long each integer unit
    is, in seconds).
    '''
    
    def print_stats(self, sort = (-1,)):
        import pstats
        pstats.Stats(self).strip_dirs().sort_stats(sort).print_stats()

    
    def dump_stats(self, file):
        import marshal
        f = open(file, 'wb')
        self.create_stats()
        marshal.dump(self.stats, f)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def create_stats(self):
        self.disable()
        self.snapshot_stats()

    
    def snapshot_stats(self):
        entries = self.getstats()
        self.stats = { }
        callersdicts = { }
        for entry in entries:
            func = label(entry.code)
            nc = entry.callcount
            cc = nc - entry.reccallcount
            tt = entry.inlinetime
            ct = entry.totaltime
            callers = { }
            callersdicts[id(entry.code)] = callers
            self.stats[func] = (cc, nc, tt, ct, callers)
            for entry in entries:
                if entry.calls:
                    func = label(entry.code)
                    for subentry in entry.calls:
                        callers = callersdicts[id(subentry.code)]
                    except KeyError:
                        continue
                    nc = subentry.callcount
                    cc = nc - subentry.reccallcount
                    tt = subentry.inlinetime
                    ct = subentry.totaltime
                    if func in callers:
                        prev = callers[func]
                        nc += prev[0]
                        cc += prev[1]
                        tt += prev[2]
                        ct += prev[3]
                    callers[func] = (nc, cc, tt, ct)
                    continue
                return None

    
    def run(self, cmd):
        import __main__
        dict = __main__.__dict__
        return self.runctx(cmd, dict, dict)

    
    def runctx(self, cmd, globals, locals):
        self.enable()
        
        try:
            exec(cmd, globals, locals)
            self.disable()
        except:
            self.disable()

        return self

    
    def runcall(self, func, *args, **kw):
        self.enable()
    # WARNING: Decompyle incomplete

    
    def __enter__(self):
        self.enable()
        return self

    
    def __exit__(self, *exc_info):
        self.disable()



def label(code):
    if isinstance(code, str):
        return ('~', 0, code)
    return (None.co_filename, code.co_firstlineno, code.co_name)


def main():
    import os
    import sys
    import runpy
    import pstats
    OptionParser = OptionParser
    import optparse
    usage = 'cProfile.py [-o output_file_path] [-s sort] [-m module | scriptfile] [arg] ...'
    parser = OptionParser(usage = usage)
    parser.allow_interspersed_args = False
    parser.add_option('-o', '--outfile', dest = 'outfile', help = 'Save stats to <outfile>', default = None)
    parser.add_option('-s', '--sort', dest = 'sort', help = 'Sort order when printing to stdout, based on pstats.Stats class', default = 2, choices = sorted(pstats.Stats.sort_arg_dict_default))
    parser.add_option('-m', dest = 'module', action = 'store_true', help = 'Profile a library module', default = False)
    if not sys.argv[1:]:
        parser.print_usage()
        sys.exit(2)
    (options, args) = parser.parse_args()
    sys.argv[:] = args
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    main()
    return None
