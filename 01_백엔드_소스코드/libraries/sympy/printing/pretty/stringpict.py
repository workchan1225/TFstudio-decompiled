# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stringpict.pyc (Python 3.11)

'''Prettyprinter by Jurjen Bos.
(I hate spammers: mail me at pietjepuk314 at the reverse of ku.oc.oohay).
All objects have a method that create a "stringPict",
that can be used in the str method for pretty printing.

Updates by Jason Gedge (email <my last name> at cs mun ca)
    - terminal_string() method
    - minor fixes and changes (mostly to prettyForm)

TODO:
    - Allow left/center/right alignment options for above/below and
      top/center/bottom alignment options for left/right
'''
import shutil
from pretty_symbology import hobj, vobj, xsym, xobj, pretty_use_unicode, line_width, center
from sympy.utilities.exceptions import sympy_deprecation_warning
_GLOBAL_WRAP_LINE = None

class stringPict:
    pass
# WARNING: Decompyle incomplete


class prettyForm(stringPict):
    '''
    Extension of the stringPict class that knows about basic math applications,
    optimizing double minus signs.

    "Binding" is interpreted as follows::

        ATOM this is an atom: never needs to be parenthesized
        FUNC this is a function application: parenthesize if added (?)
        DIV  this is a division: make wider division if divided
        POW  this is a power: only parenthesize if exponent
        MUL  this is a multiplication: parenthesize if powered
        ADD  this is an addition: parenthesize if multiplied or powered
        NEG  this is a negative number: optimize if added, parenthesize if
             multiplied or powered
        OPEN this is an open object: parenthesize if added, multiplied, or
             powered (example: Piecewise)
    '''
    (ATOM, FUNC, DIV, POW, MUL, ADD, NEG, OPEN) = range(8)
    
    def __init__(self, s, baseline, binding, unicode = (0, 0, None)):
        '''Initialize from stringPict and binding power.'''
        stringPict.__init__(self, s, baseline)
        self.binding = binding
    # WARNING: Decompyle incomplete

    unicode = (lambda self: sympy_deprecation_warning('\n            The prettyForm.unicode attribute is deprecated. Use the\n            prettyForm.s attribute instead.\n            ', deprecated_since_version = '1.7', active_deprecations_target = 'deprecated-pretty-printing-functions')self._unicode)()
    
    def __add__(self, *others):
        '''Make a pretty addition.
        Addition of negative numbers is simplified.
        '''
        arg = self
    # WARNING: Decompyle incomplete

    
    def __truediv__(self, den, slashed = (False,)):
        '''Make a pretty division; stacked or slashed.
        '''
        if slashed:
            raise NotImplementedError("Can't do slashed fraction yet")
        num = self
    # WARNING: Decompyle incomplete

    
    def __mul__(self, *others):
        '''Make a pretty multiplication.
        Parentheses are needed around +, - and neg.
        '''
        quantity = {
            'degree': '°' }
        if len(others) == 0:
            return self
        arg = None
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return 'prettyForm(%r,%d,%d)' % ('\n'.join(self.picture), self.baseline, self.binding)

    
    def __pow__(self, b):
        '''Make a pretty power.
        '''
        a = self
        use_inline_func_form = False
    # WARNING: Decompyle incomplete

    simpleFunctions = [
        'sin',
        'cos',
        'tan']
    apply = (lambda function: pass# WARNING: Decompyle incomplete
)()
