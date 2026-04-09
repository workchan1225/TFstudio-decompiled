# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: warnings.pyc (Python 3.11)

'''Python part of the warnings subsystem.'''
import sys
__all__ = [
    'warn',
    'warn_explicit',
    'showwarning',
    'formatwarning',
    'filterwarnings',
    'simplefilter',
    'resetwarnings',
    'catch_warnings']

def showwarning(message, category, filename, lineno, file, line = (None, None)):
    '''Hook to write a warning to a file; replace if you like.'''
    msg = WarningMessage(message, category, filename, lineno, file, line)
    _showwarnmsg_impl(msg)


def formatwarning(message, category, filename, lineno, line = (None,)):
    '''Function to format a warning the standard way.'''
    msg = WarningMessage(message, category, filename, lineno, None, line)
    return _formatwarnmsg_impl(msg)


def _showwarnmsg_impl(msg):
    file = msg.file
# WARNING: Decompyle incomplete


def _formatwarnmsg_impl(msg):
    category = msg.category.__name__
    s = f'''{msg.filename}:{msg.lineno}: {category}: {msg.message}\n'''
# WARNING: Decompyle incomplete

_showwarning_orig = showwarning

def _showwarnmsg(msg):
    '''Hook to write a warning to a file; replace if you like.'''
    
    try:
        sw = showwarning
        if sw is not _showwarning_orig:
            if not callable(sw):
                raise TypeError('warnings.showwarning() must be set to a function or method')
            sw(msg.message, msg.category, msg.filename, msg.lineno, msg.file, msg.line)
            return None
    except NameError:
        pass

    _showwarnmsg_impl(msg)

_formatwarning_orig = formatwarning

def _formatwarnmsg(msg):
    '''Function to format a warning the standard way.'''
    
    try:
        fw = formatwarning
        if fw is not _formatwarning_orig:
            return fw(msg.message, msg.category, msg.filename, msg.lineno, msg.line)
    except NameError:
        pass

    return _formatwarnmsg_impl(msg)


def filterwarnings(action, message, category, module, lineno, append = ('', Warning, '', 0, False)):
    '''Insert an entry into the list of warnings filters (at the front).

    \'action\' -- one of "error", "ignore", "always", "default", "module",
                or "once"
    \'message\' -- a regex that the warning message must match
    \'category\' -- a class that the warning must be a subclass of
    \'module\' -- a regex that the module name must match
    \'lineno\' -- an integer line number, 0 matches all warnings
    \'append\' -- if true, append to the list of filters
    '''
    pass
# WARNING: Decompyle incomplete


def simplefilter(action, category, lineno, append = (Warning, 0, False)):
    '''Insert a simple entry into the list of warnings filters (at the front).

    A simple filter matches all modules and messages.
    \'action\' -- one of "error", "ignore", "always", "default", "module",
                or "once"
    \'category\' -- a class that the warning must be a subclass of
    \'lineno\' -- an integer line number, 0 matches all warnings
    \'append\' -- if true, append to the list of filters
    '''
    pass
# WARNING: Decompyle incomplete


def _add_filter(*, append, *item):
    if not append:
        
        try:
            filters.remove(item)
        except ValueError:
            pass

        filters.insert(0, item)
    elif item not in filters:
        filters.append(item)
    _filters_mutated()


def resetwarnings():
    '''Clear the list of warning filters, so that no filters are active.'''
    filters[:] = []
    _filters_mutated()


class _OptionError(Exception):
    '''Exception used by option processing helpers.'''
    pass


def _processoptions(args):
    for arg in args:
        _setoption(arg)
        except _OptionError:
            msg = None
            print('Invalid -W option ignored:', msg, file = sys.stderr)
            msg = None
            del msg
            continue
            msg = None
            del msg
        return None


def _setoption(arg):
    parts = arg.split(':')
    if len(parts) > 5:
        raise _OptionError(f'''too many fields (max 5): {arg!r}''')
# WARNING: Decompyle incomplete


def _getaction(action):
    if not action:
        return 'default'
    if None == 'all':
        return 'always'
    for a in None:
        if a.startswith(action):
            
            return None, a
        raise _OptionError(f'''invalid action: {action!r}''')


def _getcategory(category):
    if not category:
        return Warning
    if None not in category:
        import builtins as m
        klass = category
    else:
        (module, _, klass) = category.rpartition('.')
        
        try:
            m = __import__(module, None, None, [
                klass])
        except ImportError:
            raise _OptionError(f'''invalid module name: {module!r}'''), None

        
        try:
            cat = getattr(m, klass)
        except AttributeError:
            raise _OptionError(f'''unknown warning category: {category!r}'''), None

        if not issubclass(cat, Warning):
            raise _OptionError(f'''invalid warning category: {category!r}''')
        return cat


def _is_internal_frame(frame):
