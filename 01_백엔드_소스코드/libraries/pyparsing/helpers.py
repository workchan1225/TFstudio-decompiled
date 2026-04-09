# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

import html.entities as html
import operator
import re
import sys
import typing
from  import __diag__
from core import *
from util import _bslash, _flatten, _escape_regex_range_chars, make_compressed_re, replaced_by_pep8

def counted_array(expr = None, int_expr = None, *, intExpr):
    '''Helper to define a counted list of expressions.

    This helper defines a pattern of the form::

        integer expr expr expr...

    where the leading integer tells how many expr expressions follow.
    The matched tokens returns the array of expr tokens as a list - the
    leading count token is suppressed.

    If ``int_expr`` is specified, it should be a pyparsing expression
    that produces an integer value.

    Examples:

    .. doctest::

        >>> counted_array(Word(alphas)).parse_string(\'2 ab cd ef\')
        ParseResults([\'ab\', \'cd\'], {})

    - In this parser, the leading integer value is given in binary,
      \'10\' indicating that 2 values are in the array:

      .. doctest::

        >>> binary_constant = Word(\'01\').set_parse_action(lambda t: int(t[0], 2))
        >>> counted_array(Word(alphas), int_expr=binary_constant
        ...     ).parse_string(\'10 ab cd ef\')
        ParseResults([\'ab\', \'cd\'], {})

    - If other fields must be parsed after the count but before the
      list items, give the fields results names and they will
      be preserved in the returned ParseResults:

      .. doctest::

         >>> ppc = pyparsing.common
         >>> count_with_metadata = ppc.integer + Word(alphas)("type")
         >>> typed_array = counted_array(Word(alphanums),
         ...     int_expr=count_with_metadata)("items")
         >>> result = typed_array.parse_string("3 bool True True False")
         >>> print(result.dump())
         [\'True\', \'True\', \'False\']
         - items: [\'True\', \'True\', \'False\']
         - type: \'bool\'
    '''
    pass
# WARNING: Decompyle incomplete


def match_previous_literal(expr = None):
    '''Helper to define an expression that is indirectly defined from
    the tokens matched in a previous expression, that is, it looks for
    a \'repeat\' of a previous expression.  For example::

    .. testcode::

       first = Word(nums)
       second = match_previous_literal(first)
       match_expr = first + ":" + second

    will match ``"1:1"``, but not ``"1:2"``.  Because this
    matches a previous literal, will also match the leading
    ``"1:1"`` in ``"1:10"``. If this is not desired, use
    :class:`match_previous_expr`. Do *not* use with packrat parsing
    enabled.
    '''
    pass
# WARNING: Decompyle incomplete


def match_previous_expr(expr = None):
    '''Helper to define an expression that is indirectly defined from
    the tokens matched in a previous expression, that is, it looks for
    a \'repeat\' of a previous expression.  For example:

    .. testcode::

       first = Word(nums)
       second = match_previous_expr(first)
       match_expr = first + ":" + second

    will match ``"1:1"``, but not ``"1:2"``.  Because this
    matches by expressions, will *not* match the leading ``"1:1"``
    in ``"1:10"``; the expressions are evaluated first, and then
    compared, so ``"1"`` is compared with ``"10"``. Do *not* use
    with packrat parsing enabled.
    '''
    pass
# WARNING: Decompyle incomplete


def one_of(strs = None, caseless = None, use_regex = None, as_keyword = None, *, useRegex, asKeyword):
    '''Helper to quickly define a set of alternative :class:`Literal` s,
    and makes sure to do longest-first testing when there is a conflict,
    regardless of the input order, but returns
    a :class:`MatchFirst` for best performance.

    :param strs: a string of space-delimited literals, or a collection of
       string literals
    :param caseless: treat all literals as caseless
    :param use_regex: bool - as an optimization, will
       generate a :class:`Regex` object; otherwise, will generate
       a :class:`MatchFirst` object (if ``caseless=True`` or
       ``as_keyword=True``, or if creating a :class:`Regex` raises an exception)
    :param as_keyword: bool - enforce :class:`Keyword`-style matching on the
       generated expressions
    
    Parameters ``asKeyword`` and ``useRegex`` are retained for pre-PEP8
    compatibility, but will be removed in a future release.

    Example:

    .. testcode::

       comp_oper = one_of("< = > <= >= !=")
       var = Word(alphas)
       number = Word(nums)
       term = var | number
       comparison_expr = term + comp_oper + term
       print(comparison_expr.search_string("B = 12  AA=23 B<=AA AA>12"))

    prints:

    .. testoutput::

       [[\'B\', \'=\', \'12\'], [\'AA\', \'=\', \'23\'], [\'B\', \'<=\', \'AA\'], [\'AA\', \'>\', \'12\']]
    '''
    pass
