# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Module with some functions for MathML, like transforming MathML
content in MathML presentation.

To use this module, you will need lxml.
'''
from pathlib import Path
from sympy.utilities.decorator import doctest_depends_on
__doctest_requires__ = {
    ('apply_xsl', 'c2p'): [
        'lxml'] }

def add_mathml_headers(s):
    return '<math xmlns:mml="http://www.w3.org/1998/Math/MathML"\n      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n      xsi:schemaLocation="http://www.w3.org/1998/Math/MathML\n        http://www.w3.org/Math/XMLSchema/mathml2/mathml2.xsd">' + s + '</math>'


def _read_binary(pkgname, filename):
    import sys
    if sys.version_info >= (3, 10):
        files = files
        import importlib.resources
        return files(pkgname).joinpath(filename).read_bytes()
    read_binary = read_binary
    import importlib.resources
    return read_binary(pkgname, filename)


def _read_xsl(xsl):
    if xsl == 'mathml/data/simple_mmlctop.xsl':
        xsl = 'simple_mmlctop.xsl'
    elif xsl == 'mathml/data/mmlctop.xsl':
        xsl = 'mmlctop.xsl'
    elif xsl == 'mathml/data/mmltex.xsl':
        xsl = 'mmltex.xsl'
    if xsl in ('simple_mmlctop.xsl', 'mmlctop.xsl', 'mmltex.xsl'):
        xslbytes = _read_binary('sympy.utilities.mathml.data', xsl)
    else:
        xslbytes = Path(xsl).read_bytes()
    return xslbytes

apply_xsl = (lambda mml, xsl: etree = etreeimport lxmlparser = etree.XMLParser(resolve_entities = False)ac = etree.XSLTAccessControl.DENY_ALLs = etree.XML(_read_xsl(xsl), parser = parser)transform = etree.XSLT(s, access_control = ac)doc = etree.XML(mml, parser = parser)result = transform(doc)s = str(result)s)()
c2p = (lambda mml, simple = (False,): if not mml.startswith('<math'):
mml = add_mathml_headers(mml)if simple:
apply_xsl(mml, 'mathml/data/simple_mmlctop.xsl')None(mml, 'mathml/data/mmlctop.xsl'))()
