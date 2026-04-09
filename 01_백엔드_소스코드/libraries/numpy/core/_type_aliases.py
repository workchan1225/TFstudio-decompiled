# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _type_aliases.pyc (Python 3.11)

'''
Due to compatibility, numpy has a very large number of different naming
conventions for the scalar types (those subclassing from `numpy.generic`).
This file produces a convoluted set of dictionaries mapping names to types,
and sometimes other mappings too.

.. data:: allTypes
    A dictionary of names to types that will be exposed as attributes through
    ``np.core.numerictypes.*``

.. data:: sctypeDict
    Similar to `allTypes`, but maps a broader set of aliases to their types.

.. data:: sctypes
    A dictionary keyed by a "type group" string, providing a list of types
    under that group.

'''
from numpy.compat import unicode
from numpy.core._string_helpers import english_lower
from numpy.core.multiarray import typeinfo, dtype
from numpy.core._dtype import _kind_name
sctypeDict = { }
allTypes = { }
_abstract_types = { }
_concrete_typeinfo = { }
for k, v in typeinfo.items():
    k = english_lower(k)
    if isinstance(v, type):
        _abstract_types[k] = v
        continue
    _concrete_typeinfo[k] = v
    _concrete_types = _concrete_typeinfo.items()()
    
    def _bits_of(obj):
        pass
    # WARNING: Decompyle incomplete

    
    def bitname(obj):
        '''Return a bit-width name for a given type object'''
        bits = _bits_of(obj)
        dt = dtype(obj)
        char = dt.kind
        base = _kind_name(dt)
        if base == 'object':
            bits = 0
        if bits != 0:
            char = '%s%d' % (char, bits // 8)
        return (base, bits, char)

    
    def _add_types():
        for name, info in _concrete_typeinfo.items():
            allTypes[name] = info.type
            sctypeDict[name] = info.type
            sctypeDict[info.char] = info.type
            sctypeDict[info.num] = info.type
            for name, cls in _abstract_types.items():
                allTypes[name] = cls
                return None

    _add_types()
    _int_ctypes = [
        'long',
        'longlong',
        'int',
        'short',
        'byte']
    _uint_ctypes = (lambda .0: pass# WARNING: Decompyle incomplete
)(_int_ctypes())
    
    def _add_aliases():
        for name, info in _concrete_typeinfo.items():
            if name in _int_ctypes or name in _uint_ctypes:
                continue
            (base, bit, char) = bitname(info.type)
            myname = '%s%d' % (base, bit)
            if name in ('longdouble', 'clongdouble') and myname in allTypes:
                continue
            if bit != 0 and base != 'bool':
                allTypes[myname] = info.type
            sctypeDict[char] = info.type
            sctypeDict[myname] = info.type
            return None

    _add_aliases()
    
    def _add_integer_aliases():
        seen_bits = set()
        for i_ctype, u_ctype in zip(_int_ctypes, _uint_ctypes):
            i_info = _concrete_typeinfo[i_ctype]
            u_info = _concrete_typeinfo[u_ctype]
            bits = i_info.bits
            for info, charname, intname in ((i_info, 'i%d' % (bits // 8,), 'int%d' % bits), (u_info, 'u%d' % (bits // 8,), 'uint%d' % bits)):
                if bits not in seen_bits:
                    allTypes[intname] = info.type
                    sctypeDict[intname] = info.type
                    sctypeDict[charname] = info.type
                seen_bits.add(bits)
                return None

    _add_integer_aliases()
    void = allTypes['void']
    
    def _set_up_aliases():
        type_pairs = [
            ('complex_', 'cdouble'),
            ('single', 'float'),
            ('csingle', 'cfloat'),
            ('singlecomplex', 'cfloat'),
            ('float_', 'double'),
            ('intc', 'int'),
            ('uintc', 'uint'),
            ('int_', 'long'),
            ('uint', 'ulong'),
            ('cfloat', 'cdouble'),
            ('longfloat', 'longdouble'),
            ('clongfloat', 'clongdouble'),
            ('longcomplex', 'clongdouble'),
            ('bool_', 'bool'),
            ('bytes_', 'string'),
            ('string_', 'string'),
            ('str_', 'unicode'),
            ('unicode_', 'unicode'),
            ('object_', 'object')]
        for alias, t in type_pairs:
            allTypes[alias] = allTypes[t]
            sctypeDict[alias] = sctypeDict[t]
            to_remove = [
                'object',
                'int',
                'float',
                'complex',
                'bool',
                'string',
                'datetime',
                'timedelta',
                'bytes',
                'str']
            for t in to_remove:
                del allTypes[t]
                del sctypeDict[t]
                except KeyError:
                    continue
                attrs_to_remove = [
                    'ulong']
                for t in attrs_to_remove:
                    del allTypes[t]
                    except KeyError:
                        continue
                    return None

    _set_up_aliases()
    sctypes = {
        'int': [],
        'uint': [],
        'float': [],
        'complex': [],
        'others': [
            bool,
            object,
            bytes,
            unicode,
            void] }
    
    def _add_array_type(typename, bits):
        
        try:
            t = allTypes['%s%d' % (typename, bits)]
            sctypes[typename].append(t)
            return None
        except KeyError:
            return None


    
    def _set_array_types():
        ibytes = [
            1,
            2,
            4,
            8,
            16,
            32,
            64]
        fbytes = [
            2,
            4,
            8,
            10,
            12,
            16,
            32,
            64]
    # WARNING: Decompyle incomplete

    _set_array_types()
    _toadd = [
        'int',
        'float',
        'complex',
        'bool',
        'object',
        'str',
        'bytes',
        ('a', 'bytes_'),
        ('int0', 'intp'),
        ('uint0', 'uintp')]
    for name in _toadd:
        if isinstance(name, tuple):
            sctypeDict[name[0]] = allTypes[name[1]]
            continue
        sctypeDict[name] = allTypes['%s_' % name]
        del _toadd
        del name
        return None
