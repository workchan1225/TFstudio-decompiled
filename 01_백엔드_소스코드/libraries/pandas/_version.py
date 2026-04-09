# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _version.pyc (Python 3.11)

'''Git implementation of _version.py.'''
from collections.abc import Callable
import errno
import functools
import os
import re
import subprocess
import sys

def get_keywords():
    '''Get the keywords needed to look up the version information.'''
    git_refnames = ' (HEAD, tag: v3.0.0, origin/main)'
    git_full = '366ccdfcd8ed1e5543bfb6d4ee0c9bc519898670'
    git_date = '2026-01-21 14:43:14 +0100'
    keywords = {
        'refnames': git_refnames,
        'full': git_full,
        'date': git_date }
    return keywords


class VersioneerConfig:
    '''Container for Versioneer configuration parameters.'''
    pass


def get_config():
    '''Create, populate and return the VersioneerConfig() object.'''
    cfg = VersioneerConfig()
    cfg.VCS = 'git'
    cfg.style = 'pep440'
    cfg.tag_prefix = 'v'
    cfg.parentdir_prefix = 'pandas-'
    cfg.versionfile_source = 'pandas/_version.py'
    cfg.verbose = False
    return cfg


class NotThisMethod(Exception):
    '''Exception raised if a method is not valid for the current scenario.'''
    pass

LONG_VERSION_PY: dict[(str, str)] = { }
HANDLERS: dict[(str, dict[(str, Callable)])] = { }

def register_vcs_handler(vcs, method):
    '''Create decorator to mark a method as the handler of a VCS.'''
    pass
# WARNING: Decompyle incomplete


def run_command(commands, args, cwd, verbose, hide_stderr, env = (None, False, False, None)):
    '''Call the given command(s).'''
    pass
# WARNING: Decompyle incomplete


def versions_from_parentdir(parentdir_prefix, root, verbose):
    '''Try to determine the version from the parent directory name.

    Source tarballs conventionally unpack into a directory that includes both
    the project name and a version string. We will also support searching up
    two directory levels for an appropriately named parent directory
    '''
    rootdirs = []
    for _ in range(3):
        dirname = os.path.basename(root)
        if dirname.startswith(parentdir_prefix):
            
            return None, {
                'version': dirname[len(parentdir_prefix):],
                'full-revisionid': None,
                'dirty': False,
                'error': None,
                'date': None }
        None.append(root)
        if verbose:
            print(f'''Tried directories {rootdirs!s}             but none started with prefix {parentdir_prefix}''')
    raise NotThisMethod("rootdir doesn't start with parentdir_prefix")

git_get_keywords = (lambda versionfile_abs: keywords = { }try:
fobj = open(versionfile_abs, encoding = 'utf-8')for line in fobj:
if line.strip().startswith('git_refnames ='):
mo = re.search('=\\s*"(.*)"', line)if mo:
keywords['refnames'] = mo.group(1)if line.strip().startswith('git_full ='):
mo = re.search('=\\s*"(.*)"', line)if mo:
keywords['full'] = mo.group(1)if line.strip().startswith('git_date ='):
mo = re.search('=\\s*"(.*)"', line)if mo:
keywords['date'] = mo.group(1)try:
None(None, None)with None:
if not None:
try:
try:
passexcept OSError:
passkeywords)()
git_versions_from_keywords = (lambda keywords, tag_prefix, verbose: pass# WARNING: Decompyle incomplete
)()
git_pieces_from_vcs = (lambda tag_prefix, root, verbose, runner = (run_command,): GITS = [
'git']if sys.platform == 'win32':
GITS = [
'git.cmd',
'git.exe']env = os.environ.copy()env.pop('GIT_DIR', None)runner = functools.partial(runner, env = env)(_, rc) = runner(GITS, [
'rev-parse',
'--git-dir'], cwd = root, hide_stderr = not verbose)if rc != 0:
if verbose:
print(f'''Directory {root} not under git control''')raise NotThisMethod("'git rev-parse --git-dir' returned error")(describe_out, rc) = runner(GITS, [
'describe',
'--tags',
'--dirty',
'--always',
'--long',
'--match',
f'''{tag_prefix}[[:digit:]]*'''], cwd = root)# WARNING: Decompyle incomplete
)()

