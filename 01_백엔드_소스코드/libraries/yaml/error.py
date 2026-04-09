# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: error.pyc (Python 3.11)

__all__ = [
    'Mark',
    'YAMLError',
    'MarkedYAMLError']

class Mark:
    
    def __init__(self, name, index, line, column, buffer, pointer):
        self.name = name
        self.index = index
        self.line = line
        self.column = column
        self.buffer = buffer
        self.pointer = pointer

    
    def get_snippet(self, indent, max_length = (4, 75)):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        snippet = self.get_snippet()
        where = '  in "%s", line %d, column %d' % (self.name, self.line + 1, self.column + 1)
    # WARNING: Decompyle incomplete



class YAMLError(Exception):
    pass


class MarkedYAMLError(YAMLError):
    
    def __init__(self, context, context_mark, problem, problem_mark, note = (None, None, None, None, None)):
        self.context = context
        self.context_mark = context_mark
        self.problem = problem
        self.problem_mark = problem_mark
        self.note = note

    
    def __str__(self):
        lines = []
    # WARNING: Decompyle incomplete
