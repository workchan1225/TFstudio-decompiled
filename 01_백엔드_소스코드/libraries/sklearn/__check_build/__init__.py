# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Module to give helpful messages to the user that did not
compile scikit-learn properly.
'''
import os
INPLACE_MSG = '\nIt appears that you are importing a local scikit-learn source tree. For\nthis, you need to have an inplace install. Maybe you are in the source\ndirectory and you need to try from another location.'
STANDARD_MSG = '\nIf you have used an installer, please check that it is suited for your\nPython version, your operating system and your platform.'

def raise_build_error(e):
    local_dir = os.path.split(__file__)[0]
    msg = STANDARD_MSG
    if local_dir == 'sklearn/__check_build':
        msg = INPLACE_MSG
    dir_content = list()
    for i, filename in enumerate(os.listdir(local_dir)):
        if (i + 1) % 3:
            dir_content.append(filename.ljust(26))
            continue
        dir_content.append(filename + '\n')
        raise ImportError(f'''{e!s}\n___________________________________________________________________________\nContents of {local_dir!s}:\n{''.join(dir_content).strip()!s}\n___________________________________________________________________________\nIt seems that scikit-learn has not been built correctly.\n\nIf you have installed scikit-learn from source, please do not forget\nto build the package before using it. For detailed instructions, see:\nhttps://scikit-learn.org/dev/developers/advanced_installation.html#building-from-source\n{msg!s}''')


try:
    from sklearn.__check_build._check_build import check_build
    return None
except ImportError:
    e = None
    raise_build_error(e)
    e = None
    del e
    return None
    e = None
    del e