def plus_or_dot(pieces = register_vcs_handler('git', 'get_keywords')):
    """Return a + if we don't already have one, else return a ."""
    if '+' in pieces.get('closest-tag', ''):
        return '.'


def render_pep440(pieces):
    '''Build up version string, with post-release "local version identifier".

    Our goal: TAG[+DISTANCE.gHEX[.dirty]] . Note that if you
    get a tagged build and then dirty it, you\'ll get TAG+0.gHEX.dirty

    Exceptions:
    1: no tags. git_describe was just HEX. 0+untagged.DISTANCE.gHEX[.dirty]
    '''
    if pieces['closest-tag']:
        rendered = pieces['closest-tag']
        if pieces['distance'] or pieces['dirty']:
            rendered += plus_or_dot(pieces)
            rendered += f'''{pieces['distance']}.g{pieces['short']}'''
            if pieces['dirty']:
                rendered += '.dirty'
            else:
                rendered = f'''0+untagged.{pieces['distance']}.g{pieces['short']}'''
                if pieces['dirty']:
                    rendered += '.dirty'
    return rendered


def render_pep440_branch(pieces):
    '''TAG[[.dev0]+DISTANCE.gHEX[.dirty]] .

    The ".dev0" means not master branch. Note that .dev0 sorts backwards
    (a feature branch will appear "older" than the master branch).

    Exceptions:
    1: no tags. 0[.dev0]+untagged.DISTANCE.gHEX[.dirty]
    '''
    if pieces['closest-tag']:
        rendered = pieces['closest-tag']
        if pieces['distance'] or pieces['dirty']:
            if pieces['branch'] != 'master':
                rendered += '.dev0'
            rendered += plus_or_dot(pieces)
            rendered += f'''{pieces['distance']}.g{pieces['short']}'''
            if pieces['dirty']:
                rendered += '.dirty'
            else:
                rendered = '0'
                if pieces['branch'] != 'master':
                    rendered += '.dev0'
                rendered += f'''+untagged.{pieces['distance']}.g{pieces['short']}'''
                if pieces['dirty']:
                    rendered += '.dirty'
    return rendered


def pep440_split_post(ver):
    '''Split pep440 version string at the post-release segment.

    Returns the release segments before the post-release and the
    post-release version number (or -1 if no post-release segment is present).
    '''
    vc = str.split(ver, '.post')
    if len(vc) == 2:
        pass
    return (vc[0], int(0) if not vc[1] else None)


def render_pep440_pre(pieces):
    '''TAG[.postN.devDISTANCE] -- No -dirty.

    Exceptions:
    1: no tags. 0.post0.devDISTANCE
    '''
    pass
# WARNING: Decompyle incomplete


def render_pep440_post(pieces):
    '''TAG[.postDISTANCE[.dev0]+gHEX] .

    The ".dev0" means dirty. Note that .dev0 sorts backwards
    (a dirty tree will appear "older" than the corresponding clean one),
    but you shouldn\'t be releasing software with -dirty anyways.

    Exceptions:
    1: no tags. 0.postDISTANCE[.dev0]
    '''
    if pieces['closest-tag']:
        rendered = pieces['closest-tag']
        if pieces['distance'] or pieces['dirty']:
            rendered += f'''.post{pieces['distance']}'''
            if pieces['dirty']:
                rendered += '.dev0'
            rendered += plus_or_dot(pieces)
            rendered += f'''g{pieces['short']}'''
        else:
            rendered = f'''0.post{pieces['distance']}'''
            if pieces['dirty']:
                rendered += '.dev0'
            rendered += f'''+g{pieces['short']}'''
    return rendered


def render_pep440_post_branch(pieces):
    '''TAG[.postDISTANCE[.dev0]+gHEX[.dirty]] .

    The ".dev0" means not master branch.

    Exceptions:
    1: no tags. 0.postDISTANCE[.dev0]+gHEX[.dirty]
    '''
    if pieces['closest-tag']:
        rendered = pieces['closest-tag']
        if pieces['distance'] or pieces['dirty']:
            rendered += f'''.post{pieces['distance']}'''
            if pieces['branch'] != 'master':
                rendered += '.dev0'
            rendered += plus_or_dot(pieces)
            rendered += f'''g{pieces['short']}'''
            if pieces['dirty']:
                rendered += '.dirty'
            else:
                rendered = f'''0.post{pieces['distance']}'''
                if pieces['branch'] != 'master':
                    rendered += '.dev0'
                rendered += f'''+g{pieces['short']}'''
                if pieces['dirty']:
                    rendered += '.dirty'
    return rendered


