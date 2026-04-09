# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: loader.pyc (Python 3.11)

__all__ = [
    'BaseLoader',
    'FullLoader',
    'SafeLoader',
    'Loader',
    'UnsafeLoader']
from reader import *
from scanner import *
from parser import *
from composer import *
from constructor import *
from resolver import *

class BaseLoader(BaseResolver, BaseConstructor, Composer, Parser, Scanner, Reader):
    
    def __init__(self, stream):
        Reader.__init__(self, stream)
        Scanner.__init__(self)
        Parser.__init__(self)
        Composer.__init__(self)
        BaseConstructor.__init__(self)
        BaseResolver.__init__(self)



class FullLoader(Resolver, FullConstructor, Composer, Parser, Scanner, Reader):
    
    def __init__(self, stream):
        Reader.__init__(self, stream)
        Scanner.__init__(self)
        Parser.__init__(self)
        Composer.__init__(self)
        FullConstructor.__init__(self)
        Resolver.__init__(self)



class SafeLoader(Resolver, SafeConstructor, Composer, Parser, Scanner, Reader):
    
    def __init__(self, stream):
        Reader.__init__(self, stream)
        Scanner.__init__(self)
        Parser.__init__(self)
        Composer.__init__(self)
        SafeConstructor.__init__(self)
        Resolver.__init__(self)



class Loader(Resolver, Constructor, Composer, Parser, Scanner, Reader):
    
    def __init__(self, stream):
        Reader.__init__(self, stream)
        Scanner.__init__(self)
        Parser.__init__(self)
        Composer.__init__(self)
        Constructor.__init__(self)
        Resolver.__init__(self)



class UnsafeLoader(Resolver, Constructor, Composer, Parser, Scanner, Reader):
    
    def __init__(self, stream):
        Reader.__init__(self, stream)
        Scanner.__init__(self)
        Parser.__init__(self)
        Composer.__init__(self)
        Constructor.__init__(self)
        Resolver.__init__(self)
