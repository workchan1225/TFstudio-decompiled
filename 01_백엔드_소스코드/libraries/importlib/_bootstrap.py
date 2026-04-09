# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _bootstrap.pyc (Python 3.11)

'''Core implementation of import.

This module is NOT meant to be directly imported! It has been designed such
that it can be bootstrapped into Python as the implementation of import. As
such it requires the injection of specific modules and attributes in order to
work. One should use importlib as the public-facing version of this module.

'''

def _object_name(obj):
    
    try:
        return obj.__qualname__
    except AttributeError:
        return 


_thread = None
_warnings = None
_weakref = None
_bootstrap_external = None

def _wrap(new, old):
    '''Simple substitute for functools.update_wrapper.'''
    for replace in ('__module__', '__name__', '__qualname__', '__doc__'):
        if hasattr(old, replace):
            setattr(new, replace, getattr(old, replace))
        new.__dict__.update(old.__dict__)
        return None


def _new_module(name):
    return type(sys)(name)

_module_locks = { }
_blocking_on = { }

class _DeadlockError(RuntimeError):
    pass


class _ModuleLock:
    '''A recursive lock implementation which is able to detect deadlocks
    (e.g. thread 1 trying to take locks A then B, and thread 2 trying to
    take locks B then A).
    '''
    
    def __init__(self, name):
        self.lock = _thread.allocate_lock()
        self.wakeup = _thread.allocate_lock()
        self.name = name
        self.owner = None
        self.count = 0
        self.waiters = 0

    
    def has_deadlock(self):
        me = _thread.get_ident()
        tid = self.owner
        seen = set()
        lock = _blocking_on.get(tid)
    # WARNING: Decompyle incomplete

    
    def acquire(self):
        '''
        Acquire the module lock.  If a potential deadlock is detected,
        a _DeadlockError is raised.
        Otherwise, the lock is always acquired and True is returned.
        '''
        tid = _thread.get_ident()
        _blocking_on[tid] = self
        
        try:
            self.lock
            if self.count == 0 or self.owner == tid:
                self.owner = tid
                
                try:
                    None(None, None)
                    del _blocking_on[tid]
                    return True
                    if self.has_deadlock():
                        raise _DeadlockError('deadlock detected by %r' % self)
                    if self.wakeup.acquire(False):
                        
                        try:
                            None(None, None)
                        with None:
                            if not self, self.waiters += 1, .waiters:
                                
                                try:
                                    
                                    try:
                                        self, self.count += 1, .count
                                        self.wakeup.acquire()
                                        self.wakeup.release()
                                        continue
                                    except:
                                        del _blocking_on[tid]






    
    def release(self):
        tid = _thread.get_ident()
        self.lock
        if self.owner != tid:
            raise RuntimeError('cannot release un-acquired lock')
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return '_ModuleLock({!r}) at {}'.format(self.name, id(self))



class _DummyModuleLock:
    '''A simple _ModuleLock equivalent for Python builds without
    multi-threading support.'''
    
    def __init__(self, name):
        self.name = name
        self.count = 0

    
    def acquire(self):
        return True

    
    def release(self):
        if self.count == 0:
            raise RuntimeError('cannot release un-acquired lock')

    
    def __repr__(self):
        return '_DummyModuleLock({!r}) at {}'.format(self.name, id(self))



class _ModuleLockManager:
    
    def __init__(self, name):
        self._name = name
        self._lock = None

    
    def __enter__(self):
        self._lock = _get_module_lock(self._name)
        self._lock.acquire()

    
    def __exit__(self, *args, **kwargs):
        self._lock.release()



def _get_module_lock(name):
    '''Get or create the module lock for a given module name.

    Acquire/release internally the global import lock to protect
    _module_locks.'''
    _imp.acquire_lock()
# WARNING: Decompyle incomplete


def _lock_unlock_module(name):
    '''Acquires then releases the module lock for a given module name.

    This is used to ensure a module is completely initialized, in the
    event it is being imported by another thread.
    '''
    lock = _get_module_lock(name)
    
    try:
        lock.acquire()
        lock.release()
        return None
    except _DeadlockError:
        return None



def _call_with_frames_removed(f, *args, **kwds):
    '''remove_importlib_frames in import.c will always remove sequences
    of importlib frames that end with a call to this function

    Use it instead of a normal call in places where including the importlib
    frames introduces unwanted noise into the traceback (e.g. when executing
    module code)
    '''
    pass
# WARNING: Decompyle incomplete