# WARNING: Decompyle incomplete


def dict_of(key = None, value = None):
    '''Helper to easily and clearly define a dictionary by specifying
    the respective patterns for the key and value.  Takes care of
    defining the :class:`Dict`, :class:`ZeroOrMore`, and
    :class:`Group` tokens in the proper order.  The key pattern
    can include delimiting markers or punctuation, as long as they are
    suppressed, thereby leaving the significant key text.  The value
    pattern can include named results, so that the :class:`Dict` results
    can include named token fields.

    Example:

    .. doctest::

       >>> text = "shape: SQUARE posn: upper left color: light blue texture: burlap"
       
       >>> data_word = Word(alphas)
       >>> label = data_word + FollowedBy(\':\')
       >>> attr_expr = (
       ...    label
       ...    + Suppress(\':\')
       ...    + OneOrMore(data_word, stop_on=label)
       ...    .set_parse_action(\' \'.join))
       >>> print(attr_expr[1, ...].parse_string(text).dump())
       [\'shape\', \'SQUARE\', \'posn\', \'upper left\', \'color\', \'light blue\', \'texture\', \'burlap\']

       >>> attr_label = label
       >>> attr_value = Suppress(\':\') + OneOrMore(data_word, stop_on=label
       ...   ).set_parse_action(\' \'.join)

       # similar to Dict, but simpler call format
       >>> result = dict_of(attr_label, attr_value).parse_string(text)
       >>> print(result.dump())
       [[\'shape\', \'SQUARE\'], [\'posn\', \'upper left\'], [\'color\', \'light blue\'], [\'texture\', \'burlap\']]
       - color: \'light blue\'
       - posn: \'upper left\'
       - shape: \'SQUARE\'
       - texture: \'burlap\'
       [0]:
         [\'shape\', \'SQUARE\']
       [1]:
         [\'posn\', \'upper left\']
       [2]:
         [\'color\', \'light blue\']
       [3]:
         [\'texture\', \'burlap\']

       >>> print(result[\'shape\'])
       SQUARE
       >>> print(result.shape)  # object attribute access works too
       SQUARE
       >>> print(result.as_dict())
       {\'shape\': \'SQUARE\', \'posn\': \'upper left\', \'color\': \'light blue\', \'texture\': \'burlap\'}
    '''
    return Dict(OneOrMore(Group(key + value)))


def original_text_for(expr = None, as_string = None, *, asString):
    '''Helper to return the original, untokenized text for a given
    expression.  Useful to restore the parsed fields of an HTML start
    tag into the raw tag text itself, or to revert separate tokens with
    intervening whitespace back to the original matching input text. By
    default, returns a string containing the original parsed text.

    If the optional ``as_string`` argument is passed as
    ``False``, then the return value is
    a :class:`ParseResults` containing any results names that
    were originally matched, and a single token containing the original
    matched text from the input string.  So if the expression passed to
    :class:`original_text_for` contains expressions with defined
    results names, you must set ``as_string`` to ``False`` if you
    want to preserve those results name values.

    The ``asString`` pre-PEP8 argument is retained for compatibility,
    but will be removed in a future release.

    Example:

    .. testcode::

       src = "this is test <b> bold <i>text</i> </b> normal text "
       for tag in ("b", "i"):
           opener, closer = make_html_tags(tag)
           patt = original_text_for(opener + ... + closer)
           print(patt.search_string(src)[0])

    prints:

    .. testoutput::

       [\'<b> bold <i>text</i> </b>\']
       [\'<i>text</i>\']
    '''
    if asString:
        asString = as_string
        locMarker = Empty().set_parse_action((lambda s, loc, t: loc))
        endlocMarker = locMarker.copy()
        endlocMarker.callPreparse = False
        matchExpr = locMarker('_original_start') + expr + endlocMarker('_original_end')
        if asString:
            
            extractText = lambda s, l, t: s[t._original_start:t._original_end]
        else:
            
            def extractText(s, l, t):
                t[:] = [
                    s[t.pop('_original_start'):t.pop('_original_end')]]

    matchExpr.set_parse_action(extractText)
    matchExpr.ignoreExprs = expr.ignoreExprs
    matchExpr.suppress_warning(Diagnostics.warn_ungrouped_named_tokens_in_collection)
    return matchExpr


