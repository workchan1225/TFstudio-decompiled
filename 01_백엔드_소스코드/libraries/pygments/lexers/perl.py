# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: perl.pyc (Python 3.11)

'''
    pygments.lexers.perl
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for Perl, Raku and related languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import RegexLexer, ExtendedRegexLexer, include, bygroups, using, this, default, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Whitespace
from pygments.util import shebang_matches
__all__ = [
    'PerlLexer',
    'Perl6Lexer']

class PerlLexer(RegexLexer):
    '''
    For Perl source code.
    '''
    name = 'Perl'
    url = 'https://www.perl.org'
    aliases = [
        'perl',
        'pl']
    filenames = [
        '*.pl',
        '*.pm',
        '*.t',
        '*.perl']
    mimetypes = [
        'text/x-perl',
        'application/x-perl']
    version_added = ''
    flags = re.DOTALL | re.MULTILINE
    tokens = {
        'balanced-regex': [][('\\A\\#!.+?$', Comment.Hashbang)][('\\#.*?$', Comment.Single)][('^=[a-zA-Z0-9]+\\s+.*?\\n=cut', Comment.Multiline)][(words(('case', 'continue', 'do', 'else', 'elsif', 'for', 'foreach', 'if', 'last', 'my', 'next', 'our', 'redo', 'reset', 'then', 'unless', 'until', 'while', 'print', 'new', 'BEGIN', 'CHECK', 'INIT', 'END', 'return'), suffix = '\\b'), Keyword)][('(format)(\\s+)(\\w+)(\\s*)(=)(\\s*\\n)', bygroups(Keyword, Whitespace, Name, Whitespace, Punctuation, Whitespace), 'format')][('(eq|lt|gt|le|ge|ne|not|and|or|cmp)\\b', Operator.Word)][('s/(\\\\\\\\|\\\\[^\\\\]|[^\\\\/])*/(\\\\\\\\|\\\\[^\\\\]|[^\\\\/])*/[egimosx]*', String.Regex)][('s!(\\\\\\\\|\\\\!|[^!])*!(\\\\\\\\|\\\\!|[^!])*![egimosx]*', String.Regex)][('s\\\\(\\\\\\\\|[^\\\\])*\\\\(\\\\\\\\|[^\\\\])*\\\\[egimosx]*', String.Regex)][('s@(\\\\\\\\|\\\\[^\\\\]|[^\\\\@])*@(\\\\\\\\|\\\\[^\\\\]|[^\\\\@])*@[egimosx]*', String.Regex)][('s%(\\\\\\\\|\\\\[^\\\\]|[^\\\\%])*%(\\\\\\\\|\\\\[^\\\\]|[^\\\\%])*%[egimosx]*', String.Regex)][('s\\{(\\\\\\\\|\\\\[^\\\\]|[^\\\\}])*\\}\\s*', String.Regex, 'balanced-regex')][('s<(\\\\\\\\|\\\\[^\\\\]|[^\\\\>])*>\\s*', String.Regex, 'balanced-regex')][('s\\[(\\\\\\\\|\\\\[^\\\\]|[^\\\\\\]])*\\]\\s*', String.Regex, 'balanced-regex')][('s\\((\\\\\\\\|\\\\[^\\\\]|[^\\\\)])*\\)\\s*', String.Regex, 'balanced-regex')][('m?/(\\\\\\\\|\\\\[^\\\\]|[^\\\\/\\n])*/[gcimosx]*', String.Regex)][('m(?=[/!\\\\{<\\[(@%$])', String.Regex, 'balanced-regex')][('((?<==~)|(?<=\\())\\s*/(\\\\\\\\|\\\\[^\\\\]|[^\\\\/])*/[gcimosx]*', String.Regex)][('\\s+', Whitespace)][(words(('abs', 'accept', 'alarm', 'atan2', 'bind', 'binmode', 'bless', 'caller', 'chdir', 'chmod', 'chomp', 'chop', 'chown', 'chr', 'chroot', 'close', 'closedir', 'connect', 'continue', 'cos', 'crypt', 'dbmclose', 'dbmopen', 'defined', 'delete', 'die', 'dump', 'each', 'endgrent', 'endhostent', 'endnetent', 'endprotoent', 'endpwent', 'endservent', 'eof', 'eval', 'exec', 'exists', 'exit', 'exp', 'fcntl', 'fileno', 'flock', 'fork', 'format', 'formline', 'getc', 'getgrent', 'getgrgid', 'getgrnam', 'gethostbyaddr', 'gethostbyname', 'gethostent', 'getlogin', 'getnetbyaddr', 'getnetbyname', 'getnetent', 'getpeername', 'getpgrp', 'getppid', 'getpriority', 'getprotobyname', 'getprotobynumber', 'getprotoent', 'getpwent', 'getpwnam', 'getpwuid', 'getservbyname', 'getservbyport', 'getservent', 'getsockname', 'getsockopt', 'glob', 'gmtime', 'goto', 'grep', 'hex', 'import', 'index', 'int', 'ioctl', 'join', 'keys', 'kill', 'last', 'lc', 'lcfirst', 'length', 'link', 'listen', 'local', 'localtime', 'log', 'lstat', 'map', 'mkdir', 'msgctl', 'msgget', 'msgrcv', 'msgsnd', 'my', 'next', 'oct', 'open', 'opendir', 'ord', 'our', 'pack', 'pipe', 'pop', 'pos', 'printf', 'prototype', 'push', 'quotemeta', 'rand', 'read', 'readdir', 'readline', 'readlink', 'readpipe', 'recv', 'redo', 'ref', 'rename', 'reverse', 'rewinddir', 'rindex', 'rmdir', 'scalar', 'seek', 'seekdir', 'select', 'semctl', 'semget', 'semop', 'send', 'setgrent', 'sethostent', 'setnetent', 'setpgrp', 'setpriority', 'setprotoent', 'setpwent', 'setservent', 'setsockopt', 'shift', 'shmctl', 'shmget', 'shmread', 'shmwrite', 'shutdown', 'sin', 'sleep', 'socket', 'socketpair', 'sort', 'splice', 'split', 'sprintf', 'sqrt', 'srand', 'stat', 'study', 'substr', 'symlink', 'syscall', 'sysopen', 'sysread', 'sysseek', 'system', 'syswrite', 'tell', 'telldir', 'tie', 'tied', 'time', 'times', 'tr', 'truncate', 'uc', 'ucfirst', 'umask', 'undef', 'unlink', 'unpack', 'unshift', 'untie', 'utime', 'values', 'vec', 'wait', 'waitpid', 'wantarray', 'warn', 'write'), suffix = '\\b'), Name.Builtin)][('((__(DATA|DIE|WARN)__)|(STD(IN|OUT|ERR)))\\b', Name.Builtin.Pseudo)][('(<<)([\\\'"]?)([a-zA-Z_]\\w*)(\\2;?\\n.*?\\n)(\\3)(\\n)', bygroups(String, String, String.Delimiter, String, String.Delimiter, Whitespace))][('__END__', Comment.Preproc, 'end-part')][('\\$\\^[ADEFHILMOPSTWX]', Name.Variable.Global)][('\\$[\\\\\\"\\[\\]\'&`+*.,;=%~?@$!<>(^|/-](?!\\w)', Name.Variable.Global)][('[$@%#]+', Name.Variable, 'varname')][('0_?[0-7]+(_[0-7]+)*', Number.Oct)][('0x[0-9A-Fa-f]+(_[0-9A-Fa-f]+)*', Number.Hex)][('0b[01]+(_[01]+)*', Number.Bin)][('(?i)(\\d*(_\\d*)*\\.\\d+(_\\d*)*|\\d+(_\\d*)*\\.\\d+(_\\d*)*)(e[+-]?\\d+)?', Number.Float)][('(?i)\\d+(_\\d*)*e[+-]?\\d+(_\\d*)*', Number.Float)][('\\d+(_\\d+)*', Number.Integer)][("'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String)][('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String)][('`(\\\\\\\\|\\\\[^\\\\]|[^`\\\\])*`', String.Backtick)][('<([^\\s>]+)>', String.Regex)][('(q|qq|qw|qr|qx)\\{', String.Other, 'cb-string')][('(q|qq|qw|qr|qx)\\(', String.Other, 'rb-string')][('(q|qq|qw|qr|qx)\\[', String.Other, 'sb-string')][('(q|qq|qw|qr|qx)\\<', String.Other, 'lt-string')][('(q|qq|qw|qr|qx)([\\W_])(.|\\n)*?\\2', String.Other)][('(package)(\\s+)([a-zA-Z_]\\w*(?:::[a-zA-Z_]\\w*)*)', bygroups(Keyword, Whitespace, Name.Namespace))][('(use|require|no)(\\s+)([a-zA-Z_]\\w*(?:::[a-zA-Z_]\\w*)*)', bygroups(Keyword, Whitespace, Name.Namespace))][('(sub)(\\s+)', bygroups(Keyword, Whitespace), 'funcname')][(words(('no', 'package', 'require', 'use'), suffix = '\\b'), Keyword)][('(\\[\\]|\\*\\*|::|<<|>>|>=|<=>|<=|={3}|!=|=~|!~|&&?|\\|\\||\\.{1,3})', Operator)][('[-+/*%=<>&^|!\\\\~]=?', Operator)][('[()\\[\\]:;,<>/?{}]', Punctuation)],
        'root': [][('\\A\\#!.+?$', Comment.Hashbang)][('\\#.*?$', Comment.Single)][('^=[a-zA-Z0-9]+\\s+.*?\\n=cut', Comment.Multiline)][(words(('case', 'continue', 'do', 'else', 'elsif', 'for', 'foreach', 'if', 'last', 'my', 'next', 'our', 'redo', 'reset', 'then', 'unless', 'until', 'while', 'print', 'new', 'BEGIN', 'CHECK', 'INIT', 'END', 'return'), suffix = '\\b'), Keyword)][('(format)(\\s+)(\\w+)(\\s*)(=)(\\s*\\n)', bygroups(Keyword, Whitespace, Name, Whitespace, Punctuation, Whitespace), 'format')][('(eq|lt|gt|le|ge|ne|not|and|or|cmp)\\b', Operator.Word)][('s/(\\\\\\\\|\\\\[^\\\\]|[^\\\\/])*/(\\\\\\\\|\\\\[^\\\\]|[^\\\\/])*/[egimosx]*', String.Regex)][('s!(\\\\\\\\|\\\\!|[^!])*!(\\\\\\\\|\\\\!|[^!])*![egimosx]*', String.Regex)][('s\\\\(\\\\\\\\|[^\\\\])*\\\\(\\\\\\\\|[^\\\\])*\\\\[egimosx]*', String.Regex)][('s@(\\\\\\\\|\\\\[^\\\\]|[^\\\\@])*@(\\\\\\\\|\\\\[^\\\\]|[^\\\\@])*@[egimosx]*', String.Regex)][('s%(\\\\\\\\|\\\\[^\\\\]|[^\\\\%])*%(\\\\\\\\|\\\\[^\\\\]|[^\\\\%])*%[egimosx]*', String.Regex)][('s\\{(\\\\\\\\|\\\\[^\\\\]|[^\\\\}])*\\}\\s*', String.Regex, 'balanced-regex')][('s<(\\\\\\\\|\\\\[^\\\\]|[^\\\\>])*>\\s*', String.Regex, 'balanced-regex')][('s\\[(\\\\\\\\|\\\\[^\\\\]|[^\\\\\\]])*\\]\\s*', String.Regex, 'balanced-regex')][('s\\((\\\\\\\\|\\\\[^\\\\]|[^\\\\)])*\\)\\s*', String.Regex, 'balanced-regex')][('m?/(\\\\\\\\|\\\\[^\\\\]|[^\\\\/\\n])*/[gcimosx]*', String.Regex)][('m(?=[/!\\\\{<\\[(@%$])', String.Regex, 'balanced-regex')][('((?<==~)|(?<=\\())\\s*/(\\\\\\\\|\\\\[^\\\\]|[^\\\\/])*/[gcimosx]*', String.Regex)][('\\s+', Whitespace)][(words(('abs', 'accept', 'alarm', 'atan2', 'bind', 'binmode', 'bless', 'caller', 'chdir', 'chmod', 'chomp', 'chop', 'chown', 'chr', 'chroot', 'close', 'closedir', 'connect', 'continue', 'cos', 'crypt', 'dbmclose', 'dbmopen', 'defined', 'delete', 'die', 'dump', 'each', 'endgrent', 'endhostent', 'endnetent', 'endprotoent', 'endpwent', 'endservent', 'eof', 'eval', 'exec', 'exists', 'exit', 'exp', 'fcntl', 'fileno', 'flock', 'fork', 'format', 'formline', 'getc', 'getgrent', 'getgrgid', 'getgrnam', 'gethostbyaddr', 'gethostbyname', 'gethostent', 'getlogin', 'getnetbyaddr', 'getnetbyname', 'getnetent', 'getpeername', 'getpgrp', 'getppid', 'getpriority', 'getprotobyname', 'getprotobynumber', 'getprotoent', 'getpwent', 'getpwnam', 'getpwuid', 'getservbyname', 'getservbyport', 'getservent', 'getsockname', 'getsockopt', 'glob', 'gmtime', 'goto', 'grep', 'hex', 'import', 'index', 'int', 'ioctl', 'join', 'keys', 'kill', 'last', 'lc', 'lcfirst', 'length', 'link', 'listen', 'local', 'localtime', 'log', 'lstat', 'map', 'mkdir', 'msgctl', 'msgget', 'msgrcv', 'msgsnd', 'my', 'next', 'oct', 'open', 'opendir', 'ord', 'our', 'pack', 'pipe', 'pop', 'pos', 'printf', 'prototype', 'push', 'quotemeta', 'rand', 'read', 'readdir', 'readline', 'readlink', 'readpipe', 'recv', 'redo', 'ref', 'rename', 'reverse', 'rewinddir', 'rindex', 'rmdir', 'scalar', 'seek', 'seekdir', 'select', 'semctl', 'semget', 'semop', 'send', 'setgrent', 'sethostent', 'setnetent', 'setpgrp', 'setpriority', 'setprotoent', 'setpwent', 'setservent', 'setsockopt', 'shift', 'shmctl', 'shmget', 'shmread', 'shmwrite', 'shutdown', 'sin', 'sleep', 'socket', 'socketpair', 'sort', 'splice', 'split', 'sprintf', 'sqrt', 'srand', 'stat', 'study', 'substr', 'symlink', 'syscall', 'sysopen', 'sysread', 'sysseek', 'system', 'syswrite', 'tell', 'telldir', 'tie', 'tied', 'time', 'times', 'tr', 'truncate', 'uc', 'ucfirst', 'umask', 'undef', 'unlink', 'unpack', 'unshift', 'untie', 'utime', 'values', 'vec', 'wait', 'waitpid', 'wantarray', 'warn', 'write'), suffix = '\\b'), Name.Builtin)][('((__(DATA|DIE|WARN)__)|(STD(IN|OUT|ERR)))\\b', Name.Builtin.Pseudo)][('(<<)([\\\'"]?)([a-zA-Z_]\\w*)(\\2;?\\n.*?\\n)(\\3)(\\n)', bygroups(String, String, String.Delimiter, String, String.Delimiter, Whitespace))][('__END__', Comment.Preproc, 'end-part')][('\\$\\^[ADEFHILMOPSTWX]', Name.Variable.Global)][('\\$[\\\\\\"\\[\\]\'&`+*.,;=%~?@$!<>(^|/-](?!\\w)', Name.Variable.Global)][('[$@%#]+', Name.Variable, 'varname')][('0_?[0-7]+(_[0-7]+)*', Number.Oct)][('0x[0-9A-Fa-f]+(_[0-9A-Fa-f]+)*', Number.Hex)][('0b[01]+(_[01]+)*', Number.Bin)][('(?i)(\\d*(_\\d*)*\\.\\d+(_\\d*)*|\\d+(_\\d*)*\\.\\d+(_\\d*)*)(e[+-]?\\d+)?', Number.Float)][('(?i)\\d+(_\\d*)*e[+-]?\\d+(_\\d*)*', Number.Float)][('\\d+(_\\d+)*', Number.Integer)][("'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String)][('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String)][('`(\\\\\\\\|\\\\[^\\\\]|[^`\\\\])*`', String.Backtick)][('<([^\\s>]+)>', String.Regex)][('(q|qq|qw|qr|qx)\\{', String.Other, 'cb-string')][('(q|qq|qw|qr|qx)\\(', String.Other, 'rb-string')][('(q|qq|qw|qr|qx)\\[', String.Other, 'sb-string')][('(q|qq|qw|qr|qx)\\<', String.Other, 'lt-string')][('(q|qq|qw|qr|qx)([\\W_])(.|\\n)*?\\2', String.Other)][('(package)(\\s+)([a-zA-Z_]\\w*(?:::[a-zA-Z_]\\w*)*)', bygroups(Keyword, Whitespace, Name.Namespace))][('(use|require|no)(\\s+)([a-zA-Z_]\\w*(?:::[a-zA-Z_]\\w*)*)', bygroups(Keyword, Whitespace, Name.Namespace))][('(sub)(\\s+)', bygroups(Keyword, Whitespace), 'funcname')][(words(('no', 'package', 'require', 'use'), suffix = '\\b'), Keyword)][('(\\[\\]|\\*\\*|::|<<|>>|>=|<=>|<=|={3}|!=|=~|!~|&&?|\\|\\||\\.{1,3})', Operator)][('[-+/*%=<>&^|!\\\\~]=?', Operator)][('[()\\[\\]:;,<>/?{}]', Punctuation)][('(?=\\w)', Name, 'name')],
        'format': [
            ('\\.\\n', String.Interpol, '#pop'),
            ('[^\\n]*\\n', String.Interpol)],
        'varname': [
            ('\\s+', Whitespace),
            ('\\{', Punctuation, '#pop'),
            ('\\)|,', Punctuation, '#pop'),
            ('\\w+::', Name.Namespace),
            ('[\\w:]+', Name.Variable, '#pop')],
        'name': [
            ('[a-zA-Z_]\\w*(::[a-zA-Z_]\\w*)*(::)?(?=\\s*->)', Name.Namespace, '#pop'),
            ('[a-zA-Z_]\\w*(::[a-zA-Z_]\\w*)*::', Name.Namespace, '#pop'),
            ('[\\w:]+', Name, '#pop'),
            ('[A-Z_]+(?=\\W)', Name.Constant, '#pop'),
            ('(?=\\W)', Text, '#pop')],
        'funcname': [
            ('[a-zA-Z_]\\w*[!?]?', Name.Function),
            ('\\s+', Whitespace),
            ('(\\([$@%]*\\))(\\s*)', bygroups(Punctuation, Whitespace)),
            (';', Punctuation, '#pop'),
            ('.*?\\{', Punctuation, '#pop')],
        'cb-string': [
            ('\\\\[{}\\\\]', String.Other),
            ('\\\\', String.Other),
            ('\\{', String.Other, 'cb-string'),
            ('\\}', String.Other, '#pop'),
            ('[^{}\\\\]+', String.Other)],
        'rb-string': [
            ('\\\\[()\\\\]', String.Other),
            ('\\\\', String.Other),
            ('\\(', String.Other, 'rb-string'),
            ('\\)', String.Other, '#pop'),
            ('[^()]+', String.Other)],
        'sb-string': [
            ('\\\\[\\[\\]\\\\]', String.Other),
            ('\\\\', String.Other),
            ('\\[', String.Other, 'sb-string'),
            ('\\]', String.Other, '#pop'),
            ('[^\\[\\]]+', String.Other)],
        'lt-string': [
            ('\\\\[<>\\\\]', String.Other),
            ('\\\\', String.Other),
            ('\\<', String.Other, 'lt-string'),
            ('\\>', String.Other, '#pop'),
            ('[^<>]+', String.Other)],
        'end-part': [
            ('.+', Comment.Preproc, '#pop')] }
    
    def analyse_text(text):
        if shebang_matches(text, 'perl'):
            return True
        result = None
        if re.search('(?:my|our)\\s+[$@%(]', text):
            result += 0.9
        if ':=' in text:
            result /= 2
        return result



class Perl6Lexer(ExtendedRegexLexer):
    pass
# WARNING: Decompyle incomplete
