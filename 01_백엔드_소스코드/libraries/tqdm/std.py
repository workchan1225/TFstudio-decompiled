# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: std.pyc (Python 3.11)

'''
Customisable progressbar decorator for iterators.
Includes a default `range` iterator printing to `stderr`.

Usage:
>>> from tqdm import trange, tqdm
>>> for i in trange(10):
...     ...
'''
import sys
from collections import OrderedDict, defaultdict
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from numbers import Number
from time import time
from warnings import warn
from weakref import WeakSet
from _monitor import TMonitor
from utils import CallbackIOWrapper, Comparable, DisableOnWriteError, FormatReplace, SimpleTextIOWrapper, _is_ascii, _screen_shape_wrapper, _supports_unicode, _term_move_up, disp_len, disp_trim, envwrap
__author__ = 'https://github.com/tqdm/tqdm#contributions'
__all__ = [
    'tqdm',
    'trange',
    'TqdmTypeError',
    'TqdmKeyError',
    'TqdmWarning',
    'TqdmExperimentalWarning',
    'TqdmDeprecationWarning',
    'TqdmMonitorWarning']

class TqdmTypeError(TypeError):
    pass


class TqdmKeyError(KeyError):
    pass


class TqdmWarning(Warning):
    pass
# WARNING: Decompyle incomplete


class TqdmExperimentalWarning(FutureWarning, TqdmWarning):
    '''beta feature, unstable API and behaviour'''
    pass


class TqdmDeprecationWarning(DeprecationWarning, TqdmWarning):
    pass


class TqdmMonitorWarning(RuntimeWarning, TqdmWarning):
    '''tqdm monitor errors which do not affect external functionality'''
    pass


def TRLock(*args, **kwargs):
    '''threading RLock'''
    pass
# WARNING: Decompyle incomplete


class TqdmDefaultWriteLock(object):
    '''
    Provide a default write lock for thread and multiprocessing safety.
    Works only on platforms supporting `fork` (so Windows is excluded).
    You must initialise a `tqdm` or `TqdmDefaultWriteLock` instance
    before forking in order for the write lock to work.
    On Windows, you need to supply the lock from the parent to the children as
    an argument to joblib or the parallelism lib you use.
    '''
    th_lock = TRLock()
    
    def __init__(self):
        cls = type(self)
        root_lock = cls.th_lock
    # WARNING: Decompyle incomplete

    
    def acquire(self, *a, **k):
        pass
    # WARNING: Decompyle incomplete

    
    def release(self):
        for lock in self.locks[::-1]:
            lock.release()
            return None

    
    def __enter__(self):
        self.acquire()

    
    def __exit__(self, *exc):
        self.release()

    create_mp_lock = (lambda cls: if not hasattr(cls, 'mp_lock'):
try:
RLock = RLockimport multiprocessingcls.mp_lock = RLock()Noneexcept (ImportError, OSError):
cls.mp_lock = NoneNoneNone)()
    create_th_lock = (lambda cls: pass# WARNING: Decompyle incomplete
)()


