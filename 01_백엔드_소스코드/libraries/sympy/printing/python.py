# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: python.pyc (Python 3.11)

import keyword as kw
import sympy
from repr import ReprPrinter
from str import StrPrinter
STRPRINT = ('Add', 'Infinity', 'Integer', 'Mul', 'NegativeInfinity', 'Pow')

class PythonPrinter(StrPrinter, ReprPrinter):
    pass
# WARNING: Decompyle incomplete


def python(expr, **settings):
    '''Return Python interpretation of passed expression
    (can be passed to the exec() function without any modifications)'''
    printer = PythonPrinter(settings)
    exprp = printer.doprint(expr)
    result = ''
    renamings = { }
    for symbolname in printer.symbols:
        if '{' in symbolname:
            newsymbolname = symbolname.replace('{', '').replace('}', '')
            renamings[sympy.Symbol(symbolname)] = newsymbolname
        else:
            newsymbolname = symbolname
        if kw.iskeyword(newsymbolname):
            newsymbolname += '_'
            if newsymbolname not in printer.symbols and newsymbolname not in printer.functions:
                renamings[sympy.Symbol(symbolname)] = sympy.Symbol(newsymbolname)
            
        result += newsymbolname + " = Symbol('" + symbolname + "')\n"
        for functionname in printer.functions:
            newfunctionname = functionname
            if kw.iskeyword(newfunctionname):
                newfunctionname += '_'
                if newfunctionname not in printer.symbols and newfunctionname not in printer.functions:
                    renamings[sympy.Function(functionname)] = sympy.Function(newfunctionname)
                
            result += newfunctionname + " = Function('" + functionname + "')\n"
            if renamings:
                exprp = expr.subs(renamings)
    result += 'e = ' + printer._str(exprp)
    return result


def print_python(expr, **settings):
    '''Print output of python() function'''
    pass
# WARNING: Decompyle incomplete