def ungroup(expr = None):
    """Helper to undo pyparsing's default grouping of And expressions,
    even if all but one are non-empty.
    """
    return TokenConverter(expr).add_parse_action((lambda t: t[0]))


def locatedExpr(expr = None):
    '''
    .. deprecated:: 3.0.0
       Use the :class:`Located` class instead.

    Helper to decorate a returned token with its starting and ending
    locations in the input string.

    This helper adds the following results names:

    - ``locn_start`` - location where matched expression begins
    - ``locn_end`` - location where matched expression ends
    - ``value`` - the actual parsed results

    Be careful if the input text contains ``<TAB>`` characters, you
    may want to call :meth:`ParserElement.parse_with_tabs`

    Example:

    .. testcode::

       wd = Word(alphas)
       res = locatedExpr(wd).search_string("ljsdf123lksdjjf123lkkjj1222")
       for match in res:
           print(match)

    prints:

    .. testoutput::

       [[0, \'ljsdf\', 5]]
       [[8, \'lksdjjf\', 15]]
       [[18, \'lkkjj\', 23]]
    '''
    locator = Empty().set_parse_action((lambda ss, ll, tt: ll))
    return Group(locator('locn_start') + expr('value') + locator.copy().leaveWhitespace()('locn_end'))

_NO_IGNORE_EXPR_GIVEN = NoMatch()

def nested_expr(opener = None, closer = None, content = None, ignore_expr = None, *, ignoreExpr):
    '''Helper method for defining nested lists enclosed in opening and
    closing delimiters (``"("`` and ``")"`` are the default).

    :param opener: str - opening character for a nested list
       (default= ``"("``); can also be a pyparsing expression

    :param closer: str - closing character for a nested list
       (default= ``")"``); can also be a pyparsing expression

    :param content: expression for items within the nested lists

    :param ignore_expr: expression for ignoring opening and closing delimiters
       (default = :class:`quoted_string`)

    Parameter ``ignoreExpr`` is retained for compatibility
    but will be removed in a future release.

    If an expression is not provided for the content argument, the
    nested expression will capture all whitespace-delimited content
    between delimiters as a list of separate values.

    Use the ``ignore_expr`` argument to define expressions that may
    contain opening or closing characters that should not be treated as
    opening or closing characters for nesting, such as quoted_string or
    a comment expression.  Specify multiple expressions using an
    :class:`Or` or :class:`MatchFirst`. The default is
    :class:`quoted_string`, but if no expressions are to be ignored, then
    pass ``None`` for this argument.

    Example:

    .. testcode::

       data_type = one_of("void int short long char float double")
       decl_data_type = Combine(data_type + Opt(Word(\'*\')))
       ident = Word(alphas+\'_\', alphanums+\'_\')
       number = pyparsing_common.number
       arg = Group(decl_data_type + ident)
       LPAR, RPAR = map(Suppress, "()")

       code_body = nested_expr(\'{\', \'}\', ignore_expr=(quoted_string | c_style_comment))

       c_function = (decl_data_type("type")
                     + ident("name")
                     + LPAR + Opt(DelimitedList(arg), [])("args") + RPAR
                     + code_body("body"))
       c_function.ignore(c_style_comment)

       source_code = \'\'\'
           int is_odd(int x) {
               return (x%2);
           }

           int dec_to_hex(char hchar) {
               if (hchar >= \'0\' && hchar <= \'9\') {
                   return (ord(hchar)-ord(\'0\'));
               } else {
                   return (10+ord(hchar)-ord(\'A\'));
               }
           }
       \'\'\'
       for func in c_function.search_string(source_code):
           print(f"{func.name} ({func.type}) args: {func.args}")


    prints:

    .. testoutput::

       is_odd (int) args: [[\'int\', \'x\']]
       dec_to_hex (int) args: [[\'char\', \'hchar\']]
    '''
    if ignoreExpr != ignore_expr:
        ignoreExpr = ignore_expr if ignoreExpr is _NO_IGNORE_EXPR_GIVEN else ignoreExpr
    if ignoreExpr is _NO_IGNORE_EXPR_GIVEN:
        ignoreExpr = quoted_string()
    if opener == closer:
        raise ValueError('opening and closing strings cannot be the same')
