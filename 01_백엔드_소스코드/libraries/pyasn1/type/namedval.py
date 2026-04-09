# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: namedval.pyc (Python 3.11)

from pyasn1 import error
__all__ = [
    'NamedValues']

class NamedValues(object):
    """Create named values object.

    The |NamedValues| object represents a collection of string names
    associated with numeric IDs. These objects are used for giving
    names to otherwise numerical values.

    |NamedValues| objects are immutable and duck-type Python
    :class:`dict` object mapping ID to name and vice-versa.

    Parameters
    ----------
    *args: variable number of two-element :py:class:`tuple`

        name: :py:class:`str`
            Value label

        value: :py:class:`int`
            Numeric value

    Keyword Args
    ------------
    name: :py:class:`str`
        Value label

    value: :py:class:`int`
        Numeric value

    Examples
    --------

    .. code-block:: pycon

        >>> nv = NamedValues('a', 'b', ('c', 0), d=1)
        >>> nv
        >>> {'c': 0, 'd': 1, 'a': 2, 'b': 3}
        >>> nv[0]
        'c'
        >>> nv['a']
        2
    """
    
    def __init__(self, *args, **kwargs):
        self._NamedValues__names = { }
        self._NamedValues__numbers = { }
        anonymousNames = []
        for namedValue in args:
            if isinstance(namedValue, (tuple, list)):
                (name, number) = namedValue
            else:
                except ValueError:
                    raise error.PyAsn1Error(f'''Not a proper attribute-value pair {namedValue!r}''')
                anonymousNames.append(namedValue)
            if name in self._NamedValues__names:
                raise error.PyAsn1Error(f'''Duplicate name {name!s}''')
            if number in self._NamedValues__numbers:
                raise error.PyAsn1Error(f'''Duplicate number  {name!s}={number!s}''')
            self._NamedValues__names[name] = number
            self._NamedValues__numbers[number] = name
            for name, number in kwargs.items():
                if name in self._NamedValues__names:
                    raise error.PyAsn1Error(f'''Duplicate name {name!s}''')
                if number in self._NamedValues__numbers:
                    raise error.PyAsn1Error(f'''Duplicate number  {name!s}={number!s}''')
                self._NamedValues__names[name] = number
                self._NamedValues__numbers[number] = name
                if anonymousNames:
                    if self._NamedValues__numbers:
                        if not max(self._NamedValues__numbers) + 1:
                            number = 0
                            for name in anonymousNames:
                                if name in self._NamedValues__names:
                                    raise error.PyAsn1Error(f'''Duplicate name {name!s}''')
                                self._NamedValues__names[name] = number
                                self._NamedValues__numbers[number] = name
                                number += 1
                                return None
                                return None

    
    def __repr__(self):
        representation = (lambda .0: [ '%s=%d' % x for x in .0 ])(self.items()())
        if len(representation) > 64:
            representation = representation[:32] + '...' + representation[-32:]
        return f'''<{self.__class__.__name__!s} object, enums {representation!s}>'''

    
    def __eq__(self, other):
        return dict(self) == other

    
    def __ne__(self, other):
        return dict(self) != other

    
    def __lt__(self, other):
        return dict(self) < other

    
    def __le__(self, other):
        return dict(self) <= other

    
    def __gt__(self, other):
        return dict(self) > other

    
    def __ge__(self, other):
        return dict(self) >= other

    
    def __hash__(self):
        return hash(self.items())

    
    def __getitem__(self, key):
        
        try:
            return self._NamedValues__numbers[key]
        except KeyError:
            return 


    
    def __len__(self):
        return len(self._NamedValues__names)

    
    def __contains__(self, key):
