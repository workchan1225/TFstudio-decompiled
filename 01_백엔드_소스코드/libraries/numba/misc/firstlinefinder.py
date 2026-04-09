# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: firstlinefinder.pyc (Python 3.11)

'''
This module provides helper functions to find the first line of a function
body.
'''
import ast
import inspect
import textwrap

class FindDefFirstLine(ast.NodeVisitor):
    pass
# WARNING: Decompyle incomplete


def _is_docstring(node):
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
        return True


def get_func_body_first_lineno(pyfunc):
    '''
    Look up the first line of function body using the file in
    ``pyfunc.__code__.co_filename``.

    Returns
    -------
    lineno : int; or None
        The first line number of the function body; or ``None`` if the first
        line cannot be determined.
    '''
    co = pyfunc.__code__
    
    try:
        fin = open(co.co_filename)
        source = fin.read()
        offset = 0
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        pass
                    except (FileNotFoundError, OSError):
                        (lines, offset) = inspect.getsourcelines(pyfunc)
                        source = ''.join(lines)
                        offset = offset - 1
                    except (OSError, TypeError):
                        return None


                tree = ast.parse(textwrap.dedent(source))
                finder = FindDefFirstLine(co.co_name, co.co_firstlineno - offset)
                finder.visit(tree)
                if finder.first_stmt_line:
                    return finder.first_stmt_line + offset
                return None
