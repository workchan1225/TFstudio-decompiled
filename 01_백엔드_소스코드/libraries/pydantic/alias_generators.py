# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: alias_generators.pyc (Python 3.11)

'''Alias generators for converting between different capitalization conventions.'''
import re
__all__ = ('to_pascal', 'to_camel', 'to_snake')

def to_pascal(snake = None):
    '''Convert a snake_case string to PascalCase.

    Args:
        snake: The string to convert.

    Returns:
        The PascalCase string.
    '''
    camel = snake.title()
    return re.sub('([0-9A-Za-z])_(?=[0-9A-Z])', (lambda m: m.group(1)), camel)


def to_camel(snake = None):
    '''Convert a snake_case string to camelCase.

    Args:
        snake: The string to convert.

    Returns:
        The converted camelCase string.
    '''
    if not re.match('^[a-z]+[A-Za-z0-9]*$', snake) and re.search('\\d[a-z]', snake):
        return snake
    camel = None(snake)
    return re.sub('(^_*[A-Z])', (lambda m: m.group(1).lower()), camel)


def to_snake(camel = None):
    '''Convert a PascalCase, camelCase, or kebab-case string to snake_case.

    Args:
        camel: The string to convert.

    Returns:
        The converted string in snake_case.
    '''
    snake = re.sub('([A-Z]+)([A-Z][a-z])', (lambda m: f'''{m.group(1)}_{m.group(2)}'''), camel)
    snake = re.sub('([a-z])([A-Z])', (lambda m: f'''{m.group(1)}_{m.group(2)}'''), snake)
    snake = re.sub('([0-9])([A-Z])', (lambda m: f'''{m.group(1)}_{m.group(2)}'''), snake)
    snake = re.sub('([a-z])([0-9])', (lambda m: f'''{m.group(1)}_{m.group(2)}'''), snake)
    snake = snake.replace('-', '_')
    return snake.lower()
