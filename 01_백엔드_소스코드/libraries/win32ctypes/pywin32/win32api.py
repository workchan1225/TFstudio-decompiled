# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: win32api.pyc (Python 3.11)

''' A module, encapsulating the Windows Win32 API. '''
from win32ctypes.core import _common, _dll, _resource, _system_information, _backend, _time
from win32ctypes.pywin32.pywintypes import pywin32error as _pywin32error
LOAD_LIBRARY_AS_DATAFILE = 2
LANG_NEUTRAL = 0

def LoadLibraryEx(fileName, handle, flags):
    ''' Loads the specified DLL, and returns the handle.

    Parameters
    ----------
    fileName : unicode
        The filename of the module to load.

    handle : int
        Reserved, always zero.

    flags : int
        The action to be taken when loading the module.

    Returns
    -------
    handle : hModule
        The handle of the loaded module

    '''
    if not handle == 0:
        raise ValueError('handle != 0 not supported')
    _pywin32error()
    None(None, None)
    return 
    with None:
        if not None, _dll._LoadLibraryEx(fileName, 0, flags):
            pass


def EnumResourceTypes(hModule):
    ''' Enumerates resource types within a module.

    Parameters
    ----------
    hModule : handle
        The handle to the module.

    Returns
    -------
    resource_types : list
       The list of resource types in the module.

    '''
    pass
# WARNING: Decompyle incomplete


def EnumResourceNames(hModule, resType):
    ''' Enumerates all the resources of the specified type within a module.

    Parameters
    ----------
    hModule : handle
        The handle to the module.
    resType : str : int
        The type or id of resource to enumerate.

    Returns
    -------
    resource_names : list
       The list of resource names (unicode strings) of the specific
       resource type in the module.

    '''
    pass
# WARNING: Decompyle incomplete


def EnumResourceLanguages(hModule, lpType, lpName):
    ''' List languages of a resource module.

    Parameters
    ----------
    hModule : handle
        Handle to the resource module.

    lpType : str : int
        The type or id of resource to enumerate.

    lpName : str : int
        The type or id of resource to enumerate.

    Returns
    -------
    resource_languages : list
        List of the resource language ids.

    '''
    pass
# WARNING: Decompyle incomplete


def LoadResource(hModule, type, name, language = (LANG_NEUTRAL,)):
    ''' Find and Load a resource component.

    Parameters
    ----------
    handle : hModule
        The handle of the module containing the resource.
        Use None for current process executable.

    type : str : int
        The type of resource to load.

    name : str : int
        The name or Id of the resource to load.

    language : int
        Language to use, default is LANG_NEUTRAL.

    Returns
    -------
    resource : bytes
        The byte string blob of the resource

    '''
    _pywin32error()
    hrsrc = _resource._FindResourceEx(hModule, type, name, language)
    size = _resource._SizeofResource(hModule, hrsrc)
    hglob = _resource._LoadResource(hModule, hrsrc)
    if _backend == 'ctypes':
        pointer = _common.cast(_resource._LockResource(hglob), _common.c_char_p)
    else:
        pointer = _resource._LockResource(hglob)
    None(None, None)
    return 
    with None:
        if not None, _common._PyBytes_FromStringAndSize(pointer, size):
            pass


def FreeLibrary(hModule):
    ''' Free the loaded dynamic-link library (DLL) module.

    If necessary, decrements its reference count.

    Parameters
    ----------
    handle : hModule
        The handle to the library as returned by the LoadLibrary function.

    '''
    _pywin32error()
    None(None, None)
    return 
    with None:
        if not None, _dll._FreeLibrary(hModule):
            pass


def GetTickCount():
    ''' The number of milliseconds that have elapsed since startup

    Returns
    -------
    counts : int
        The millisecond counts since system startup.
    '''
    return _time._GetTickCount()


def BeginUpdateResource(filename, delete):
    ''' Get a handle that can be used by the :func:`UpdateResource`.

    Parameters
    ----------
    fileName : unicode
        The filename of the module to load.
    delete : bool
        When true all existing resources are deleted

    Returns
    -------
    result : hModule
        Handle of the resource.

    '''
    _pywin32error()
    None(None, None)
    return 
    with None:
        if not None, _resource._BeginUpdateResource(filename, delete):
            pass


def EndUpdateResource(handle, discard):
    ''' End the update resource of the handle.

    Parameters
    ----------
    handle : hModule
        The handle of the resource as it is returned
        by :func:`BeginUpdateResource`

    discard : bool
        When True all writes are discarded.

    '''
    _pywin32error()
    _resource._EndUpdateResource(handle, discard)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def UpdateResource(handle, type, name, data, language = (LANG_NEUTRAL,)):
    ''' Update a resource.

    Parameters
    ----------
    handle : hModule
        The handle of the resource file as returned by
        :func:`BeginUpdateResource`.

    type : str : int
        The type of resource to update.

    name : str : int
        The name or Id of the resource to update.

    data : bytes
        A bytes like object is expected.

        .. note::
          PyWin32 version 219, on Python 2.7, can handle unicode inputs.
          However, the data are stored as bytes and it is not really
          possible to convert the information back into the original
          unicode string. To be consistent with the Python 3 behaviour
          of PyWin32, we raise an error if the input cannot be
          converted to `bytes`.

    language : int
        Language to use, default is LANG_NEUTRAL.

    '''
    _pywin32error()
    lp_data = bytes(data)


def GetWindowsDirectory():
    ''' Get the ``Windows`` directory.

    Returns
    -------
    result : str
        The path to the ``Windows`` directory.

    '''
    _pywin32error()
    None(None, None)
    return 
    with None:
        if not None, str(_system_information._GetWindowsDirectory()):
            pass


def GetSystemDirectory():
    ''' Get the ``System`` directory.

    Returns
    -------
    result : str
        The path to the ``System`` directory.

    '''
    _pywin32error()
    None(None, None)
    return 
    with None:
        if not None, str(_system_information._GetSystemDirectory()):
            pass