# WARNING: Decompyle incomplete


def _makeTags(tagStr, xml, suppress_LT, suppress_GT = (Suppress('<'), Suppress('>'))):
    '''Internal helper to construct opening and closing tag expressions,
    given a tag name'''
    pass
# WARNING: Decompyle incomplete


def make_html_tags(tag_str = None):
    '''Helper to construct opening and closing tag expressions for HTML,
    given a tag name. Matches tags in either upper or lower case,
    attributes with namespaces and with quoted or unquoted values.

    Example:

    .. testcode::

       text = \'<td>More info at the <a href="https://github.com/pyparsing/pyparsing/wiki">pyparsing</a> wiki page</td>\'
       # make_html_tags returns pyparsing expressions for the opening and
       # closing tags as a 2-tuple
       a, a_end = make_html_tags("A")
       link_expr = a + SkipTo(a_end)("link_text") + a_end

       for link in link_expr.search_string(text):
           # attributes in the <A> tag (like "href" shown here) are
           # also accessible as named results
           print(link.link_text, \'->\', link.href)

    prints:

    .. testoutput::

       pyparsing -> https://github.com/pyparsing/pyparsing/wiki
    '''
    return _makeTags(tag_str, False)


def any_close_tag: ParserElement(tag_str = None):
    '''Helper to construct opening and closing tag expressions for XML,
    given a tag name. Matches tags only in the given upper/lower case.

    Example: similar to :class:`make_html_tags`
    '''
    return _makeTags(tag_str, True)

(any_open_tag, any_close_tag) = make_html_tags(Word(alphas, alphanums + '_:').set_name('any tag'))
_htmlEntityMap = html.entities.html5.items()()
_most_common_entities = 'nbsp lt gt amp quot apos cent pound euro copy'.replace(' ', '|')
common_html_entity = Regex((lambda : f'''&(?P<entity>{_most_common_entities}|{make_compressed_re(_htmlEntityMap)});''')).set_name('common HTML entity')

def replace_html_entity(s, l, t):
    '''Helper parser action to replace common HTML entities with their special characters'''
    return _htmlEntityMap.get(t.entity)


class OpAssoc(Enum):
    '''Enumeration of operator associativity
    - used in constructing InfixNotationOperatorSpec for :class:`infix_notation`'''
    LEFT = 1
    RIGHT = 2

InfixNotationOperatorArgType = Union[(ParserElement, str, tuple[(Union[(ParserElement, str)], Union[(ParserElement, str)])])]
InfixNotationOperatorSpec = Union[(tuple[(InfixNotationOperatorArgType, int, OpAssoc, typing.Optional[ParseAction])], tuple[(InfixNotationOperatorArgType, int, OpAssoc)])]

