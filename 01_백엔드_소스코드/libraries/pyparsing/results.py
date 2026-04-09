# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: results.pyc (Python 3.11)

from __future__ import annotations
import collections
from collections.abc import MutableMapping, Mapping, MutableSequence, Iterator, Iterable
import pprint
from typing import Any
from util import replaced_by_pep8
str_type: 'tuple[type, ...]' = (str, bytes)
_generator_type = (lambda .0: pass# WARNING: Decompyle incomplete
)(()())

class _ParseResultsWithOffset:
    tup: 'tuple[ParseResults, int]' = '_ParseResultsWithOffset'
    __slots__ = [
        'tup']
    
    def __init__(self = None, p1 = None, p2 = None):
        self.tup = (p1, p2)

    
    def __getitem__(self, i):
        return self.tup[i]

    
    def __getstate__(self):
        return self.tup

    
    def __setstate__(self, *args):
        self.tup = args[0]



class ParseResults:
    '''Structured parse results, to provide multiple means of access to
    the parsed data:

    - as a list (``len(results)``)
    - by list index (``results[0], results[1]``, etc.)
    - by attribute (``results.<results_name>`` - see :class:`ParserElement.set_results_name`)

    Example:

    .. testcode::

       integer = Word(nums)
       date_str = (integer.set_results_name("year") + \'/\'
                   + integer.set_results_name("month") + \'/\'
                   + integer.set_results_name("day"))
       # equivalent form:
       # date_str = (integer("year") + \'/\'
       #             + integer("month") + \'/\'
       #             + integer("day"))

       # parse_string returns a ParseResults object
       result = date_str.parse_string("1999/12/31")

       def test(s, fn=repr):
           print(f"{s} -> {fn(eval(s))}")

       test("list(result)")
       test("result[0]")
       test("result[\'month\']")
       test("result.day")
       test("\'month\' in result")
       test("\'minutes\' in result")
       test("result.dump()", str)

    prints:

    .. testoutput::

       list(result) -> [\'1999\', \'/\', \'12\', \'/\', \'31\']
       result[0] -> \'1999\'
       result[\'month\'] -> \'12\'
       result.day -> \'31\'
       \'month\' in result -> True
       \'minutes\' in result -> False
       result.dump() -> [\'1999\', \'/\', \'12\', \'/\', \'31\']
       - day: \'31\'
       - month: \'12\'
       - year: \'1999\'

    '''
    _tokdict: 'dict[str, Any]' = (None, [], ())
    __slots__ = ('_name', '_parent', '_all_names', '_modal', '_toklist', '_tokdict')
    
    class List(list):
        '''
        Simple wrapper class to distinguish parsed list results that should be preserved
        as actual Python lists, instead of being converted to :class:`ParseResults`:

        .. testcode::

           import pyparsing as pp
           ppc = pp.common

           LBRACK, RBRACK, LPAR, RPAR = pp.Suppress.using_each("[]()")
           element = pp.Forward()
           item = ppc.integer
           item_list = pp.DelimitedList(element)
           element_list = LBRACK + item_list + RBRACK | LPAR + item_list + RPAR
           element <<= item | element_list

           # add parse action to convert from ParseResults
           # to actual Python collection types
           @element_list.add_parse_action
           def as_python_list(t):
               return pp.ParseResults.List(t.as_list())

           element.run_tests(\'\'\'
               100
               [2,3,4]
               [[2, 1],3,4]
               [(2, 1),3,4]
               (2,3,4)
               ([2, 3], 4)
               \'\'\', post_parse=lambda s, r: (r[0], type(r[0]))
           )

        prints:

        .. testoutput::
           :options: +NORMALIZE_WHITESPACE


           100
           (100, <class \'int\'>)

           [2,3,4]
           ([2, 3, 4], <class \'list\'>)

           [[2, 1],3,4]
           ([[2, 1], 3, 4], <class \'list\'>)

           [(2, 1),3,4]
           ([[2, 1], 3, 4], <class \'list\'>)

           (2,3,4)
           ([2, 3, 4], <class \'list\'>)

           ([2, 3], 4)
           ([[2, 3], 4], <class \'list\'>)

        (Used internally by :class:`Group` when `aslist=True`.)
        '''
        
        def __new__(cls, contained = (None,)):
            pass
        # WARNING: Decompyle incomplete


    
    def __new__(cls, toklist, name = (None, None), **kwargs):
        if isinstance(toklist, ParseResults):
            return toklist
        self = None.__new__(cls)
        self._name = None
        self._parent = None
        self._all_names = set()
    # WARNING: Decompyle incomplete

    
    def __init__(self, toklist = None, name = None, asList = None, modal = (None, None, True, True, isinstance), isinstance = ('return', 'None')):
        self
        self._modal = modal
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, i):
        if isinstance(i, (int, slice)):
            return self._toklist[i]
        if None not in self._all_names:
            return self._tokdict[i][-1][0]
        return (lambda .0: [ v[0] for v in .0 ])(self._tokdict[i]())

    
    def __setitem__(self, k, v, isinstance = (isinstance,)):
        if isinstance(v, _ParseResultsWithOffset):
            self._tokdict[k] = self._tokdict.get(k, list()) + [
                v]
            sub = v[0]
        elif isinstance(k, (int, slice)):
            self._toklist[k] = v
            sub = v
        else:
            self._tokdict[k] = self._tokdict.get(k, []) + [
                _ParseResultsWithOffset(v, 0)]
            sub = v
        if isinstance(sub, ParseResults):
            sub._parent = self
            return None

    
    def __delitem__(self, i):
        if not isinstance(i, (int, slice)):
            del self._tokdict[i]
            return None
        mylen = None(self._toklist)
        del self._toklist[i]
        if isinstance(i, int):
            if i < 0:
                i += mylen
            i = slice(i, i + 1)
    # WARNING: Decompyle incomplete

    
    def __contains__(self = None, k = None):
        return k in self._tokdict

    
    def __len__(self = None):
        return len(self._toklist)

    
    def __bool__(self = None):
