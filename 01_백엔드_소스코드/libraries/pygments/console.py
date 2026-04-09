# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: console.pyc (Python 3.11)

'''
    pygments.console
    ~~~~~~~~~~~~~~~~

    Format colored console output.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
esc = '\x1b['
codes = { }
codes[''] = ''
codes['reset'] = esc + '39;49;00m'
codes['bold'] = esc + '01m'
codes['faint'] = esc + '02m'
codes['standout'] = esc + '03m'
codes['underline'] = esc + '04m'
codes['blink'] = esc + '05m'
codes['overline'] = esc + '06m'
dark_colors = [
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'gray']
light_colors = [
    'brightblack',
    'brightred',
    'brightgreen',
    'brightyellow',
    'brightblue',
    'brightmagenta',
    'brightcyan',
    'white']
x = 30
for dark, light in zip(dark_colors, light_colors):
    codes[dark] = esc + '%im' % x
    codes[light] = esc + '%im' % (60 + x)
    x += 1
    del dark
    del light
    del x
    codes['white'] = codes['bold']
    
    def reset_color():
        return codes['reset']

    
    def colorize(color_key, text):
        return codes[color_key] + text + codes['reset']

    
    def ansiformat(attr, text):
        '''
    Format ``text`` with a color and/or some attributes::

        color       normal color
        *color*     bold color
        _color_     underlined color
        +color+     blinking color
    '''
        result = []
        if  == attr[:1], attr[-1:] or attr[:1], attr[-1:] == '+':
            pass
        
        result.append(codes['blink'])
        if  == attr[:1], attr[-1:] or attr[:1], attr[-1:] == '*':
            pass
        else:
            attr[1:-1]
        result.append(codes['bold'])
        if  == attr[:1], attr[-1:] or attr[:1], attr[-1:] == '_':
            pass
        else:
            attr[1:-1]
        result.append(codes['underline'])
        result.append(codes[attr])
        result.append(text)
        result.append(codes['reset'])
        return ''.join(result)

    return None
