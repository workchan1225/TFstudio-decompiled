# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: repr.pyc (Python 3.11)

import inspect
from functools import partial
from typing import Any, Callable, Iterable, List, Optional, Tuple, Type, TypeVar, Union, overload
T = TypeVar('T')
Result = Iterable[Union[(Any, Tuple[Any], Tuple[(str, Any)], Tuple[(str, Any, Any)])]]
RichReprResult = Result

class ReprError(Exception):
    '''An error occurred when attempting to build a repr.'''
    pass

auto = (lambda cls = None: pass)()
auto = (lambda *: pass)()

def auto(cls = None, *, angular):
    '''Class decorator to create __repr__ from __rich_repr__'''
    
    def do_replace(cls = None, angular = None):
        
        def auto_repr(self = None):
            '''Create repr string from __rich_repr__'''
            repr_str = []
            append = repr_str.append
            angular = getattr(self.__rich_repr__, 'angular', False)
        # WARNING: Decompyle incomplete

        
        def auto_rich_repr(self = None):
            '''Auto generate __rich_rep__ from signature of __init__'''
            pass
        # WARNING: Decompyle incomplete

        if not hasattr(cls, '__rich_repr__'):
            auto_rich_repr.__doc__ = 'Build a rich repr'
            cls.__rich_repr__ = auto_rich_repr
        auto_repr.__doc__ = 'Return repr(self)'
        cls.__repr__ = auto_repr
    # WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete

rich_repr = (lambda cls = None: pass)()
rich_repr = (lambda *: pass)()

def rich_repr(cls = None, *, angular):
    pass
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    Foo = <NODE:12>()
    foo = Foo()
    from rich.console import Console
    console = Console()
    console.rule('Standard repr')
    console.print(foo)
    console.print(foo, width = 60)
    console.print(foo, width = 30)
    console.rule('Angular repr')
    Foo.__rich_repr__.angular = True
    console.print(foo)
    console.print(foo, width = 60)
    console.print(foo, width = 30)
    return None
