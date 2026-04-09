# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pretty_annotate.pyc (Python 3.11)

'''
This module implements code highlighting of numba function annotations.
'''
from warnings import warn
warn('The pretty_annotate functionality is experimental and might change API', FutureWarning)

def hllines(code, style):
    
    try:
        highlight = highlight
        import pygments
        PythonLexer = PythonLexer
        import pygments.lexers
        HtmlFormatter = HtmlFormatter
        import pygments.formatters
    except ImportError:
        raise ImportError("please install the 'pygments' package")

    pylex = PythonLexer()
    hf = HtmlFormatter(noclasses = True, style = style, nowrap = True)
    res = highlight(code, pylex, hf)
    return res.splitlines()


def htlines(code, style):
    
    try:
        highlight = highlight
        import pygments
        PythonLexer = PythonLexer
        import pygments.lexers
        TerminalFormatter = TerminalFormatter
        import pygments.formatters
    except ImportError:
        raise ImportError("please install the 'pygments' package")

    pylex = PythonLexer()
    hf = TerminalFormatter(style = style)
    res = highlight(code, pylex, hf)
    return res.splitlines()


def get_ansi_template():
    
    try:
        Template = Template
        import jinja2
    except ImportError:
        raise ImportError("please install the 'jinja2' package")

    return Template('\n    {%- for func_key in func_data.keys() -%}\n        Function name: \x1b[34m{{func_data[func_key][\'funcname\']}}\x1b[39;49;00m\n        {%- if func_data[func_key][\'filename\'] -%}\n        {{\'\n\'}}In file: \x1b[34m{{func_data[func_key][\'filename\'] -}}\x1b[39;49;00m\n        {%- endif -%}\n        {{\'\n\'}}With signature: \x1b[34m{{func_key[1]}}\x1b[39;49;00m\n        {{- "\n" -}}\n        {%- for num, line, hl, hc in func_data[func_key][\'pygments_lines\'] -%}\n                {{-\'\n\'}}{{ num}}: {{hc-}}\n                {%- if func_data[func_key][\'ir_lines\'][num] -%}\n                    {%- for ir_line, ir_line_type in func_data[func_key][\'ir_lines\'][num] %}\n                        {{-\'\n\'}}--{{- \' \'*func_data[func_key][\'python_indent\'][num]}}\n                        {{- \' \'*(func_data[func_key][\'ir_indent\'][num][loop.index0]+4)\n                        }}{{ir_line }}\x1b[41m{{ir_line_type-}}\x1b[39;49;00m\n                    {%- endfor -%}\n                {%- endif -%}\n            {%- endfor -%}\n    {%- endfor -%}\n    ')