def _verbose_message(message = None, *, verbosity, *args):
    '''Print the message to stderr if -v/PYTHONVERBOSE is turned on.'''
    pass
# WARNING: Decompyle incomplete


def _requires_builtin(fxn):
    '''Decorator to verify the named module is built-in.'''
    pass
# WARNING: Decompyle incomplete


def _requires_frozen(fxn):
    '''Decorator to verify the named module is frozen.'''
    pass
# WARNING: Decompyle incomplete


def _load_module_shim(self, fullname):
    '''Load the specified module into sys.modules and return it.

    This method is deprecated.  Use loader.exec_module() instead.

    '''
    msg = 'the load_module() method is deprecated and slated for removal in Python 3.12; use exec_module() instead'
    _warnings.warn(msg, DeprecationWarning)
    spec = spec_from_loader(fullname, self)
    if fullname in sys.modules:
        module = sys.modules[fullname]
        _exec(spec, module)
        return sys.modules[fullname]
    return None(spec)


def _module_repr(module):
    '''The implementation of ModuleType.__repr__().'''
    loader = getattr(module, '__loader__', None)
    spec = getattr(module, '__spec__', None)
    if getattr(module, '__spec__', None):
        return _module_repr_from_spec(spec)
# WARNING: Decompyle incomplete


class ModuleSpec:
    '''The specification for a module, used for loading.

    A module\'s spec is the source for information about the module.  For
    data associated with the module, including source, use the spec\'s
    loader.

    `name` is the absolute name of the module.  `loader` is the loader
    to use when loading the module.  `parent` is the name of the
    package the module is in.  The parent is derived from the name.

    `is_package` determines if the module is considered a package or
    not.  On modules this is reflected by the `__path__` attribute.

    `origin` is the specific location used by the loader from which to
    load the module, if that information is available.  When filename is
    set, origin will match.

    `has_location` indicates that a spec\'s "origin" reflects a location.
    When this is True, `__file__` attribute of the module is set.

    `cached` is the location of the cached bytecode file, if any.  It
    corresponds to the `__cached__` attribute.

    `submodule_search_locations` is the sequence of path entries to
    search when importing submodules.  If set, is_package should be
    True--and False otherwise.

    Packages are simply modules that (may) have submodules.  If a spec
    has a non-None value in `submodule_search_locations`, the import
    system will consider modules loaded from the spec as packages.

    Only finders (see importlib.abc.MetaPathFinder and
    importlib.abc.PathEntryFinder) should modify ModuleSpec instances.

    '''
    
    def __init__(self, name = None, loader = {
        'origin': None,
        'loader_state': None,
        'is_package': None }, *, origin, loader_state, is_package):
        self.name = name
        self.loader = loader
        self.origin = origin
        self.loader_state = loader_state
        self.submodule_search_locations = [] if is_package else None
        self._uninitialized_submodules = []
        self._set_fileattr = False
        self._cached = None

    
    def __repr__(self):
        args = [
            'name={!r}'.format(self.name),
            'loader={!r}'.format(self.loader)]
    # WARNING: Decompyle incomplete

    
    def __eq__(self, other):
        smsl = self.submodule_search_locations
        
        try:
            if self.name == other.name:
                if self.loader == other.loader:
                    if self.origin == other.origin:
                        if smsl == other.submodule_search_locations:
                            if self.cached == other.cached:
                                return self.has_location == other.has_location
                            except AttributeError:
                                return 


    cached = (lambda self: pass# WARNING: Decompyle incomplete
)()
    cached = (lambda self, cached: self._cached = cached)()
    parent = (lambda self: pass# WARNING: Decompyle incomplete
)()
    has_location = (lambda self: self._set_fileattr)()
    has_location = (lambda self, value: self._set_fileattr = bool(value))()


def spec_from_loader(name = None, loader = {
    'origin': None,
    'is_package': None }, *, origin, is_package):
    '''Return a module spec based on various loader methods.'''
    pass
# WARNING: Decompyle incomplete


def _spec_from_module(module, loader, origin = (None, None)):
    pass
# WARNING: Decompyle incomplete


def _init_module_attrs(spec = None, module = {
    'override': False }, *, override):
    pass
# WARNING: Decompyle incomplete


def module_from_spec(spec):
    '''Create a module based on the provided spec.'''
    module = None
    if hasattr(spec.loader, 'create_module'):
        module = spec.loader.create_module(spec)
    elif hasattr(spec.loader, 'exec_module'):
        raise ImportError('loaders that define exec_module() must also define create_module()')
# WARNING: Decompyle incomplete


