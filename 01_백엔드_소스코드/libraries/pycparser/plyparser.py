# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plyparser.pyc (Python 3.11)

import warnings

class Coord(object):
    ''' Coordinates of a syntactic element. Consists of:
            - File name
            - Line number
            - (optional) column number, for the Lexer
    '''
    __slots__ = ('file', 'line', 'column', '__weakref__')
    
    def __init__(self, file, line, column = (None,)):
        self.file = file
        self.line = line
        self.column = column

    
    def __str__(self):
        str = f'''{self.file!s}:{self.line!s}'''
        if self.column:
            str += ':%s' % self.column
        return str



class ParseError(Exception):
    pass


class PLYParser(object):
    
    def _create_opt_rule(self, rulename):
        ''' Given a rule name, creates an optional ply.yacc rule
            for it. The name of the optional rule is
            <rulename>_opt
        '''
        optname = rulename + '_opt'
        
        def optrule(self, p):
            p[0] = p[1]

        optrule.__doc__ = f'''{optname!s} : empty\n| {rulename!s}'''
        optrule.__name__ = 'p_%s' % optname
        setattr(self.__class__, optrule.__name__, optrule)

    
    def _coord(self, lineno, column = (None,)):
        return Coord(file = self.clex.filename, line = lineno, column = column)

    
    def _token_coord(self, p, token_idx):
        """ Returns the coordinates for the YaccProduction object 'p' indexed
            with 'token_idx'. The coordinate includes the 'lineno' and
            'column'. Both follow the lex semantic, starting from 1.
        """
        last_cr = p.lexer.lexer.lexdata.rfind('\n', 0, p.lexpos(token_idx))
        if last_cr < 0:
            last_cr = -1
        column = p.lexpos(token_idx) - last_cr
        return self._coord(p.lineno(token_idx), column)

    
    def _parse_error(self, msg, coord):
        raise ParseError(f'''{coord!s}: {msg!s}''')



def parameterized(*params):
    """ Decorator to create parameterized rules.

    Parameterized rule methods must be named starting with 'p_' and contain
    'xxx', and their docstrings may contain 'xxx' and 'yyy'. These will be
    replaced by the given parameter tuples. For example, ``p_xxx_rule()`` with
    docstring 'xxx_rule  : yyy' when decorated with
    ``@parameterized(('id', 'ID'))`` produces ``p_id_rule()`` with the docstring
    'id_rule  : ID'. Using multiple tuples produces multiple rules.
    """
    pass
# WARNING: Decompyle incomplete


def template(cls):
    ''' Class decorator to generate rules from parameterized rule templates.

    See `parameterized` for more information on parameterized rules.
    '''
    issued_nodoc_warning = False
# WARNING: Decompyle incomplete


def _create_param_rules(cls, func):
    """ Create ply.yacc rules based on a parameterized rule function

    Generates new methods (one per each pair of parameters) based on the
    template rule function `func`, and attaches them to `cls`. The rule
    function's parameters must be accessible via its `_params` attribute.
    """
    pass
# WARNING: Decompyle incomplete
