# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text.pyc (Python 3.11)

'''
Simple text manipulation functions.

The :mod:`~humanfriendly.text` module contains simple functions to manipulate text:

- The :func:`concatenate()` and :func:`pluralize()` functions make it easy to
  generate human friendly output.

- The :func:`format()`, :func:`compact()` and :func:`dedent()` functions
  provide a clean and simple to use syntax for composing large text fragments
  with interpolated variables.

- The :func:`tokenize()` function parses simple user input.
'''
import numbers
import random
import re
import string
import textwrap
__all__ = ('compact', 'compact_empty_lines', 'concatenate', 'dedent', 'format', 'generate_slug', 'is_empty_line', 'join_lines', 'pluralize', 'pluralize_raw', 'random_string', 'split', 'split_paragraphs', 'tokenize', 'trim_empty_lines')

def compact(text, *args, **kw):
    '''
    Compact whitespace in a string.

    Trims leading and trailing whitespace, replaces runs of whitespace
    characters with a single space and interpolates any arguments using
    :func:`format()`.

    :param text: The text to compact (a string).
    :param args: Any positional arguments are interpolated using :func:`format()`.
    :param kw: Any keyword arguments are interpolated using :func:`format()`.
    :returns: The compacted text (a string).

    Here\'s an example of how I like to use the :func:`compact()` function, this
    is an example from a random unrelated project I\'m working on at the moment::

        raise PortDiscoveryError(compact("""
            Failed to discover port(s) that Apache is listening on!
            Maybe I\'m parsing the wrong configuration file? ({filename})
        """, filename=self.ports_config))

    The combination of :func:`compact()` and Python\'s multi line strings allows
    me to write long text fragments with interpolated variables that are easy
    to write, easy to read and work well with Python\'s whitespace
    sensitivity.
    '''
    non_whitespace_tokens = text.split()
    compacted_text = ' '.join(non_whitespace_tokens)
# WARNING: Decompyle incomplete


def compact_empty_lines(text):
    '''
    Replace repeating empty lines with a single empty line (similar to ``cat -s``).

    :param text: The text in which to compact empty lines (a string).
    :returns: The text with empty lines compacted (a string).
    '''
    i = 0
    lines = text.splitlines(True)
# WARNING: Decompyle incomplete


def concatenate(items, conjunction, serial_comma = ('and', False)):
    '''
    Concatenate a list of items in a human friendly way.

    :param items:

        A sequence of strings.

    :param conjunction:

        The word to use before the last item (a string, defaults to "and").

    :param serial_comma:

        :data:`True` to use a `serial comma`_, :data:`False` otherwise
        (defaults to :data:`False`).

    :returns:

        A single string.

    >>> from humanfriendly.text import concatenate
    >>> concatenate(["eggs", "milk", "bread"])
    \'eggs, milk and bread\'

    .. _serial comma: https://en.wikipedia.org/wiki/Serial_comma
    '''
    items = list(items)
    if len(items) > 1:
        final_item = items.pop()
        formatted = ', '.join(items)
        if serial_comma:
            formatted += ','
        return ' '.join([
            formatted,
            conjunction,
            final_item])
    if None:
        return items[0]


def dedent(text, *args, **kw):
    """
    Dedent a string (remove common leading whitespace from all lines).

    Removes common leading whitespace from all lines in the string using
    :func:`textwrap.dedent()`, removes leading and trailing empty lines using
    :func:`trim_empty_lines()` and interpolates any arguments using
    :func:`format()`.

    :param text: The text to dedent (a string).
    :param args: Any positional arguments are interpolated using :func:`format()`.
    :param kw: Any keyword arguments are interpolated using :func:`format()`.
    :returns: The dedented text (a string).

    The :func:`compact()` function's documentation contains an example of how I
    like to use the :func:`compact()` and :func:`dedent()` functions. The main
    difference is that I use :func:`compact()` for text that will be presented
    to the user (where whitespace is not so significant) and :func:`dedent()`
    for data file and code generation tasks (where newlines and indentation are
    very significant).
    """
    dedented_text = textwrap.dedent(text)
    trimmed_text = trim_empty_lines(dedented_text)