class Bar(object):
    '''
    `str.format`-able bar with format specifiers: `[width][type]`

    - `width`
      + unspecified (default): use `self.default_len`
      + `int >= 0`: overrides `self.default_len`
      + `int < 0`: subtract from `self.default_len`
    - `type`
      + `a`: ascii (`charset=self.ASCII` override)
      + `u`: unicode (`charset=self.UTF` override)
      + `b`: blank (`charset="  "` override)
    '''
    ASCII = ' 123456789#'
    UTF = ' ' + ''.join(map(chr, range(9615, 9607, -1)))
    BLANK = '  '
    COLOUR_RESET = '\x1b[0m'
    COLOUR_RGB = '\x1b[38;2;%d;%d;%dm'
    COLOURS = {
        'BLACK': '\x1b[30m',
        'RED': '\x1b[31m',
        'GREEN': '\x1b[32m',
        'YELLOW': '\x1b[33m',
        'BLUE': '\x1b[34m',
        'MAGENTA': '\x1b[35m',
        'CYAN': '\x1b[36m',
        'WHITE': '\x1b[37m' }
    
    def __init__(self, frac, default_len, charset, colour = (10, UTF, None)):
        if not  <= 0, frac or 0, frac <= 1:
            pass
        
        warn('clamping frac to range [0, 1]', TqdmWarning, stacklevel = 2)
    # WARNING: Decompyle incomplete

    colour = (lambda self: self._colour)()
    colour = (lambda self, value: if not value:
self._colour = NoneNonetry:
if value.upper() in self.COLOURS:
self._colour = self.COLOURS[value.upper()]Noneif None[0] == '#' and len(value) == 7:
self._colour = tuple % (lambda .0: pass# WARNING: Decompyle incomplete
)((value[1:3], value[3:5], value[5:7])())
                return None
            raise None
        except (KeyError, AttributeError):
            warn(f'''Unknown colour ({value!s}); valid choices: [hex (#00ff00), {', '.join(self.COLOURS)!s}]''', TqdmWarning, stacklevel = 2)
            self._colour = None
            return None

)()
    
    def __format__(self, format_spec):
        if format_spec:
            _type = format_spec[-1].lower()
            
            try:
                charset = {
                    'a': self.ASCII,
                    'u': self.UTF,
                    'b': self.BLANK }[_type]
                format_spec = format_spec[:-1]
            except KeyError:
                charset = self.charset

            if format_spec:
                N_BARS = int(format_spec)
                if N_BARS < 0:
                    N_BARS += self.default_len
                else:
                    N_BARS = self.default_len
            else:
                charset = self.charset
                N_BARS = self.default_len
        nsyms = len(charset) - 1
        (bar_length, frac_bar_length) = divmod(int(self.frac * N_BARS * nsyms), nsyms)
        res = charset[-1] * bar_length
        if bar_length < N_BARS:
            res = res + charset[frac_bar_length] + charset[0] * (N_BARS - bar_length - 1)
        return self.colour + res + self.COLOUR_RESET if self.colour else res



class EMA(object):
    '''
    Exponential moving average: smoothing to give progressively lower
    weights to older values.

    Parameters
    ----------
    smoothing  : float, optional
        Smoothing factor in range [0, 1], [default: 0.3].
        Increase to give more weight to recent values.
        Ranges from 0 (yields old value) to 1 (yields new value).
    '''
    
    def __init__(self, smoothing = (0.3,)):
        self.alpha = smoothing
        self.last = 0
        self.calls = 0

    
    def __call__(self, x = (None,)):
        '''
        Parameters
        ----------
        x  : float
            New value to include in EMA.
        '''
        beta = 1 - self.alpha
    # WARNING: Decompyle incomplete



