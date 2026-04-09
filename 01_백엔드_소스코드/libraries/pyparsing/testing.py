# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: testing.pyc (Python 3.11)

from contextlib import contextmanager
import re
import typing
from core import ParserElement, ParseException, Keyword, __diag__, __compat__

class pyparsing_test:
    '''
    namespace class for classes useful in writing unit tests
    '''
    
    class reset_pyparsing_context:
        '''
        Context manager to be used when writing unit tests that modify pyparsing config values:
        - packrat parsing
        - bounded recursion parsing
        - default whitespace characters
        - default keyword characters
        - literal string auto-conversion class
        - ``__diag__`` settings

        Example:

        .. testcode::

            ppt = pyparsing.pyparsing_test

            class MyTestClass(ppt.TestParseResultsAsserts):
                def test_literal(self):
                    with ppt.reset_pyparsing_context():
                        # test that literals used to construct
                        # a grammar are automatically suppressed
                        ParserElement.inline_literals_using(Suppress)

                        term = Word(alphas) | Word(nums)
                        group = Group(\'(\' + term[...] + \')\')

                        # assert that the \'()\' characters
                        # are not included in the parsed tokens
                        self.assertParseAndCheckList(
                            group,
                            "(abc 123 def)",
                            [\'abc\', \'123\', \'def\']
                        )

                    # after exiting context manager, literals
                    # are converted to Literal expressions again
        '''
        
        def __init__(self):
            self._save_context = { }

        
        def save(self):
            self._save_context['default_whitespace'] = ParserElement.DEFAULT_WHITE_CHARS
            self._save_context['default_keyword_chars'] = Keyword.DEFAULT_KEYWORD_CHARS
            self._save_context['literal_string_class'] = ParserElement._literalStringClass
            self._save_context['verbose_stacktrace'] = ParserElement.verbose_stacktrace
            self._save_context['packrat_enabled'] = ParserElement._packratEnabled
            if ParserElement._packratEnabled:
                self._save_context['packrat_cache_size'] = ParserElement.packrat_cache.size
            else:
                self._save_context['packrat_cache_size'] = None
            self._save_context['packrat_parse'] = ParserElement._parse
            self._save_context['recursion_enabled'] = ParserElement._left_recursion_enabled
            self._save_context['__diag__'] = __diag__._all_names()
            self._save_context['__compat__'] = {
                'collect_all_And_tokens': __compat__.collect_all_And_tokens }
            return self

        
        def restore(self):
            if ParserElement.DEFAULT_WHITE_CHARS != self._save_context['default_whitespace']:
                ParserElement.set_default_whitespace_chars(self._save_context['default_whitespace'])
            ParserElement.verbose_stacktrace = self._save_context['verbose_stacktrace']
            Keyword.DEFAULT_KEYWORD_CHARS = self._save_context['default_keyword_chars']
            ParserElement.inlineLiteralsUsing(self._save_context['literal_string_class'])
            for name, value in self._save_context['__diag__'].items():
                __diag__.enable if value else __diag__.disable(name)
                ParserElement._packratEnabled = False
                if self._save_context['packrat_enabled']:
                    ParserElement.enable_packrat(self._save_context['packrat_cache_size'])
                else:
                    ParserElement._parse = self._save_context['packrat_parse']
            ParserElement._left_recursion_enabled = self._save_context['recursion_enabled']
            __compat__.collect_all_And_tokens = self._save_context['__compat__']
            return self

        
        def copy(self):
            ret = type(self)()
            ret._save_context.update(self._save_context)
            return ret

        
        def __enter__(self):
            return self.save()

        
        def __exit__(self, *args):
            self.restore()


    
    class TestParseResultsAsserts:
        '''
        A mixin class to add parse results assertion methods to normal unittest.TestCase classes.
        '''
        
        def assertParseResultsEquals(self, result, expected_list, expected_dict, msg = (None, None, None)):
            '''
            Unit test assertion to compare a :class:`ParseResults` object with an optional ``expected_list``,
            and compare any defined results names with an optional ``expected_dict``.
            '''
            pass
        # WARNING: Decompyle incomplete

        
        def assertParseAndCheckList(self, expr, test_string, expected_list, msg, verbose = (None, True)):
            '''
            Convenience wrapper assert to test a parser element and input string, and assert that
            the resulting :meth:`ParseResults.as_list` is equal to the ``expected_list``.
            '''
            result = expr.parse_string(test_string, parse_all = True)
            if verbose:
                print(result.dump())
            else:
                print(result.as_list())
            self.assertParseResultsEquals(result, expected_list = expected_list, msg = msg)

        
        def assertParseAndCheckDict(self, expr, test_string, expected_dict, msg, verbose = (None, True)):
            '''
            Convenience wrapper assert to test a parser element and input string, and assert that
            the resulting :meth:`ParseResults.as_dict` is equal to the ``expected_dict``.
            '''
            result = expr.parse_string(test_string, parseAll = True)
            if verbose:
                print(result.dump())
            else:
                print(result.as_list())
            self.assertParseResultsEquals(result, expected_dict = expected_dict, msg = msg)

        
        def assertRunTestResults(self, run_tests_report, expected_parse_results, msg = (None, None)):
            '''
            Unit test assertion to evaluate output of
            :meth:`~ParserElement.run_tests`.

            If a list of list-dict tuples is given as the
            ``expected_parse_results`` argument, then these are zipped
            with the report tuples returned by ``run_tests()``
            and evaluated using :meth:`assertParseResultsEquals`.
            Finally, asserts that the overall
            `:meth:~ParserElement.run_tests` success value is ``True``.

            :param run_tests_report: the return value from :meth:`ParserElement.run_tests`
            :type run_tests_report: tuple[bool, list[tuple[str, ParseResults | Exception]]]
            :param expected_parse_results: (optional)
            :type expected_parse_results: list[tuple[str | list | dict | Exception, ...]]
            '''
            (run_test_success, run_test_results) = run_tests_report
        # WARNING: Decompyle incomplete

        assertRaisesParseException = (lambda self, exc_type, expected_msg, msg = (ParseException, None, None): pass# WARNING: Decompyle incomplete
)()

    with_line_numbers = (lambda s = None, start_line = None, end_line = None, expand_tabs = staticmethod, eol_mark = (None, None, True, '|', None, None), mark_spaces = {
        'indent': '',
        'base_1': True }, mark_control = ('s', str, 'start_line', typing.Optional[int], 'end_line', typing.Optional[int], 'expand_tabs', bool, 'eol_mark', str, 'mark_spaces', typing.Optional[str], 'mark_control', typing.Optional[str], 'indent', typing.Union[(str, int)], 'base_1', bool, 'return', str), *, indent, base_1, transtable_map = None, tbl = None, s_lines = None, max_line_len = None, lead = None: pass# WARNING: Decompyle incomplete
)()