def get_html_template():
    
    try:
        Template = Template
        import jinja2
    except ImportError:
        raise ImportError("please install the 'jinja2' package")

    return Template('\n    <html>\n    <head>\n        <style>\n\n            .annotation_table {\n                color: #000000;\n                font-family: monospace;\n                margin: 5px;\n                width: 100%;\n            }\n\n            /* override JupyterLab style */\n            .annotation_table td {\n                text-align: left;\n                background-color: transparent; \n                padding: 1px;\n            }\n\n            .annotation_table tbody tr:nth-child(even) {\n                background: white;\n            }\n\n            .annotation_table code\n            {\n                background-color: transparent; \n                white-space: normal;\n            }\n\n            /* End override JupyterLab style */\n\n            tr:hover {\n                background-color: rgba(92, 200, 249, 0.25);\n            }\n\n            td.object_tag summary ,\n            td.lifted_tag summary{\n                font-weight: bold;\n                display: list-item;\n            }\n\n            span.lifted_tag {\n                color: #00cc33;\n            }\n\n            span.object_tag {\n                color: #cc3300;\n            }\n\n\n            td.lifted_tag {\n                background-color: #cdf7d8;\n            }\n\n            td.object_tag {\n                background-color: #fef5c8;\n            }\n\n            code.ir_code {\n                color: grey;\n                font-style: italic;\n            }\n\n            .metadata {\n                border-bottom: medium solid black;\n                display: inline-block;\n                padding: 5px;\n                width: 100%;\n            }\n\n            .annotations {\n                padding: 5px;\n            }\n\n            .hidden {\n                display: none;\n            }\n\n            .buttons {\n                padding: 10px;\n                cursor: pointer;\n            }\n        </style>\n    </head>\n\n    <body>\n        {% for func_key in func_data.keys() %}\n            <div class="metadata">\n            Function name: {{func_data[func_key][\'funcname\']}}<br />\n            {% if func_data[func_key][\'filename\'] %}\n                in file: {{func_data[func_key][\'filename\']|escape}}<br />\n            {% endif %}\n            with signature: {{func_key[1]|e}}\n            </div>\n            <div class="annotations">\n            <table class="annotation_table tex2jax_ignore">\n                {%- for num, line, hl, hc in func_data[func_key][\'pygments_lines\'] -%}\n                    {%- if func_data[func_key][\'ir_lines\'][num] %}\n                        <tr><td style="text-align:left;" class="{{func_data[func_key][\'python_tags\'][num]}}">\n                            <details>\n                                <summary>\n                                    <code>\n                                    {{num}}:\n                                    {{\'&nbsp;\'*func_data[func_key][\'python_indent\'][num]}}{{hl}}\n                                    </code>\n                                </summary>\n                                <table class="annotation_table">\n                                    <tbody>\n                                        {%- for ir_line, ir_line_type in func_data[func_key][\'ir_lines\'][num] %}\n                                            <tr class="ir_code">\n                                                <td style="text-align: left;"><code>\n                                                &nbsp;\n                                                {{- \'&nbsp;\'*func_data[func_key][\'python_indent\'][num]}}\n                                                {{ \'&nbsp;\'*func_data[func_key][\'ir_indent\'][num][loop.index0]}}{{ir_line|e -}}\n                                                <span class="object_tag">{{ir_line_type}}</span>\n                                                </code>\n                                                </td>\n                                            </tr>\n                                        {%- endfor -%}\n                                    </tbody>\n                                </table>\n                                </details>\n                        </td></tr>\n                    {% else -%}\n                        <tr><td style="text-align:left; padding-left: 22px;" class="{{func_data[func_key][\'python_tags\'][num]}}">\n                            <code>\n                                {{num}}:\n                                {{\'&nbsp;\'*func_data[func_key][\'python_indent\'][num]}}{{hl}}\n                            </code>\n                        </td></tr>\n                    {%- endif -%}\n                {%- endfor -%}\n            </table>\n            </div>\n        {% endfor %}\n    </body>\n    </html>\n    ')


def reform_code(annotation):
    '''
    Extract the code from the Numba annotation datastructure. 

    Pygments can only highlight full multi-line strings, the Numba
    annotation is list of single lines, with indentation removed.
    '''
    ident_dict = annotation['python_indent']
    s = ''
    for n, l in annotation['python_lines']:
        s = s + ' ' * ident_dict[n] + l + '\n'
        return s


class Annotate:
    '''
    Construct syntax highlighted annotation for a given jitted function:

    Example:

    >>> import numba
    >>> from numba.pretty_annotate import Annotate
    >>> @numba.jit
    ... def test(q):
    ...     res = 0
    ...     for i in range(q):
    ...         res += i
    ...     return res
    ...
    >>> test(10)
    45
    >>> Annotate(test)

    The last line will return an HTML and/or ANSI representation that will be
    displayed accordingly in Jupyter/IPython.

    Function annotations persist across compilation for newly encountered
    type signatures and as a result annotations are shown for all signatures
    by default.

    Annotations for a specific signature can be shown by using the
    ``signature`` parameter.

    >>> @numba.jit
    ... def add(x, y):
    ...     return x + y
    ...
    >>> add(1, 2)
    3
    >>> add(1.3, 5.7)
    7.0
    >>> add.signatures
    [(int64, int64), (float64, float64)]
    >>> Annotate(add, signature=add.signatures[1])  # annotation for (float64, float64)
    '''
    
    def __init__(self, function, signature = (None,), **kwargs):
        style = kwargs.get('style', 'default')
        if not function.signatures:
            raise ValueError('function need to be jitted for at least one signature')
        ann = function.get_annotation_info(signature = signature)
        self.ann = ann
        for k, v in ann.items():
            res = hllines(reform_code(v), style)
            rest = htlines(reform_code(v), style)
            v['pygments_lines'] = zip(v['python_lines'], res, rest)()
            return None

    
    def _repr_html_(self):
        return get_html_template().render(func_data = self.ann)

    
    def __repr__(self):
        return get_ansi_template().render(func_data = self.ann)