class tqdm(Comparable):
    '''
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.

    Parameters
    ----------
    iterable  : iterable, optional
        Iterable to decorate with a progressbar.
        Leave blank to manually manage the updates.
    desc  : str, optional
        Prefix for the progressbar.
    total  : int or float, optional
        The number of expected iterations. If unspecified,
        len(iterable) is used if possible. If float("inf") or as a last
        resort, only basic progress statistics are displayed
        (no ETA, no progressbar).
        If `gui` is True and this parameter needs subsequent updating,
        specify an initial arbitrary large positive number,
        e.g. 9e9.
    leave  : bool, optional
        If [default: True], keeps all traces of the progressbar
        upon termination of iteration.
        If `None`, will leave only if `position` is `0`.
    file  : `io.TextIOWrapper` or `io.StringIO`, optional
        Specifies where to output the progress messages
        (default: sys.stderr). Uses `file.write(str)` and `file.flush()`
        methods.  For encoding, see `write_bytes`.
    ncols  : int, optional
        The width of the entire output message. If specified,
        dynamically resizes the progressbar to stay within this bound.
        If unspecified, attempts to use environment width. The
        fallback is a meter width of 10 and no limit for the counter and
        statistics. If 0, will not print any meter (only stats).
    mininterval  : float, optional
        Minimum progress display update interval [default: 0.1] seconds.
    maxinterval  : float, optional
        Maximum progress display update interval [default: 10] seconds.
        Automatically adjusts `miniters` to correspond to `mininterval`
        after long display update lag. Only works if `dynamic_miniters`
        or monitor thread is enabled.
    miniters  : int or float, optional
        Minimum progress display update interval, in iterations.
        If 0 and `dynamic_miniters`, will automatically adjust to equal
        `mininterval` (more CPU efficient, good for tight loops).
        If > 0, will skip display of specified number of iterations.
        Tweak this and `mininterval` to get very efficient loops.
        If your progress is erratic with both fast and slow iterations
        (network, skipping items, etc) you should set miniters=1.
    ascii  : bool or str, optional
        If unspecified or False, use unicode (smooth blocks) to fill
        the meter. The fallback is to use ASCII characters " 123456789#".
    disable  : bool, optional
        Whether to disable the entire progressbar wrapper
        [default: False]. If set to None, disable on non-TTY.
    unit  : str, optional
        String that will be used to define the unit of each iteration
        [default: it].
    unit_scale  : bool or int or float, optional
        If 1 or True, the number of iterations will be reduced/scaled
        automatically and a metric prefix following the
        International System of Units standard will be added
        (kilo, mega, etc.) [default: False]. If any other non-zero
        number, will scale `total` and `n`.
    dynamic_ncols  : bool, optional
        If set, constantly alters `ncols` and `nrows` to the
        environment (allowing for window resizes) [default: False].
    smoothing  : float, optional
        Exponential moving average smoothing factor for speed estimates
        (ignored in GUI mode). Ranges from 0 (average speed) to 1
        (current/instantaneous speed) [default: 0.3].
    bar_format  : str, optional
        Specify a custom bar string formatting. May impact performance.
        [default: \'{l_bar}{bar}{r_bar}\'], where
        l_bar=\'{desc}: {percentage:3.0f}%|\' and
        r_bar=\'| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, \'
            \'{rate_fmt}{postfix}]\'
        Possible vars: l_bar, bar, r_bar, n, n_fmt, total, total_fmt,
            percentage, elapsed, elapsed_s, ncols, nrows, desc, unit,
            rate, rate_fmt, rate_noinv, rate_noinv_fmt,
            rate_inv, rate_inv_fmt, postfix, unit_divisor,
            remaining, remaining_s, eta.
        Note that a trailing ": " is automatically removed after {desc}
        if the latter is empty.
    initial  : int or float, optional
        The initial counter value. Useful when restarting a progress
        bar [default: 0]. If using float, consider specifying `{n:.3f}`
        or similar in `bar_format`, or specifying `unit_scale`.
    position  : int, optional
        Specify the line offset to print this bar (starting from 0)
        Automatic if unspecified.
        Useful to manage multiple bars at once (eg, from threads).
    postfix  : dict or *, optional
        Specify additional stats to display at the end of the bar.
        Calls `set_postfix(**postfix)` if possible (dict).
    unit_divisor  : float, optional
        [default: 1000], ignored unless `unit_scale` is True.
    write_bytes  : bool, optional
        Whether to write bytes. If (default: False) will write unicode.
    lock_args  : tuple, optional
        Passed to `refresh` for intermediate output
        (initialisation, iterating, and updating).
    nrows  : int, optional
        The screen height. If specified, hides nested bars outside this
        bound. If unspecified, attempts to use environment height.
        The fallback is 20.
    colour  : str, optional
        Bar colour (e.g. \'green\', \'#00ff00\').
    delay  : float, optional
        Don\'t display until [default: 0] seconds have elapsed.
    gui  : bool, optional
        WARNING: internal parameter - do not use.
        Use tqdm.gui.tqdm(...) instead. If set, will attempt to use
        matplotlib animations for a graphical output [default: False].

    Returns
    -------
    out  : decorated iterator.
    '''
    monitor_interval = 10
    monitor = None
    _instances = WeakSet()
    format_sizeof = (lambda num, suffix, divisor = ('', 1000): for unit in ('', 'k', 'M', 'G', 'T', 'P', 'E', 'Z'):
if abs(num) < 999.5:
if abs(num) < 99.95:
if abs(num) < 9.995:
None, f'''{num:1.2f}{unit}{suffix}'''None, f'''{None:2.1f}{unit}{suffix}'''None, f'''{None:3.0f}{unit}{suffix}'''f'''{num:3.1f}Y{suffix}''')()
    format_interval = (lambda t: (mins, s) = divmod(int(t), 60)(h, m) = divmod(mins, 60)f'''{h:d}:{m:02d}:{s:02d}''' if h else f'''{m:02d}:{s:02d}''')()
    format_num = (lambda n: f = f'''{n:.3g}'''.replace('e+0', 'e+').replace('e-0', 'e-')n = str(n)f if len(f) < len(n) else n)()
    status_printer = (lambda file: pass# WARNING: Decompyle incomplete
)()
    format_meter = (lambda n, total, elapsed, ncols, prefix, ascii, unit, unit_scale, rate, bar_format, postfix, unit_divisor, initial, colour = (None, '', False, 'it', False, None, None, None, 1000, 0, None): if total and n >= total + 0.5:
total = Noneif unit_scale and unit_scale not in (True, 1):
if total:
total *= unit_scalen *= unit_scaleif rate:
rate *= unit_scaleunit_scale = Falseelapsed_str = tqdm.format_interval(elapsed)# WARNING: Decompyle incomplete
)()
    
    def __new__(cls, *_, **__):
        instance = object.__new__(cls)
        cls.get_lock()
        cls._instances.add(instance)
    # WARNING: Decompyle incomplete

    _get_free_pos = (lambda cls, instance = (None,): pass# WARNING: Decompyle incomplete
)()
    _decr_instances = (lambda cls, instance: pass# WARNING: Decompyle incomplete
)()
    write = (lambda cls, s, file, end, nolock = (None, '\n', False): pass# WARNING: Decompyle incomplete
)()
    external_write_mode = (lambda cls, file, nolock = (None, False): pass# WARNING: Decompyle incomplete
)()()
    set_lock = (lambda cls, lock: cls._lock = lock)()
    get_lock = (lambda cls: if not hasattr(cls, '_lock'):
cls._lock = TqdmDefaultWriteLock()cls._lock)()
    pandas = (lambda cls: pass# WARNING: Decompyle incomplete
)()
    __init__ = (lambda self, iterable, desc, total, leave, file, ncols, mininterval, maxinterval, miniters, ascii, disable, unit, unit_scale, dynamic_ncols, smoothing, bar_format, initial, position, postfix, unit_divisor, write_bytes, lock_args, nrows, colour, delay, gui = (None, None, None, True, None, None, 0.1, 10, None, None, False, 'it', False, False, 0.3, None, 0, None, None, 1000, False, None, None, None, 0, False): pass# WARNING: Decompyle incomplete
)()
    
    def __bool__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __len__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __reversed__(self):
        
        try:
            orig = self.iterable
            
            try:
                self.iterable = reversed(self.iterable)
                self.iterable = orig
                return self.__iter__()
                except AttributeError:
                    raise TypeError("'tqdm' object is not reversible")
                
                try:
                    pass
                except:
                    self.iterable = orig




    
    def __contains__(self, item):
        contains = getattr(self.iterable, '__contains__', None)
    # WARNING: Decompyle incomplete

    
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc_value, traceback):
        
        try:
            self.close()
            return None
        except AttributeError:
            if (exc_type, exc_value, traceback) == (None, None, None):
                raise 
            warn('AttributeError ignored', TqdmWarning, stacklevel = 2)
            return None


    
    def __del__(self):
        self.close()

    
    def __str__(self):
        pass
    # WARNING: Decompyle incomplete

    _comparable = (lambda self: abs(getattr(self, 'pos', 0x80000000)))()
    
    def __hash__(self):
        return id(self)

    
    def __iter__(self):
        '''Backward-compatibility to use: for x in tqdm(iterable)'''
        pass
    # WARNING: Decompyle incomplete

    
    def update(self, n = (1,)):
        '''
        Manually update the progress bar, useful for streams
        such as reading files.
        E.g.:
        >>> t = tqdm(total=filesize) # Initialise
        >>> for current_buffer in stream:
        ...    ...
        ...    t.update(len(current_buffer))
        >>> t.close()
        The last line is highly recommended, but possibly not necessary if
        `t.update()` will be called in such a way that `filesize` will be
        exactly reached and printed.

        Parameters
        ----------
        n  : int or float, optional
            Increment to add to the internal counter of iterations
            [default: 1]. If using float, consider specifying `{n:.3f}`
            or similar in `bar_format`, or specifying `unit_scale`.

        Returns
        -------
        out  : bool or None
            True if a `display()` was triggered.
        '''
        if self.disable:
            return None
        if None < 0:
            pass
        if self.n - self.last_print_n >= self.miniters:
            self._time() = self, self.n += n, .n
            dt = cur_t - self.last_print_t
            if dt >= self.mininterval or cur_t >= self.start_t + self.delay:
                cur_t = self._time()
                dn = self.n - self.last_print_n
                if self.smoothing and dt and dn:
                    self._ema_dn(dn)
                    self._ema_dt(dt)
                self.refresh(lock_args = self.lock_args)
                if self.dynamic_miniters:
                    if self.maxinterval and dt >= self.maxinterval:
                        if not self.mininterval:
                            self.miniters = dn * self.maxinterval / dt
                        elif self.smoothing:
                            self.miniters = self._ema_miniters(dn * self.mininterval / dt if self.mininterval and dt else 1)
                        else:
                            self.miniters = max(self.miniters, dn)
                self.last_print_n = self.n
                self.last_print_t = cur_t
                return True
            return self, self.last_print_n += n, .last_print_n
        return self, self.n += n, .n

    
    def close(self):
        '''Cleanup and (if leave=False) close the progressbar.'''
        pass
    # WARNING: Decompyle incomplete

    
    def clear(self, nolock = (False,)):
        '''Clear current bar display.'''
        if self.disable:
            return None
        if not None:
            self._lock.acquire()
        pos = abs(self.pos)
        if self.nrows or pos < 20:
            self.moveto(pos)
            self.sp('')
            self.fp.write('\r')
            self.moveto(-pos)
        if not nolock:
            self._lock.release()
            return None

    
    def refresh(self, nolock, lock_args = (False, None)):
        """
        Force refresh the display of this bar.

        Parameters
        ----------
        nolock  : bool, optional
            If `True`, does not lock.
            If [default: `False`]: calls `acquire()` on internal lock.
        lock_args  : tuple, optional
            Passed to internal lock's `acquire()`.
            If specified, will only `display()` if `acquire()` returns `True`.
        """
        if self.disable:
            return None
    # WARNING: Decompyle incomplete

    
    def unpause(self):
        '''Restart tqdm timer from last print time.'''
        if self.disable:
            return None
        cur_t = None._time()
        cur_t = self, self.start_t += cur_t - self.last_print_t, .start_t

    
    def reset(self, total = (None,)):
        '''
        Resets to 0 iterations for repeated use.

        Consider combining with `leave=True`.

        Parameters
        ----------
        total  : int or float, optional. Total to use for the new bar.
        '''
        self.n = 0
    # WARNING: Decompyle incomplete

    
    def set_description(self, desc, refresh = (None, True)):
        '''
        Set/modify description of the progress bar.

        Parameters
        ----------
        desc  : str, optional
        refresh  : bool, optional
            Forces refresh [default: True].
        '''
        self.desc = desc + ': ' if desc else ''
        if refresh:
            self.refresh()
            return None

    
    def set_description_str(self, desc, refresh = (None, True)):