def infix_notation(base_expr = None, op_list = (lambda .0: pass# WARNING: Decompyle incomplete
), lpar = None, rpar = (Suppress('('), Suppress(')'))):
    """Helper method for constructing grammars of expressions made up of
    operators working in a precedence hierarchy.  Operators may be unary
    or binary, left- or right-associative.  Parse actions can also be
    attached to operator expressions. The generated parser will also
    recognize the use of parentheses to override operator precedences
    (see example below).

    Note: if you define a deep operator list, you may see performance
    issues when using infix_notation. See
    :class:`ParserElement.enable_packrat` for a mechanism to potentially
    improve your parser performance.

    Parameters:

    :param base_expr: expression representing the most basic operand to
       be used in the expression
    :param op_list: list of tuples, one for each operator precedence level
       in the expression grammar; each tuple is of the form ``(op_expr,
       num_operands, right_left_assoc, (optional)parse_action)``, where:

       - ``op_expr`` is the pyparsing expression for the operator; may also
         be a string, which will be converted to a Literal; if ``num_operands``
         is 3, ``op_expr`` is a tuple of two expressions, for the two
         operators separating the 3 terms
       - ``num_operands`` is the number of terms for this operator (must be 1,
         2, or 3)
       - ``right_left_assoc`` is the indicator whether the operator is right
         or left associative, using the pyparsing-defined constants
         ``OpAssoc.RIGHT`` and ``OpAssoc.LEFT``.
       - ``parse_action`` is the parse action to be associated with
         expressions matching this operator expression (the parse action
         tuple member may be omitted); if the parse action is passed
         a tuple or list of functions, this is equivalent to calling
         ``set_parse_action(*fn)``
         (:class:`ParserElement.set_parse_action`)

    :param lpar: expression for matching left-parentheses; if passed as a
       str, then will be parsed as ``Suppress(lpar)``. If lpar is passed as
       an expression (such as ``Literal('(')``), then it will be kept in
       the parsed results, and grouped with them. (default= ``Suppress('(')``)
    :param rpar: expression for matching right-parentheses; if passed as a
       str, then will be parsed as ``Suppress(rpar)``. If rpar is passed as
       an expression (such as ``Literal(')')``), then it will be kept in
       the parsed results, and grouped with them. (default= ``Suppress(')')``)

    Example:

    .. testcode::

       # simple example of four-function arithmetic with ints and
       # variable names
       integer = pyparsing_common.signed_integer
       varname = pyparsing_common.identifier

       arith_expr = infix_notation(integer | varname,
           [
           ('-', 1, OpAssoc.RIGHT),
           (one_of('* /'), 2, OpAssoc.LEFT),
           (one_of('+ -'), 2, OpAssoc.LEFT),
           ])

       arith_expr.run_tests('''
           5+3*6
           (5+3)*6
           (5+x)*y
           -2--11
           ''', full_dump=False)

    prints:

    .. testoutput::
       :options: +NORMALIZE_WHITESPACE


       5+3*6
       [[5, '+', [3, '*', 6]]]

       (5+3)*6
       [[[5, '+', 3], '*', 6]]

       (5+x)*y
       [[[5, '+', 'x'], '*', 'y']]

       -2--11
       [[['-', 2], '-', ['-', 11]]]
    """
    
    class _FB(FollowedBy):
        
        def parseImpl(self, instring, loc, doActions = (True,)):
            self.expr.try_parse(instring, loc)
            return (loc, [])


    _FB.__name__ = 'FollowedBy>'
    ret = Forward()
    ret.set_name(f'''{base_expr.name}_expression''')
    if isinstance(lpar, str):
        lpar = Suppress(lpar)
    if isinstance(rpar, str):
        rpar = Suppress(rpar)
    nested_expr = (lpar + ret + rpar).set_name(f'''nested_{base_expr.name}_expression''')
    if not isinstance(lpar, Suppress) or isinstance(rpar, Suppress):
        lastExpr = base_expr | Group(nested_expr)
    else:
        lastExpr = base_expr | nested_expr
# WARNING: Decompyle incomplete


