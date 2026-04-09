# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: loaders.pyc (Python 3.11)

'''API and implementations for loading templates from different data
sources.
'''
import importlib.util as importlib
import os
import posixpath
import sys
import typing as t
import weakref
import zipimport
from collections import abc
from hashlib import sha1
from importlib import import_module
from types import ModuleType
from exceptions import TemplateNotFound
from utils import internalcode
if t.TYPE_CHECKING:
    from environment import Environment
    from environment import Template

def split_template_path(template = None):
    """Split a path into segments and perform a sanity check.  If it detects
    '..' in the path it will raise a `TemplateNotFound` error.
    """
    pieces = []
    for piece in template.split('/'):
        if not os.path.sep in piece:
            if os.path.altsep or os.path.altsep in piece or piece == os.path.pardir:
                raise TemplateNotFound(template)
            if piece and piece != '.':
                pieces.append(piece)
        return pieces


class BaseLoader:
    """Baseclass for all loaders.  Subclass this and override `get_source` to
    implement a custom loading mechanism.  The environment provides a
    `get_template` method that calls the loader's `load` method to get the
    :class:`Template` object.

    A very basic example for a loader that looks up templates on the file
    system could look like this::

        from jinja2 import BaseLoader, TemplateNotFound
        from os.path import join, exists, getmtime

        class MyLoader(BaseLoader):

            def __init__(self, path):
                self.path = path

            def get_source(self, environment, template):
                path = join(self.path, template)
                if not exists(path):
                    raise TemplateNotFound(template)
                mtime = getmtime(path)
                with open(path) as f:
                    source = f.read()
                return source, path, lambda: mtime == getmtime(path)
    """
    has_source_access = True
    
    def get_source(self = None, environment = None, template = None):
        """Get the template source, filename and reload helper for a template.
        It's passed the environment and template name and has to return a
        tuple in the form ``(source, filename, uptodate)`` or raise a
        `TemplateNotFound` error if it can't locate the template.

        The source part of the returned tuple must be the source of the
        template as a string. The filename should be the name of the
        file on the filesystem if it was loaded from there, otherwise
        ``None``. The filename is used by Python for the tracebacks
        if no loader extension is used.

        The last item in the tuple is the `uptodate` function.  If auto
        reloading is enabled it's always called to check if the template
        changed.  No arguments are passed so the function must store the
        old state somewhere (for example in a closure).  If it returns `False`
        the template will be reloaded.
        """
        if not self.has_source_access:
            raise RuntimeError(f'''{type(self).__name__} cannot provide access to the source''')
        raise TemplateNotFound(template)

    
    def list_templates(self = None):
        '''Iterates over all templates.  If the loader does not support that
        it should raise a :exc:`TypeError` which is the default behavior.
        '''
        raise TypeError('this loader cannot iterate over all templates')

    load = (lambda self = None, environment = None, name = internalcode, globals = (None,): code = None# WARNING: Decompyle incomplete
)()


class FileSystemLoader(BaseLoader):
    '''Load templates from a directory in the file system.

    The path can be relative or absolute. Relative paths are relative to
    the current working directory.

    .. code-block:: python

        loader = FileSystemLoader("templates")

    A list of paths can be given. The directories will be searched in
    order, stopping at the first matching template.

    .. code-block:: python

        loader = FileSystemLoader(["/override/templates", "/default/templates"])

    :param searchpath: A path, or list of paths, to the directory that
        contains the templates.
    :param encoding: Use this encoding to read the text from template
        files.
    :param followlinks: Follow symbolic links in the path.

    .. versionchanged:: 2.8
        Added the ``followlinks`` parameter.
    '''
    
    def __init__(self = None, searchpath = None, encoding = None, followlinks = ('utf-8', False)):
        if isinstance(searchpath, abc.Iterable) or isinstance(searchpath, str):
            searchpath = [
                searchpath]
        self.searchpath = searchpath()
        self.encoding = encoding
        self.followlinks = followlinks

    
    def get_source(self = None, environment = None, template = None):
        pass
    # WARNING: Decompyle incomplete

    
    def list_templates(self = None):
        found = set()
        for searchpath in self.searchpath:
            walk_dir = os.walk(searchpath, followlinks = self.followlinks)
            for dirpath, _, filenames in walk_dir:
                for filename in filenames:
                    template = os.path.join(dirpath, filename)[len(searchpath):].strip(os.path.sep).replace(os.path.sep, '/')
                    if template[:2] == './':
                        template = template[2:]
                    if template not in found:
                        found.add(template)
                    return sorted(found)


if sys.version_info >= (3, 13):
    
    def _get_zipimporter_files(z = None):
        
        try:
            get_files = z._get_files
        except AttributeError:
            e = None
            raise TypeError('This zip import does not have the required metadata to list templates.'), e
            e = None
            del e

        return get_files()

else:
    
    def _get_zipimporter_files(z = None):
        
        try:
            files = z._files
        except AttributeError:
            e = None
            raise TypeError('This zip import does not have the required metadata to list templates.'), e
            e = None
            del e

        return files


class PackageLoader(BaseLoader):
    '''Load templates from a directory in a Python package.

    :param package_name: Import name of the package that contains the
        template directory.
    :param package_path: Directory within the imported package that
        contains the templates.
    :param encoding: Encoding of template files.

    The following example looks up templates in the ``pages`` directory
    within the ``project.ui`` package.

    .. code-block:: python

        loader = PackageLoader("project.ui", "pages")

    Only packages installed as directories (standard pip behavior) or
    zip/egg files (less common) are supported. The Python API for
    introspecting data in packages is too limited to support other
    installation methods the way this loader requires.

    There is limited support for :pep:`420` namespace packages. The
    template directory is assumed to only be in one namespace
    contributor. Zip files contributing to a namespace are not
    supported.

    .. versionchanged:: 3.0
        No longer uses ``setuptools`` as a dependency.

    .. versionchanged:: 3.0
        Limited PEP 420 namespace package support.
    '''
    
    def __init__(self = None, package_name = None, package_path = None, encoding = ('templates', 'utf-8')):
        package_path = os.path.normpath(package_path).rstrip(os.path.sep)
        if package_path == os.path.curdir:
            package_path = ''
        elif package_path[:2] == os.path.curdir + os.path.sep:
            package_path = package_path[2:]
        self.package_path = package_path
        self.package_name = package_name
        self.encoding = encoding
        import_module(package_name)
        spec = importlib.util.find_spec(package_name)
    # WARNING: Decompyle incomplete

    
    def get_source(self = None, environment = None, template = None):
        pass
    # WARNING: Decompyle incomplete

    
    def list_templates(self = None):
        pass
    # WARNING: Decompyle incomplete



class DictLoader(BaseLoader):
    """Loads a template from a Python dict mapping template names to
    template source.  This loader is useful for unittesting:

    >>> loader = DictLoader({'index.html': 'source here'})

    Because auto reloading is rarely useful this is disabled by default.
    """
    
    def __init__(self = None, mapping = None):
        self.mapping = mapping

    
    def get_source(self = None, environment = None, template = None):
        pass
    # WARNING: Decompyle incomplete

    
    def list_templates(self = None):
        return sorted(self.mapping)



class FunctionLoader(BaseLoader):
    """A loader that is passed a function which does the loading.  The
    function receives the name of the template and has to return either
    a string with the template source, a tuple in the form ``(source,
    filename, uptodatefunc)`` or `None` if the template does not exist.

    >>> def load_template(name):
    ...     if name == 'index.html':
    ...         return '...'
    ...
    >>> loader = FunctionLoader(load_template)

    The `uptodatefunc` is a function that is called if autoreload is enabled
    and has to return `True` if the template is still up to date.  For more
    details have a look at :meth:`BaseLoader.get_source` which has the same
    return value.
    """
    
    def __init__(self = None, load_func = None):
        self.load_func = load_func

    
    def get_source(self = None, environment = None, template = None):
        rv = self.load_func(template)
    # WARNING: Decompyle incomplete



class PrefixLoader(BaseLoader):
    """A loader that is passed a dict of loaders where each loader is bound
    to a prefix.  The prefix is delimited from the template by a slash per
    default, which can be changed by setting the `delimiter` argument to
    something else::

        loader = PrefixLoader({
            'app1':     PackageLoader('mypackage.app1'),
            'app2':     PackageLoader('mypackage.app2')
        })

    By loading ``'app1/index.html'`` the file from the app1 package is loaded,
    by loading ``'app2/index.html'`` the file from the second.
    """
    
    def __init__(self = None, mapping = None, delimiter = None):
        self.mapping = mapping
        self.delimiter = delimiter

    
    def get_loader(self = None, template = None):
        
        try:
            (prefix, name) = template.split(self.delimiter, 1)
            loader = self.mapping[prefix]
        except (ValueError, KeyError):
            e = None
            raise TemplateNotFound(template), e
            e = None
            del e

        return (loader, name)

    
    def get_source(self = None, environment = None, template = None):
        (loader, name) = self.get_loader(template)
        
        try:
            return loader.get_source(environment, name)
        except TemplateNotFound:
            e = None
            raise TemplateNotFound(template), e
            e = None
            del e


    load = (lambda self = None, environment = None, name = internalcode, globals = (None,): (loader, local_name) = self.get_loader(name)try:
loader.load(environment, local_name, globals)except TemplateNotFound:
e = Noneraise TemplateNotFound(name), ee = Nonedel e)()
    
    def list_templates(self = None):
        result = []
        for prefix, loader in self.mapping.items():
            for template in loader.list_templates():
                result.append(prefix + self.delimiter + template)
                return result



class ChoiceLoader(BaseLoader):
    """This loader works like the `PrefixLoader` just that no prefix is
    specified.  If a template could not be found by one loader the next one
    is tried.

    >>> loader = ChoiceLoader([
    ...     FileSystemLoader('/path/to/user/templates'),
    ...     FileSystemLoader('/path/to/system/templates')
    ... ])

    This is useful if you want to allow users to override builtin templates
    from a different location.
    """
    
    def __init__(self = None, loaders = None):
        self.loaders = loaders

    
    def get_source(self = None, environment = None, template = None):
        for loader in self.loaders:
            
            return None, loader.get_source(environment, template)
            except TemplateNotFound:
                continue
            raise TemplateNotFound(template)

    load = (lambda self = None, environment = None, name = internalcode, globals = (None,): for loader in self.loaders:
None, loader.load(environment, name, globals)except TemplateNotFound:
continueraise TemplateNotFound(name))()
    
    def list_templates(self = None):
        found = set()
        for loader in self.loaders:
            found.update(loader.list_templates())
            return sorted(found)



class _TemplateModule(ModuleType):
    '''Like a normal module but with support for weak references'''
    pass


class ModuleLoader(BaseLoader):
    """This loader loads templates from precompiled templates.

    Example usage:

    >>> loader = ModuleLoader('/path/to/compiled/templates')

    Templates can be precompiled with :meth:`Environment.compile_templates`.
    """
    has_source_access = False
    
    def __init__(self = None, path = None):
        pass
    # WARNING: Decompyle incomplete

    get_template_key = (lambda name = None: 'tmpl_' + sha1(name.encode('utf-8')).hexdigest())()
    get_module_filename = (lambda name = None: ModuleLoader.get_template_key(name) + '.py')()
    load = (lambda self = None, environment = None, name = internalcode, globals = (None,): key = self.get_template_key(name)module = f'''{self.package_name}.{key}'''mod = getattr(self.module, module, None)# WARNING: Decompyle incomplete
)()
