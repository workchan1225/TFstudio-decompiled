# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _namespace_utils.pyc (Python 3.11)

from __future__ import annotations
import sys
from collections.abc import Generator, Iterator, Mapping
from contextlib import contextmanager
from functools import cached_property
from typing import Any, Callable, NamedTuple, TypeVar
from typing_extensions import ParamSpec, TypeAlias, TypeAliasType, TypeVarTuple
GlobalsNamespace: 'TypeAlias' = 'dict[str, Any]'
MappingNamespace: 'TypeAlias' = Mapping[(str, Any)]
_TypeVarLike: 'TypeAlias' = 'TypeVar | ParamSpec | TypeVarTuple'

class NamespacesTuple(NamedTuple):
    locals: 'MappingNamespace' = 'A tuple of globals and locals to be used during annotations evaluation.\n\n    This datastructure is defined as a named tuple so that it can easily be unpacked:\n\n    ```python {lint="skip" test="skip"}\n    def eval_type(typ: type[Any], ns: NamespacesTuple) -> None:\n        return eval(typ, *ns)\n    ```\n    '


def get_module_ns_of(obj = None):
    '''Get the namespace of the module where the object is defined.

    Caution: this function does not return a copy of the module namespace, so the result
    should not be mutated. The burden of enforcing this is on the caller.
    '''
    module_name = getattr(obj, '__module__', None)
    if module_name:
        
        try:
            return sys.modules[module_name].__dict__
        except KeyError:
            return 
            return { }



def LazyLocalNamespace():
    '''LazyLocalNamespace'''
    __doc__ = 'A lazily evaluated mapping, to be used as the `locals` argument during annotations evaluation.\n\n    While the [`eval`][eval] function expects a mapping as the `locals` argument, it only\n    performs `__getitem__` calls. The [`Mapping`][collections.abc.Mapping] abstract base class\n    is fully implemented only for type checking purposes.\n\n    Args:\n        *namespaces: The namespaces to consider, in ascending order of priority.\n\n    Example:\n        ```python {lint="skip" test="skip"}\n        ns = LazyLocalNamespace({\'a\': 1, \'b\': 2}, {\'a\': 3})\n        ns[\'a\']\n        #> 3\n        ns[\'b\']\n        #> 2\n        ```\n    '
    
    def __init__(self = None, *namespaces):
        self._namespaces = namespaces

    data = (lambda self = None: self._namespaces())()
    
    def __len__(self = None):
        return len(self.data)

    
    def __getitem__(self = None, key = None):
        return self.data[key]

    
    def __contains__(self = None, key = None):
        return key in self.data

    
    def __iter__(self = None):
        return iter(self.data)


LazyLocalNamespace = <NODE:27>(LazyLocalNamespace, 'LazyLocalNamespace', Mapping[(str, Any)])

def ns_for_function(obj = None, parent_namespace = None):
    '''Return the global and local namespaces to be used when evaluating annotations for the provided function.

    The global namespace will be the `__dict__` attribute of the module the function was defined in.
    The local namespace will contain the `__type_params__` introduced by PEP 695.

    Args:
        obj: The object to use when building namespaces.
        parent_namespace: Optional namespace to be added with the lowest priority in the local namespace.
            If the passed function is a method, the `parent_namespace` will be the namespace of the class
            the method is defined in. Thus, we also fetch type `__type_params__` from there (i.e. the
            class-scoped type variables).
    '''
    locals_list = []
# WARNING: Decompyle incomplete


class NsResolver:
    '''A class responsible for the namespaces resolving logic for annotations evaluation.

    This class handles the namespace logic when evaluating annotations mainly for class objects.

    It holds a stack of classes that are being inspected during the core schema building,
    and the `types_namespace` property exposes the globals and locals to be used for
    type annotation evaluation. Additionally -- if no class is present in the stack -- a
    fallback globals and locals can be provided using the `namespaces_tuple` argument
    (this is useful when generating a schema for a simple annotation, e.g. when using
    `TypeAdapter`).

    The namespace creation logic is unfortunately flawed in some cases, for backwards
    compatibility reasons and to better support valid edge cases. See the description
    for the `parent_namespace` argument and the example for more details.

    Args:
        namespaces_tuple: The default globals and locals to use if no class is present
            on the stack. This can be useful when using the `GenerateSchema` class
            with `TypeAdapter`, where the "type" being analyzed is a simple annotation.
        parent_namespace: An optional parent namespace that will be added to the locals
            with the lowest priority. For a given class defined in a function, the locals
            of this function are usually used as the parent namespace:

            ```python {lint="skip" test="skip"}
            from pydantic import BaseModel

            def func() -> None:
                SomeType = int

                class Model(BaseModel):
                    f: \'SomeType\'

                # when collecting fields, an namespace resolver instance will be created
                # this way:
                # ns_resolver = NsResolver(parent_namespace={\'SomeType\': SomeType})
            ```

            For backwards compatibility reasons and to support valid edge cases, this parent
            namespace will be used for *every* type being pushed to the stack. In the future,
            we might want to be smarter by only doing so when the type being pushed is defined
            in the same module as the parent namespace.

    Example:
        ```python {lint="skip" test="skip"}
        ns_resolver = NsResolver(
            parent_namespace={\'fallback\': 1},
        )

        class Sub:
            m: \'Model\'

        class Model:
            some_local = 1
            sub: Sub

        ns_resolver = NsResolver()

        # This is roughly what happens when we build a core schema for `Model`:
        with ns_resolver.push(Model):
            ns_resolver.types_namespace
            #> NamespacesTuple({\'Sub\': Sub}, {\'Model\': Model, \'some_local\': 1})
            # First thing to notice here, the model being pushed is added to the locals.
            # Because `NsResolver` is being used during the model definition, it is not
            # yet added to the globals. This is useful when resolving self-referencing annotations.

            with ns_resolver.push(Sub):
                ns_resolver.types_namespace
                #> NamespacesTuple({\'Sub\': Sub}, {\'Sub\': Sub, \'Model\': Model})
                # Second thing to notice: `Sub` is present in both the globals and locals.
                # This is not an issue, just that as described above, the model being pushed
                # is added to the locals, but it happens to be present in the globals as well
                # because it is already defined.
                # Third thing to notice: `Model` is also added in locals. This is a backwards
                # compatibility workaround that allows for `Sub` to be able to resolve `\'Model\'`
                # correctly (as otherwise models would have to be rebuilt even though this
                # doesn\'t look necessary).
        ```
    '''
    
    def __init__(self = None, namespaces_tuple = None, parent_namespace = None):
        if not namespaces_tuple:
            pass
        self._base_ns_tuple = NamespacesTuple({ }, { })
        self._parent_ns = parent_namespace
        self._types_stack = []

    types_namespace = (lambda self = None: if not self._types_stack:
self._base_ns_tupletyp = None._types_stack[-1]globalns = get_module_ns_of(typ)locals_list = []# WARNING: Decompyle incomplete
)()
    push = (lambda self = None, typ = None: pass# WARNING: Decompyle incomplete
)()