def indentedBlock(blockStatementExpr, indentStack, indent, backup_stacks = (True, [])):
    '''
    .. deprecated:: 3.0.0
       Use the :class:`IndentedBlock` class instead.

    Helper method for defining space-delimited indentation blocks,
    such as those used to define block statements in Python source code.

    :param blockStatementExpr: expression defining syntax of statement that
      is repeated within the indented block

    :param indentStack: list created by caller to manage indentation stack
      (multiple ``statementWithIndentedBlock`` expressions within a single
      grammar should share a common ``indentStack``)

    :param indent: boolean indicating whether block must be indented beyond
      the current level; set to ``False`` for block of left-most statements

    A valid block must contain at least one ``blockStatement``.

    (Note that indentedBlock uses internal parse actions which make it
    incompatible with packrat parsing.)

    Example:

    .. testcode::

       data = \'\'\'
       def A(z):
         A1
         B = 100
         G = A2
         A2
         A3
       B
       def BB(a,b,c):
         BB1
         def BBA():
           bba1
           bba2
           bba3
       C
       D
       def spam(x,y):
            def eggs(z):
                pass
       \'\'\'

       indentStack = [1]
       stmt = Forward()

       identifier = Word(alphas, alphanums)
       funcDecl = ("def" + identifier + Group("(" + Opt(delimitedList(identifier)) + ")") + ":")
       func_body = indentedBlock(stmt, indentStack)
       funcDef = Group(funcDecl + func_body)

       rvalue = Forward()
       funcCall = Group(identifier + "(" + Opt(delimitedList(rvalue)) + ")")
       rvalue << (funcCall | identifier | Word(nums))
       assignment = Group(identifier + "=" + rvalue)
       stmt << (funcDef | assignment | identifier)

       module_body = stmt[1, ...]

       parseTree = module_body.parseString(data)
       parseTree.pprint()

    prints:

    .. testoutput::

       [[\'def\',
         \'A\',
         [\'(\', \'z\', \')\'],
         \':\',
         [[\'A1\'], [[\'B\', \'=\', \'100\']], [[\'G\', \'=\', \'A2\']], [\'A2\'], [\'A3\']]],
        \'B\',
        [\'def\',
         \'BB\',
         [\'(\', \'a\', \'b\', \'c\', \')\'],
         \':\',
         [[\'BB1\'], [[\'def\', \'BBA\', [\'(\', \')\'], \':\', [[\'bba1\'], [\'bba2\'], [\'bba3\']]]]]],
        \'C\',
        \'D\',
        [\'def\',
         \'spam\',
         [\'(\', \'x\', \'y\', \')\'],
         \':\',
         [[[\'def\', \'eggs\', [\'(\', \'z\', \')\'], \':\', [[\'pass\']]]]]]]
    '''
    pass
# WARNING: Decompyle incomplete

c_style_comment = Regex('/\\*(?:[^*]|\\*(?!/))*\\*\\/').set_name('C style comment')
html_comment = Regex('<!--[\\s\\S]*?-->').set_name('HTML comment')
rest_of_line = Regex('.*').leave_whitespace().set_name('rest of line')
dbl_slash_comment = Regex('//(?:\\\\\\n|[^\\n])*').set_name('// comment')
cpp_style_comment = Regex('(?:/\\*(?:[^*]|\\*(?!/))*\\*\\/)|(?://(?:\\\\\\n|[^\\n])*)').set_name('C++ style comment')
java_style_comment = cpp_style_comment
python_style_comment = Regex('#.*').set_name('Python style comment')
_builtin_exprs: list[ParserElement] = vars().values()()

def delimited_list(expr = None, delim = None, combine = None, min = (lambda .0: pass# WARNING: Decompyle incomplete
), max = (',', False, None, None), *, allow_trailing_delim):
    '''
    .. deprecated:: 3.1.0
       Use the :class:`DelimitedList` class instead.
    '''
    return DelimitedList(expr, delim, combine, min, max, allow_trailing_delim = allow_trailing_delim)

opAssoc = OpAssoc
anyOpenTag = any_open_tag
anyCloseTag = any_close_tag
commonHTMLEntity = common_html_entity
cStyleComment = c_style_comment
htmlComment = html_comment
restOfLine = rest_of_line
dblSlashComment = dbl_slash_comment
cppStyleComment = cpp_style_comment
javaStyleComment = java_style_comment
pythonStyleComment = python_style_comment
delimitedList = replaced_by_pep8('delimitedList', DelimitedList)
delimited_list = replaced_by_pep8('delimited_list', DelimitedList)
countedArray = replaced_by_pep8('countedArray', counted_array)
matchPreviousLiteral = replaced_by_pep8('matchPreviousLiteral', match_previous_literal)
matchPreviousExpr = replaced_by_pep8('matchPreviousExpr', match_previous_expr)
oneOf = replaced_by_pep8('oneOf', one_of)
dictOf = replaced_by_pep8('dictOf', dict_of)
originalTextFor = replaced_by_pep8('originalTextFor', original_text_for)
nestedExpr = replaced_by_pep8('nestedExpr', nested_expr)
makeHTMLTags = replaced_by_pep8('makeHTMLTags', make_html_tags)
makeXMLTags = replaced_by_pep8('makeXMLTags', make_xml_tags)
replaceHTMLEntity = replaced_by_pep8('replaceHTMLEntity', replace_html_entity)
infixNotation = replaced_by_pep8('infixNotation', infix_notation)