def _module_repr_from_spec(spec):
    '''Return the repr to use for the module.'''
    pass
# WARNING: Decompyle incomplete


def _exec(spec, module):
    """Execute the spec's specified module in an existing module's namespace."""
    name = spec.name
    _ModuleLockManager(name)
    if sys.modules.get(name) is not module:
        msg = 'module {!r} not in sys.modules'.format(name)
        raise ImportError(msg, name = name)
# WARNING: Decompyle incomplete


def _load_backward_compatible(spec):
    
    try:
        spec.loader.load_module(spec.name)
    except:
        if spec.name in sys.modules:
            module = sys.modules.pop(spec.name)
            sys.modules[spec.name] = module
        raise 

    module = sys.modules.pop(spec.name)
    sys.modules[spec.name] = module
# WARNING: Decompyle incomplete


def _load_unlocked(spec):
    pass
# WARNING: Decompyle incomplete


def _load(spec):
    """Return a new module object, loaded by the spec's loader.

    The module is not added to its parent.

    If a module is already in sys.modules, that existing module gets
    clobbered.

    """
    _ModuleLockManager(spec.name)
    None(None, None)
    return 
    with None:
        if not None, _load_unlocked(spec):
            pass


class BuiltinImporter:
    '''Meta path import for built-in modules.

    All methods are either class or static methods to avoid the need to
    instantiate the class.

    '''
    _ORIGIN = 'built-in'
    module_repr = (lambda module: _warnings.warn('BuiltinImporter.module_repr() is deprecated and slated for removal in Python 3.12', DeprecationWarning)f'''<module {module.__name__!r} ({BuiltinImporter._ORIGIN})>''')()
    find_spec = (lambda cls, fullname, path, target = (None, None): if _imp.is_builtin(fullname):
spec_from_loader(fullname, cls, origin = cls._ORIGIN))()
    find_module = (lambda cls, fullname, path = (None,): _warnings.warn('BuiltinImporter.find_module() is deprecated and slated for removal in Python 3.12; use find_spec() instead', DeprecationWarning)spec = cls.find_spec(fullname, path)# WARNING: Decompyle incomplete
)()
    create_module = (lambda spec: if spec.name not in sys.builtin_module_names:
raise ImportError('{!r} is not a built-in module'.format(spec.name), name = spec.name)_call_with_frames_removed(_imp.create_builtin, spec))()
    exec_module = (lambda module: _call_with_frames_removed(_imp.exec_builtin, module))()
    get_code = (lambda cls, fullname: pass)()()
    get_source = (lambda cls, fullname: pass)()()
    is_package = (lambda cls, fullname: False)()()
    load_module = classmethod(_load_module_shim)


class FrozenImporter:
    '''Meta path import for frozen modules.

    All methods are either class or static methods to avoid the need to
    instantiate the class.

    '''
    _ORIGIN = 'frozen'
    module_repr = (lambda m: _warnings.warn('FrozenImporter.module_repr() is deprecated and slated for removal in Python 3.12', DeprecationWarning)'<module {!r} ({})>'.format(m.__name__, FrozenImporter._ORIGIN))()
    _fix_up_module = (lambda cls, module: spec = module.__spec__state = spec.loader_state# WARNING: Decompyle incomplete
)()
    _resolve_filename = (lambda cls, fullname, alias, ispkg = (None, False): if not fullname or getattr(sys, '_stdlib_dir', None):
(None, None)try:
sep = cls._SEPexcept AttributeError:
sep = '\\' if sys.platform == 'win32' else '/'cls._SEP = '\\' if sys.platform == 'win32' else '/'if fullname != alias:
if fullname.startswith('<'):
fullname = fullname[1:]if not ispkg:
fullname = f'''{fullname}.__init__'''else:
ispkg = Falserelfile = fullname.replace('.', sep)if ispkg:
pkgdir = f'''{sys._stdlib_dir}{sep}{relfile}'''filename = f'''{pkgdir}{sep}__init__.py'''else:
pkgdir = Nonefilename = f'''{sys._stdlib_dir}{sep}{relfile}.py'''(filename, pkgdir))()
    find_spec = (lambda cls, fullname, path, target = (None, None): info = _call_with_frames_removed(_imp.find_frozen, fullname)# WARNING: Decompyle incomplete
)()
    find_module = (lambda cls, fullname, path = (None,): _warnings.warn('FrozenImporter.find_module() is deprecated and slated for removal in Python 3.12; use find_spec() instead', DeprecationWarning)cls if _imp.is_frozen(fullname) else None)()
    create_module = (lambda spec:
