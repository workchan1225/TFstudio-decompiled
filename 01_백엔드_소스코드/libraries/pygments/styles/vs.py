# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vs.pyc (Python 3.11)

'''
    pygments.styles.vs
    ~~~~~~~~~~~~~~~~~~

    Simple style with MS Visual Studio colors.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Operator, Generic
__all__ = [
    'VisualStudioStyle']

class VisualStudioStyle(Style):
    name = 'vs'
    background_color = '#ffffff'
    styles = {
        Error: 'border:#FF0000',
        Generic.Prompt: 'bold',
        Generic.EmphStrong: 'bold italic',
        Generic.Strong: 'bold',
        Generic.Emph: 'italic',
        Generic.Subheading: 'bold',
        Generic.Heading: 'bold',
        String: '#a31515',
        Name.Class: '#2b91af',
        Keyword.Type: '#2b91af',
        Operator.Word: '#0000ff',
        Keyword: '#0000ff',
        Comment.Preproc: '#0000ff',
        Comment: '#008000' }
