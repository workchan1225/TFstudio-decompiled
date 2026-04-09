# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: templite.pyc (Python 3.11)

'''A simple Python template renderer, for a nano-subset of Django syntax.

For a detailed discussion of this code, see this chapter from 500 Lines:
http://aosabook.org/en/500L/a-template-engine.html

'''
from __future__ import annotations
import re
from typing import Any, Callable, NoReturn, cast

class TempliteSyntaxError(ValueError):
    '''Raised when a template has a syntax error.'''
    pass


class TempliteValueError(ValueError):
    """Raised when an expression won't evaluate in a template."""
    pass


class CodeBuilder:
    '''Build source code conveniently.'''
    
    def __init__(self = None, indent = None):
        self.code = []
        self.indent_level = indent

    
    def __str__(self = None):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.code())

    
    def add_line(self = None, line = None):
        """Add a line of source to the code.

        Indentation and newline will be added for you, don't provide them.

        """
        self.code.extend([
            ' ' * self.indent_level,
            line,
            '\n'])

    
    def add_section(self = None):
        '''Add a section, a sub-CodeBuilder.'''
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

    INDENT_STEP = 4
    
    def indent(self = None):
        '''Increase the current indent for following lines.'''
        pass

    
    def dedent(self = None):
        '''Decrease the current indent for following lines.'''
        pass

    
    def get_globals(self = None):
        '''Execute the code, and return a dict of globals it defines.'''
        pass
    # WARNING: Decompyle incomplete



class Templite:
    '''A simple template renderer, for a nano-subset of Django syntax.

    Supported constructs are extended variable access::

        {{var.modifier.modifier|filter|filter}}

    loops::

        {% for var in list %}...{% endfor %}

    and ifs::

        {% if var %}...{% endif %}

    if-else::

        {% if var %}...{% else %}...{% endif %}

    Comments are within curly-hash markers::

        {# This will be ignored #}

    Lines between `{% joined %}` and `{% endjoined %}` will have lines stripped
    and joined.  Be careful, this could join words together!

    Any of these constructs can have a hyphen at the end (`-}}`, `-%}`, `-#}`),
    which will collapse the white space following the tag.

    Construct a Templite with the template text, then use `render` against a
    dictionary context to create a finished string::

        templite = Templite(\'\'\'
            <h1>Hello {{name|upper}}!</h1>
            {% for topic in topics %}
                <p>You are interested in {{topic}}.</p>
            {% endif %}
            \'\'\',
            {"upper": str.upper},
        )
        text = templite.render({
            "name": "Ned",
            "topics": ["Python", "Geometry", "Juggling"],
        })

    '''
    
    def __init__(self = None, text = None, *contexts):
        '''Construct a Templite with the given `text`.

        `contexts` are dictionaries of values to use for future renderings.
        These are good for filters and global values.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _expr_code(self = None, expr = None):
        '''Generate a Python expression for `expr`.'''
        if '|' in expr:
            pipes = expr.split('|')
            code = self._expr_code(pipes[0])
            for func in pipes[1:]:
                self._variable(func, self.all_vars)
                code = f'''c_{func}({code})'''
        return code

    
    def _syntax_error(self = None, msg = None, thing = None):
        '''Raise a syntax error using `msg`, and showing `thing`.'''
        raise TempliteSyntaxError(f'''{msg}: {thing!r}''')

    
    def _variable(self = None, name = None, vars_set = None):
        '''Track that `name` is used as a variable.

        Adds the name to `vars_set`, a set of variable names.

        Raises an syntax error if `name` is not a valid name.

        '''
        if not re.match('[_a-zA-Z][_a-zA-Z0-9]*$', name):
            self._syntax_error('Not a valid name', name)
        vars_set.add(name)

    
    def render(self = None, context = None):
        '''Render this template by applying it to `context`.

        `context` is a dictionary of values to use in this rendering.

        '''
        render_context = dict(self.context)
        if context:
            render_context.update(context)
        return self._render_function(render_context, self._do_dots)

    
    def _do_dots(self = None, value = None, *dots):
        '''Evaluate dotted expressions at run-time.'''
        for dot in dots:
            value = getattr(value, dot)
        except AttributeError:
            value = value[dot]
        except (TypeError, KeyError):
            exc = None
            raise TempliteValueError(f'''Couldn\'t evaluate {value!r}.{dot}'''), exc
            exc = None
            del exc
