# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: signals.pyc (Python 3.11)

'''
    Implements signals based on blinker if available, otherwise
    falls silently back to a noop. Shamelessly stolen from flask.signals:
    https://github.com/mitsuhiko/flask/blob/master/flask/signals.py
'''
signals_available = False

try:
    from blinker import Namespace
    signals_available = True
except ImportError:
    
    class Namespace:
        
        def signal(self, name, doc = (None,)):
            return _FakeSignal(name, doc)


    
    class _FakeSignal:
        '''If blinker is unavailable, create a fake class with the same
        interface that allows sending of signals but will fail with an
        error on anything else.  Instead of doing anything on send, it
        will just ignore the arguments and do nothing instead.
        '''
        
        def __init__(self, name, doc = (None,)):
            self.name = name
            self.__doc__ = doc

        
        def _fail(self, *args, **kwargs):
            raise RuntimeError('signalling support is unavailable because the blinker library is not installed.')

        
        def send(*a, **kw):
            pass

        connect = _fail
        disconnect = _fail
        has_receivers_for = _fail
        receivers_for = _fail
        temporarily_connected_to = _fail
        connected_to = _fail
        del _fail


_signals = Namespace()
scope_changed = _signals.signal('scope-changed')
