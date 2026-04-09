# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: results.pyc (Python 3.11)

from collections.abc import MutableMapping, Mapping, MutableSequence, Iterator
import pprint
from weakref import ref as wkref
from typing import Tuple, Any
str_type: Tuple[(type, ...)] = (str, bytes)
_generator_type = (lambda .0: pass# WARNING: Decompyle incomplete
)(()())

class _ParseResultsWithOffset:
    __slots__ = [
        'tup']
    
    def __init__(self, p1, p2):
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

    Example::

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
            print("{} -> {}".format(s, fn(eval(s))))
        test("list(result)")
        test("result[0]")
        test("result[\'month\']")
        test("result.day")
        test("\'month\' in result")
        test("\'minutes\' in result")
        test("result.dump()", str)

    prints::

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
    _null_values: Tuple[(Any, ...)] = (None, [], '', ())
    __slots__ = [
        '_name',
        '_parent',
        '_all_names',
        '_modal',
        '_toklist',
        '_tokdict',
        '__weakref__']
    
    class List(list):
        '''
        Simple wrapper class to distinguish parsed list results that should be preserved
        as actual Python lists, instead of being converted to :class:`ParseResults`:

            LBRACK, RBRACK = map(pp.Suppress, "[]")
            element = pp.Forward()
            item = ppc.integer
            element_list = LBRACK + pp.delimited_list(element) + RBRACK

            # add parse actions to convert from ParseResults to actual Python collection types
            def as_python_list(t):
                return pp.ParseResults.List(t.as_list())
            element_list.add_parse_action(as_python_list)

            element <<= item | element_list

            element.run_tests(\'\'\'
                100
                [2,3,4]
                [[2, 1],3,4]
                [(2, 1),3,4]
                (2,3,4)
                \'\'\', post_parse=lambda s, r: (r[0], type(r[0])))

        prints:

            100
            (100, <class \'int\'>)

            [2,3,4]
            ([2, 3, 4], <class \'list\'>)

            [[2, 1],3,4]
            ([[2, 1], 3, 4], <class \'list\'>)

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

    
    def __init__(self, toklist, name, asList, modal, isinstance = (None, None, True, True, isinstance)):
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
            self._tokdict[k] = self._tokdict.get(k, list()) + [
                _ParseResultsWithOffset(v, 0)]
            sub = v
        if isinstance(sub, ParseResults):
            sub._parent = wkref(self)
            return None

    
    def __delitem__(self, i):
        pass
    # WARNING: Decompyle incomplete

    
    def __contains__(self = None, k = None):
        return k in self._tokdict

    
    def __len__(self = None):
        return len(self._toklist)

    
    def __bool__(self = None):
