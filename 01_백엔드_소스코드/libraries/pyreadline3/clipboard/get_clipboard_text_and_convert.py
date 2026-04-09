# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: get_clipboard_text_and_convert.pyc (Python 3.11)

from typing import Any, List, Tuple
from api import get_clipboard_text

def _make_num(x = None):
    
    try:
        return int(x)
    except ValueError:
        return 
        except ValueError:
            return 
            except ValueError:
                return 



def _make_list_of_list(txt = None):
    ut = []
    flag = False
    for line in txt.split('\r\n')():
        words = line.split('\t')()
        if str in list(map(type, words)):
            flag = True
        ut.append(words)
        return (ut, flag)


def get_clipboard_text_and_convert(paste_list = None):
    '''Get txt from clipboard. if paste_list==True the convert tab separated
    data to list of lists. Enclose list of list in array() if all elements are
    numeric'''
    txt = get_clipboard_text()
    if not txt:
        return ''
    if not None:
        return txt
    if None not in txt:
        return txt
    (array, flag) = None(txt)
    if flag:
        txt = repr(array)
    else:
        txt = 'array(%s)' % repr(array)
    txt = (lambda .0: pass# WARNING: Decompyle incomplete
)(txt())
    return txt