# WARNING: Decompyle incomplete


def format(text, *args, **kw):
    '''
    Format a string using the string formatting operator and/or :meth:`str.format()`.

    :param text: The text to format (a string).
    :param args: Any positional arguments are interpolated into the text using
                 the string formatting operator (``%``). If no positional
                 arguments are given no interpolation is done.
    :param kw: Any keyword arguments are interpolated into the text using the
               :meth:`str.format()` function. If no keyword arguments are given
               no interpolation is done.
    :returns: The text with any positional and/or keyword arguments
              interpolated (a string).

    The implementation of this function is so trivial that it seems silly to
    even bother writing and documenting it. Justifying this requires some
    context :-).

    **Why format() instead of the string formatting operator?**

    For really simple string interpolation Python\'s string formatting operator
    is ideal, but it does have some strange quirks:

    - When you switch from interpolating a single value to interpolating
      multiple values you have to wrap them in tuple syntax. Because
      :func:`format()` takes a `variable number of arguments`_ it always
      receives a tuple (which saves me a context switch :-). Here\'s an
      example:

      >>> from humanfriendly.text import format
      >>> # The string formatting operator.
      >>> print(\'the magic number is %s\' % 42)
      the magic number is 42
      >>> print(\'the magic numbers are %s and %s\' % (12, 42))
      the magic numbers are 12 and 42
      >>> # The format() function.
      >>> print(format(\'the magic number is %s\', 42))
      the magic number is 42
      >>> print(format(\'the magic numbers are %s and %s\', 12, 42))
      the magic numbers are 12 and 42

    - When you interpolate a single value and someone accidentally passes in a
      tuple your code raises a :exc:`~exceptions.TypeError`. Because
      :func:`format()` takes a `variable number of arguments`_ it always
      receives a tuple so this can never happen. Here\'s an example:

      >>> # How expecting to interpolate a single value can fail.
      >>> value = (12, 42)
      >>> print(\'the magic value is %s\' % value)
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
      TypeError: not all arguments converted during string formatting
      >>> # The following line works as intended, no surprises here!
      >>> print(format(\'the magic value is %s\', value))
      the magic value is (12, 42)

    **Why format() instead of the str.format() method?**

    When you\'re doing complex string interpolation the :meth:`str.format()`
    function results in more readable code, however I frequently find myself
    adding parentheses to force evaluation order. The :func:`format()` function
    avoids this because of the relative priority between the comma and dot
    operators. Here\'s an example:

    >>> "{adjective} example" + " " + "(can\'t think of anything less {adjective})".format(adjective=\'silly\')
    "{adjective} example (can\'t think of anything less silly)"
    >>> ("{adjective} example" + " " + "(can\'t think of anything less {adjective})").format(adjective=\'silly\')
    "silly example (can\'t think of anything less silly)"
    >>> format("{adjective} example" + " " + "(can\'t think of anything less {adjective})", adjective=\'silly\')
    "silly example (can\'t think of anything less silly)"

    The :func:`compact()` and :func:`dedent()` functions are wrappers that
    combine :func:`format()` with whitespace manipulation to make it easy to
    write nice to read Python code.

    .. _variable number of arguments: https://docs.python.org/2/tutorial/controlflow.html#arbitrary-argument-lists
    '''
    if args:
        text %= args
# WARNING: Decompyle incomplete


def generate_slug(text, delimiter = ('-',)):
    '''
    Convert text to a normalized "slug" without whitespace.

    :param text: The original text, for example ``Some Random Text!``.
    :param delimiter: The delimiter used to separate words
                      (defaults to the ``-`` character).
    :returns: The slug text, for example ``some-random-text``.
    :raises: :exc:`~exceptions.ValueError` when the provided
             text is nonempty but results in an empty slug.
    '''
    slug = text.lower()
    escaped = delimiter.replace('\\', '\\\\')
    slug = re.sub('[^a-z0-9]+', escaped, slug)
    slug = slug.strip(delimiter)
    if not text and slug:
        msg = 'The provided text %r results in an empty slug!'
        raise ValueError(format(msg, text))
    return slug


def is_empty_line(text):
