# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: extbuild.pyc (Python 3.11)

'''
Build a c-extension module on-the-fly in tests.
See build_and_import_extensions for usage hints

'''
import os
import pathlib
import subprocess
import sys
import sysconfig
import textwrap
__all__ = [
    'build_and_import_extension',
    'compile_extension_module']

def build_and_import_extension(modname = None, functions = {
    'prologue': '',
    'build_dir': None,
    'include_dirs': [],
    'more_init': '' }, *, prologue, build_dir, include_dirs, more_init):
    '''
    Build and imports a c-extension module `modname` from a list of function
    fragments `functions`.


    Parameters
    ----------
    functions : list of fragments
        Each fragment is a sequence of func_name, calling convention, snippet.
    prologue : string
        Code to precede the rest, usually extra ``#include`` or ``#define``
        macros.
    build_dir : pathlib.Path
        Where to build the module, usually a temporary directory
    include_dirs : list
        Extra directories to find include files when compiling
    more_init : string
        Code to appear in the module PyMODINIT_FUNC

    Returns
    -------
    out: module
        The module will have been loaded and is ready for use

    Examples
    --------
    >>> functions = [("test_bytes", "METH_O", """
        if ( !PyBytesCheck(args)) {
            Py_RETURN_FALSE;
        }
        Py_RETURN_TRUE;
    """)]
    >>> mod = build_and_import_extension("testme", functions)
    >>> assert not mod.test_bytes(u\'abc\')
    >>> assert mod.test_bytes(b\'abc\')
    '''
    body = prologue + _make_methods(functions, modname)
    init = 'PyObject *mod = PyModule_Create(&moduledef);\n           '
    if not build_dir:
        build_dir = pathlib.Path('.')
    if more_init:
        init += '#define INITERROR return NULL\n                '
        init += more_init
    init += '\nreturn mod;'
    source_string = _make_source(modname, init, body)
    
    try:
        mod_so = compile_extension_module(modname, build_dir, include_dirs, source_string)
    except Exception:
        e = None
        raise RuntimeError(f'''could not compile in {build_dir}:'''), e
        e = None
        del e

    import importlib.util as importlib
    spec = importlib.util.spec_from_file_location(modname, mod_so)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo


def compile_extension_module(name, builddir, include_dirs, source_string, libraries, library_dirs = ([], [])):
    '''
    Build an extension module and return the filename of the resulting
    native code file.

    Parameters
    ----------
    name : string
        name of the module, possibly including dots if it is a module inside a
        package.
    builddir : pathlib.Path
        Where to build the module, usually a temporary directory
    include_dirs : list
        Extra directories to find include files when compiling
    libraries : list
        Libraries to link into the extension module
    library_dirs: list
        Where to find the libraries, ``-L`` passed to the linker
    '''
    modname = name.split('.')[-1]
    dirname = builddir / name
    dirname.mkdir(exist_ok = True)
    cfile = _convert_str_to_file(source_string, dirname)
    include_dirs = include_dirs + [
        sysconfig.get_config_var('INCLUDEPY')]
    return _c_compile(cfile, outputfilename = dirname / modname, include_dirs = include_dirs, libraries = [], library_dirs = [])


def _convert_str_to_file(source, dirname):
    '''Helper function to create a file ``source.c`` in `dirname` that contains
    the string in `source`. Returns the file name
    '''
    filename = dirname / 'source.c'
    f = filename.open('w')
    f.write(str(source))
    None(None, None)


def _make_methods(functions, modname):
    ''' Turns the name, signature, code in functions into complete functions
    and lists them in a methods_table. Then turns the methods_table into a
    ``PyMethodDef`` structure and returns the resulting code fragment ready
    for compilation
    '''
    methods_table = []
    codes = []
    for funcname, flags, code in functions:
        cfuncname = f'''{modname!s}_{funcname!s}'''
        if 'METH_KEYWORDS' in flags:
            signature = '(PyObject *self, PyObject *args, PyObject *kwargs)'
        else:
            signature = '(PyObject *self, PyObject *args)'
        methods_table.append(f'''{{"{funcname!s}", (PyCFunction){cfuncname!s}, {flags!s}}},''')
        func_code = '\n        static PyObject* {cfuncname}{signature}\n        {{\n        {code}\n        }}\n        '.format(cfuncname = cfuncname, signature = signature, code = code)
        codes.append(func_code)
        body = '\n'.join(codes) + '\n    static PyMethodDef methods[] = {\n    %(methods)s\n    { NULL }\n    };\n    static struct PyModuleDef moduledef = {\n        PyModuleDef_HEAD_INIT,\n        "%(modname)s",  /* m_name */\n        NULL,           /* m_doc */\n        -1,             /* m_size */\n        methods,        /* m_methods */\n    };\n    ' % dict(methods = '\n'.join(methods_table), modname = modname)
        return body


def _make_source(name, init, body):
    ''' Combines the code fragments into source code ready to be compiled
    '''
    code = '\n    #include <Python.h>\n\n    %(body)s\n\n    PyMODINIT_FUNC\n    PyInit_%(name)s(void) {\n    %(init)s\n    }\n    ' % dict(name = name, init = init, body = body)
    return code


def _c_compile(cfile, outputfilename, include_dirs, libraries, library_dirs = ([], [], [])):
    if sys.platform == 'win32':
        compile_extra = [
            '/we4013']
        link_extra = [
            '/LIBPATH:' + os.path.join(sys.base_prefix, 'libs')]
    elif sys.platform.startswith('linux'):
        compile_extra = [
            '-O0',
            '-g',
            '-Werror=implicit-function-declaration',
            '-fPIC']
        link_extra = []
    else:
        compile_extra = []
        link_extra = []
    if sys.platform == 'win32':
        link_extra = link_extra + [
            '/DEBUG']
    if sys.platform == 'darwin':
        for s in ('/sw/', '/opt/local/'):
            if s + 'include' not in include_dirs and os.path.exists(s + 'include'):
                include_dirs.append(s + 'include')
            if s + 'lib' not in library_dirs and os.path.exists(s + 'lib'):
                library_dirs.append(s + 'lib')
            outputfilename = outputfilename.with_suffix(get_so_suffix())
            build(cfile, outputfilename, compile_extra, link_extra, include_dirs, libraries, library_dirs)
            return outputfilename


def build(cfile, outputfilename, compile_extra, link_extra, include_dirs, libraries, library_dirs):
    '''use meson to build'''
    build_dir = cfile.parent / 'build'
    os.makedirs(build_dir, exist_ok = True)
    so_name = outputfilename.parts[-1]
    fid = open(cfile.parent / 'meson.build', 'wt')
    includes = include_dirs()
    link_dirs = library_dirs()
    fid.write(textwrap.dedent(f'''            project(\'foo\', \'c\')\n            shared_module(\'{so_name}\', \'{cfile.parts[-1]}\',\n                c_args: {includes} + {compile_extra},\n                link_args: {link_dirs} + {link_extra},\n                link_with: {libraries},\n                name_prefix: \'\',\n                name_suffix: \'dummy\',\n            )\n        '''))
    None(None, None)


def get_so_suffix():
    ret = sysconfig.get_config_var('EXT_SUFFIX')
# WARNING: Decompyle incomplete