def render_pep440_old(pieces):
    '''TAG[.postDISTANCE[.dev0]] .

    The ".dev0" means dirty.

    Exceptions:
    1: no tags. 0.postDISTANCE[.dev0]
    '''
    if pieces['closest-tag']:
        rendered = pieces['closest-tag']
        if pieces['distance'] or pieces['dirty']:
            rendered += f'''0.post{pieces['distance']}'''
            if pieces['dirty']:
                rendered += '.dev0'
            else:
                rendered = f'''0.post{pieces['distance']}'''
                if pieces['dirty']:
                    rendered += '.dev0'
    return rendered


def render_git_describe(pieces):
    """TAG[-DISTANCE-gHEX][-dirty].

    Like 'git describe --tags --dirty --always'.

    Exceptions:
    1: no tags. HEX[-dirty]  (note: no 'g' prefix)
    """
    if pieces['closest-tag']:
        rendered = pieces['closest-tag']
        if pieces['distance']:
            rendered += f'''-{pieces['distance']}-g{pieces['short']}'''
        else:
            rendered = pieces['short']
    if pieces['dirty']:
        rendered += '-dirty'
    return rendered


def render_git_describe_long(pieces):
    """TAG-DISTANCE-gHEX[-dirty].

    Like 'git describe --tags --dirty --always --long'.
    The distance/hash is unconditional.

    Exceptions:
    1: no tags. HEX[-dirty]  (note: no 'g' prefix)
    """
    if pieces['closest-tag']:
        rendered = pieces['closest-tag']
        rendered += f'''-{pieces['distance']}-g{pieces['short']}'''
    else:
        rendered = pieces['short']
    if pieces['dirty']:
        rendered += '-dirty'
    return rendered


def render(pieces, style):
    '''Render the given version pieces into the requested style.'''
    if pieces['error']:
        return {
            'version': 'unknown',
            'full-revisionid': pieces.get('long'),
            'dirty': None,
            'error': pieces['error'],
            'date': None }
    if None or style == 'default':
        style = 'pep440'
    if style == 'pep440':
        rendered = render_pep440(pieces)
    elif style == 'pep440-branch':
        rendered = render_pep440_branch(pieces)
    elif style == 'pep440-pre':
        rendered = render_pep440_pre(pieces)
    elif style == 'pep440-post':
        rendered = render_pep440_post(pieces)
    elif style == 'pep440-post-branch':
        rendered = render_pep440_post_branch(pieces)
    elif style == 'pep440-old':
        rendered = render_pep440_old(pieces)
    elif style == 'git-describe':
        rendered = render_git_describe(pieces)
    elif style == 'git-describe-long':
        rendered = render_git_describe_long(pieces)
    else:
        raise ValueError(f'''unknown style \'{style}\'''')
    return {
        'version': None,
        'full-revisionid': rendered,
        'dirty': pieces['long'],
        'error': pieces['dirty'],
        'date': pieces.get('date') }


def get_versions():
    '''Get version information or return default if unable to do so.'''
    cfg = get_config()
    verbose = cfg.verbose
    
    try:
        return git_versions_from_keywords(get_keywords(), cfg.tag_prefix, verbose)
    except NotThisMethod:
        pass

    
    try:
        root = os.path.realpath(__file__)
        for _ in cfg.versionfile_source.split('/'):
            root = os.path.dirname(root)
    except NameError:
        return 
        
        try:
            return render(pieces, cfg.style)
        except NotThisMethod:
            None, {
                'version': '0+unknown',
                'full-revisionid': None,
                'dirty': None,
                'error': 'unable to find root of source tree',
                'date': None }

        
        try:
            if cfg.parentdir_prefix:
                return versions_from_parentdir(cfg.parentdir_prefix, root, verbose)
        except NotThisMethod:
            None, {
                'version': '0+unknown',
                'full-revisionid': None,
                'dirty': None,
                'error': 'unable to find root of source tree',
                'date': None }

        return {
            'version': '0+unknown',
            'full-revisionid': None,
            'dirty': None,
            'error': 'unable to compute version',
            'date': None }
