# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rest.pyc (Python 3.11)

'''ReST-style docstring parsing.'''
import inspect
import re
import typing as T
from common import DEPRECATION_KEYWORDS, PARAM_KEYWORDS, RAISES_KEYWORDS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, Docstring, DocstringDeprecated, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns, DocstringStyle, ParseError, RenderingStyle

def _build_meta(args = None, desc = None):
    key = args[0]
    if key in PARAM_KEYWORDS:
        if len(args) == 3:
            (key, type_name, arg_name) = args
            if type_name.endswith('?'):
                is_optional = True
                type_name = type_name[:-1]
            else:
                is_optional = False
        elif len(args) == 2:
            (key, arg_name) = args
            type_name = None
            is_optional = None
        else:
            raise ParseError(f'''Expected one or two arguments for a {key} keyword.''')
        match = re.match('.*defaults to (.+)', desc, flags = re.DOTALL)
        default = match.group(1).rstrip('.') if match else None
        return DocstringParam(args = args, description = desc, arg_name = arg_name, type_name = type_name, is_optional = is_optional, default = default)
    if None in RETURNS_KEYWORDS | YIELDS_KEYWORDS:
        if len(args) == 2:
            type_name = args[1]
        elif len(args) == 1:
            type_name = None
        else:
            raise ParseError(f'''Expected one or no arguments for a {key} keyword.''')
        return DocstringReturns(args = args, description = desc, type_name = type_name, is_generator = key in YIELDS_KEYWORDS)
    if None in DEPRECATION_KEYWORDS:
        match = re.search('^(?P<version>v?((?:\\d+)(?:\\.[0-9a-z\\.]+))) (?P<desc>.+)', desc, flags = re.I)
        return DocstringDeprecated(args = args, version = match.group('version') if match else None, description = match.group('desc') if match else desc)
    if None in RAISES_KEYWORDS:
        if len(args) == 2:
            type_name = args[1]
        elif len(args) == 1:
            type_name = None
        else:
            raise ParseError(f'''Expected one or no arguments for a {key} keyword.''')
        return DocstringRaises(args = args, description = desc, type_name = type_name)
    return None(args = args, description = desc)


def parse(text = None):
    '''Parse the ReST-style docstring into its components.

    :returns: parsed docstring
    '''
    ret = Docstring(style = DocstringStyle.REST)
    if not text:
        return ret
    text = None.cleandoc(text)
    match = re.search('^:', text, flags = re.M)
    if match:
        desc_chunk = None[text:match.start()]
        meta_chunk = text[match.start():]
    else:
        desc_chunk = text
        meta_chunk = ''
    parts = desc_chunk.split('\n', 1)
    if not parts[0]:
        ret.short_description = None
        if len(parts) > 1:
            if not parts[1]:
                long_desc_chunk = ''
                ret.blank_after_short_description = long_desc_chunk.startswith('\n')
                ret.blank_after_long_description = long_desc_chunk.endswith('\n\n')
                if not long_desc_chunk.strip():
                    ret.long_description = None
                    types = { }
                    rtypes = { }
                    for match in re.finditer('(^:.*?)(?=^:|\\Z)', meta_chunk, flags = re.S | re.M):
                        chunk = match.group(0)
                        if not chunk:
                            continue
                        (args_chunk, desc_chunk) = chunk.lstrip(':').split(':', 1)
                    except ValueError:
                        ex = None
                        raise ParseError(f'''Error parsing meta information near "{chunk}".'''), ex
                        ex = None
                        del ex
                    args = args_chunk.split()
                    desc = desc_chunk.strip()
                    if '\n' in desc:
                        (first_line, rest) = desc.split('\n', 1)
                        desc = first_line + '\n' + inspect.cleandoc(rest)
    if len(args) == 2 and args[0] == 'type':
        types[args[1]] = desc
        continue
    if len(args) in (1, 2) and args[0] == 'rtype':
        rtypes[None if len(args) == 1 else args[1]] = desc
        continue
    ret.meta.append(_build_meta(args, desc))
    continue
    for meta in ret.meta:
        if isinstance(meta, DocstringParam):
            if not meta.type_name:
                meta.type_name = types.get(meta.arg_name)
                continue
                if isinstance(meta, DocstringReturns):
                    if not meta.type_name:
                        meta.type_name = rtypes.get(meta.return_name)
                        continue
                        if (lambda .0: pass# WARNING: Decompyle incomplete
)(ret.meta()) and rtypes:
                            for return_name, type_name in rtypes.items():
                                ret.meta.append(DocstringReturns(args = [], type_name = type_name, description = None, is_generator = False, return_name = return_name))
                                return ret


def compose(docstring = None, rendering_style = None, indent = None):
    '''Render a parsed docstring into docstring text.

    :param docstring: parsed docstring representation
    :param rendering_style: the style to render docstrings
    :param indent: the characters used as indentation in the docstring string
    :returns: docstring text
    '''
    pass
# WARNING: Decompyle incomplete
