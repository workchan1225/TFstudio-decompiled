# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''

uritemplate
===========

URI templates implemented as close to :rfc:`6570` as possible

See http://uritemplate.rtfd.org/ for documentation

:copyright:
    (c) 2013 Ian Stapleton Cordasco
:license:
    Modified BSD Apache License (Version 2.0), see LICENSE for more details
    and either LICENSE.BSD or LICENSE.APACHE for the details of those specific
    licenses

'''
__title__ = 'uritemplate'
__author__ = 'Ian Stapleton Cordasco'
__license__ = 'Modified BSD or Apache License, Version 2.0'
__copyright__ = 'Copyright 2013 Ian Stapleton Cordasco'
__version__ = '4.2.0'
__version_info__ = (lambda .0: pass# WARNING: Decompyle incomplete
)(__version__.split('.')())
from uritemplate.api import URITemplate
from uritemplate.api import expand
from uritemplate.api import partial
from uritemplate.api import variables
__all__ = ('URITemplate', 'expand', 'partial', 'variables')
