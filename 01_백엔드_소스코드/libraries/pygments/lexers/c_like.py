# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: c_like.pyc (Python 3.11)

'''
    pygments.lexers.c_like
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexers for other C-like languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import RegexLexer, include, bygroups, inherit, words, default
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Whitespace
from pygments.lexers.c_cpp import CLexer, CppLexer
from pygments.lexers import _mql_builtins
__all__ = [
    'PikeLexer',
    'NesCLexer',
    'ClayLexer',
    'ECLexer',
    'ValaLexer',
    'CudaLexer',
    'SwigLexer',
    'MqlLexer',
    'ArduinoLexer',
    'CharmciLexer',
    'OmgIdlLexer',
    'PromelaLexer']

class PikeLexer(CppLexer):
    '''
    For `Pike <http://pike.lysator.liu.se/>`_ source code.
    '''
    name = 'Pike'
    aliases = [
        'pike']
    filenames = [
        '*.pike',
        '*.pmod']
    mimetypes = [
        'text/x-pike']
    version_added = '2.0'
    tokens = {
        'statements': [
            (words(('catch', 'new', 'private', 'protected', 'public', 'gauge', 'throw', 'throws', 'class', 'interface', 'implement', 'abstract', 'extends', 'from', 'this', 'super', 'constant', 'final', 'static', 'import', 'use', 'extern', 'inline', 'proto', 'break', 'continue', 'if', 'else', 'for', 'while', 'do', 'switch', 'case', 'as', 'in', 'version', 'return', 'true', 'false', 'null', '__VERSION__', '__MAJOR__', '__MINOR__', '__BUILD__', '__REAL_VERSION__', '__REAL_MAJOR__', '__REAL_MINOR__', '__REAL_BUILD__', '__DATE__', '__TIME__', '__FILE__', '__DIR__', '__LINE__', '__AUTO_BIGNUM__', '__NT__', '__PIKE__', '__amigaos__', '_Pragma', 'static_assert', 'defined', 'sscanf'), suffix = '\\b'), Keyword),
            ('(bool|int|long|float|short|double|char|string|object|void|mapping|array|multiset|program|function|lambda|mixed|[a-z_][a-z0-9_]*_t)\\b', Keyword.Type),
            ('(class)(\\s+)', bygroups(Keyword, Whitespace), 'classname'),
            ('[~!%^&*+=|?:<>/@-]', Operator),
            inherit],
        'classname': [
            ('[a-zA-Z_]\\w*', Name.Class, '#pop'),
            ('\\s*(?=>)', Whitespace, '#pop')] }


class NesCLexer(CLexer):
    '''
    For `nesC <https://github.com/tinyos/nesc>`_ source code with preprocessor
    directives.
    '''
    name = 'nesC'
    aliases = [
        'nesc']
    filenames = [
        '*.nc']
    mimetypes = [
        'text/x-nescsrc']
    version_added = '2.0'
    tokens = {
        'statements': [
            (words(('abstract', 'as', 'async', 'atomic', 'call', 'command', 'component', 'components', 'configuration', 'event', 'extends', 'generic', 'implementation', 'includes', 'interface', 'module', 'new', 'norace', 'post', 'provides', 'signal', 'task', 'uses'), suffix = '\\b'), Keyword),
            (words(('nx_struct', 'nx_union', 'nx_int8_t', 'nx_int16_t', 'nx_int32_t', 'nx_int64_t', 'nx_uint8_t', 'nx_uint16_t', 'nx_uint32_t', 'nx_uint64_t'), suffix = '\\b'), Keyword.Type),
            inherit] }


class ClayLexer(RegexLexer):
    '''
    For Clay source.
    '''
    name = 'Clay'
    filenames = [
        '*.clay']
    aliases = [
        'clay']
    mimetypes = [
        'text/x-clay']
    url = 'http://claylabs.com/clay'
    version_added = '2.0'
    tokens = {
        'root': [
            ('\\s+', Whitespace),
            ('//.*?$', Comment.Single),
            ('/(\\\\\\n)?[*](.|\\n)*?[*](\\\\\\n)?/', Comment.Multiline),
            ('\\b(public|private|import|as|record|variant|instance|define|overload|default|external|alias|rvalue|ref|forward|inline|noinline|forceinline|enum|var|and|or|not|if|else|goto|return|while|switch|case|break|continue|for|in|true|false|try|catch|throw|finally|onerror|staticassert|eval|when|newtype|__FILE__|__LINE__|__COLUMN__|__ARG__)\\b', Keyword),
            ('[~!%^&*+=|:<>/-]', Operator),
            ('[#(){}\\[\\],;.]', Punctuation),
            ('0x[0-9a-fA-F]+[LlUu]*', Number.Hex),
            ('\\d+[LlUu]*', Number.Integer),
            ('\\b(true|false)\\b', Name.Builtin),
            ('(?i)[a-z_?][\\w?]*', Name),
            ('"""', String, 'tdqs'),
            ('"', String, 'dqs')],
        'strings': [
            ('(?i)\\\\(x[0-9a-f]{2}|.)', String.Escape),
            ('[^\\\\"]+', String)],
        'nl': [
            ('\\n', String)],
        'dqs': [
            ('"', String, '#pop'),
            include('strings')],
        'tdqs': [
            ('"""', String, '#pop'),
            include('strings'),
            include('nl')] }


class ECLexer(CLexer):
    '''
    For eC source code with preprocessor directives.
    '''
    name = 'eC'
    aliases = [
        'ec']
    filenames = [
        '*.ec',
        '*.eh']
    mimetypes = [
        'text/x-echdr',
        'text/x-ecsrc']
    url = 'https://ec-lang.org'
    version_added = '1.5'
    tokens = {
        'statements': [
            (words(('virtual', 'class', 'private', 'public', 'property', 'import', 'delete', 'new', 'new0', 'renew', 'renew0', 'define', 'get', 'set', 'remote', 'dllexport', 'dllimport', 'stdcall', 'subclass', '__on_register_module', 'namespace', 'using', 'typed_object', 'any_object', 'incref', 'register', 'watch', 'stopwatching', 'firewatchers', 'watchable', 'class_designer', 'class_fixed', 'class_no_expansion', 'isset', 'class_default_property', 'property_category', 'class_data', 'class_property', 'thisclass', 'dbtable', 'dbindex', 'database_open', 'dbfield'), suffix = '\\b'), Keyword),
            (words(('uint', 'uint16', 'uint32', 'uint64', 'bool', 'byte', 'unichar', 'int64'), suffix = '\\b'), Keyword.Type),
            ('(class)(\\s+)', bygroups(Keyword, Whitespace), 'classname'),
            ('(null|value|this)\\b', Name.Builtin),
            inherit] }


class ValaLexer(RegexLexer):
    '''
    For Vala source code with preprocessor directives.
    '''
    name = 'Vala'
    aliases = [
        'vala',
        'vapi']
    filenames = [
        '*.vala',
        '*.vapi']
    mimetypes = [
        'text/x-vala']
    url = 'https://vala.dev'
    version_added = '1.1'
    tokens = {
        'whitespace': [
            ('^\\s*#if\\s+0', Comment.Preproc, 'if0'),
            ('\\n', Whitespace),
            ('\\s+', Whitespace),
            ('\\\\\\n', Text),
            ('//(\\n|(.|\\n)*?[^\\\\]\\n)', Comment.Single),
            ('/(\\\\\\n)?[*](.|\\n)*?[*](\\\\\\n)?/', Comment.Multiline)],
        'statements': [
            ('[L@]?"', String, 'string'),
            ("L?'(\\\\.|\\\\[0-7]{1,3}|\\\\x[a-fA-F0-9]{1,2}|[^\\\\\\'\\n])'", String.Char),
            ('(?s)""".*?"""', String),
            ('(\\d+\\.\\d*|\\.\\d+|\\d+)[eE][+-]?\\d+[lL]?', Number.Float),
            ('(\\d+\\.\\d*|\\.\\d+|\\d+[fF])[fF]?', Number.Float),
            ('0x[0-9a-fA-F]+[Ll]?', Number.Hex),
            ('0[0-7]+[Ll]?', Number.Oct),
            ('\\d+[Ll]?', Number.Integer),
            ('[~!%^&*+=|?:<>/-]', Operator),
            ('(\\[)(Compact|Immutable|(?:Boolean|Simple)Type)(\\])', bygroups(Punctuation, Name.Decorator, Punctuation)),
            ('(\\[)(CCode|(?:Integer|Floating)Type)', bygroups(Punctuation, Name.Decorator)),
            ('[()\\[\\],.]', Punctuation),
            (words(('as', 'base', 'break', 'case', 'catch', 'construct', 'continue', 'default', 'delete', 'do', 'else', 'enum', 'finally', 'for', 'foreach', 'get', 'if', 'in', 'is', 'lock', 'new', 'out', 'params', 'return', 'set', 'sizeof', 'switch', 'this', 'throw', 'try', 'typeof', 'while', 'yield'), suffix = '\\b'), Keyword),
            (words(('abstract', 'const', 'delegate', 'dynamic', 'ensures', 'extern', 'inline', 'internal', 'override', 'owned', 'private', 'protected', 'public', 'ref', 'requires', 'signal', 'static', 'throws', 'unowned', 'var', 'virtual', 'volatile', 'weak', 'yields'), suffix = '\\b'), Keyword.Declaration),
            ('(namespace|using)(\\s+)', bygroups(Keyword.Namespace, Whitespace), 'namespace'),
            ('(class|errordomain|interface|struct)(\\s+)', bygroups(Keyword.Declaration, Whitespace), 'class'),
            ('(\\.)([a-zA-Z_]\\w*)', bygroups(Operator, Name.Attribute)),
            (words(('void', 'bool', 'char', 'double', 'float', 'int', 'int8', 'int16', 'int32', 'int64', 'long', 'short', 'size_t', 'ssize_t', 'string', 'time_t', 'uchar', 'uint', 'uint8', 'uint16', 'uint32', 'uint64', 'ulong', 'unichar', 'ushort'), suffix = '\\b'), Keyword.Type),
            ('(true|false|null)\\b', Name.Builtin),
            ('[a-zA-Z_]\\w*', Name)],
        'root': [
            include('whitespace'),
            default('statement')],
        'statement': [
            include('whitespace'),
            include('statements'),
            ('[{}]', Punctuation),
            (';', Punctuation, '#pop')],
        'string': [
            ('"', String, '#pop'),
            ('\\\\([\\\\abfnrtv"\\\']|x[a-fA-F0-9]{2,4}|[0-7]{1,3})', String.Escape),
            ('[^\\\\"\\n]+', String),
            ('\\\\\\n', String),
            ('\\\\', String)],
        'if0': [
            ('^\\s*#if.*?(?<!\\\\)\\n', Comment.Preproc, '#push'),
            ('^\\s*#el(?:se|if).*\\n', Comment.Preproc, '#pop'),
            ('^\\s*#endif.*?(?<!\\\\)\\n', Comment.Preproc, '#pop'),
            ('.*?\\n', Comment)],
        'class': [
            ('[a-zA-Z_]\\w*', Name.Class, '#pop')],
        'namespace': [
            ('[a-zA-Z_][\\w.]*', Name.Namespace, '#pop')] }


class CudaLexer(CLexer):
    '''
    For NVIDIA CUDA™ source.
    '''
    name = 'CUDA'
    filenames = [
        '*.cu',
        '*.cuh']
    aliases = [
        'cuda',
        'cu']
    mimetypes = [
        'text/x-cuda']
    url = 'https://developer.nvidia.com/category/zone/cuda-zone'
    version_added = '1.6'
    function_qualifiers = {
        '__host__',
        '__device__',
        '__global__',
        '__noinline__',
        '__forceinline__'}
    variable_qualifiers = {
        '__device__',
        '__shared__',
        '__constant__',
        '__restrict__'}
    vector_types = {
        'dim3',
        'int1',
        'int2',
        'int3',
        'int4',
        'char1',
        'char2',
        'char3',
        'char4',
        'long1',
        'long2',
        'long3',
        'long4',
        'uint1',
        'uint2',
        'uint3',
        'uint4',
        'float1',
        'float2',
        'float3',
        'float4',
        'short1',
        'short2',
        'short3',
        'short4',
        'uchar1',
        'uchar2',
        'uchar3',
        'uchar4',
        'ulong1',
        'ulong2',
        'ulong3',
        'ulong4',
        'double1',
        'double2',
        'ushort1',
        'ushort2',
        'ushort3',
        'ushort4',
        'longlong1',
        'longlong2',
        'ulonglong1',
        'ulonglong2'}
    variables = {
        'gridDim',
        'blockDim',
        'blockIdx',
        'warpSize',
        'threadIdx'}
    functions = {
        '__syncthreads',
        '__threadfence',
        '__syncthreads_or',
        '__syncthreads_and',
        '__syncthreads_count',
        '__threadfence_block',
        '__threadfence_system'}
    execution_confs = {
        '<<<',
        '>>>'}
    
    def get_tokens_unprocessed(self, text, stack = (('root',),)):
        pass
    # WARNING: Decompyle incomplete



class SwigLexer(CppLexer):
    '''
    For `SWIG <http://www.swig.org/>`_ source code.
    '''
    name = 'SWIG'
    aliases = [
        'swig']
    filenames = [
        '*.swg',
        '*.i']
    mimetypes = [
        'text/swig']
    version_added = '2.0'
    priority = 0.04
    tokens = {
        'root': [
            ('\\$\\**\\&?\\w+', Name),
            inherit],
        'statements': [
            ('(%[a-z_][a-z0-9_]*)', Name.Function),
            ('\\$\\**\\&?\\w+', Name),
            ('##*[a-zA-Z_]\\w*', Comment.Preproc),
            inherit] }
    swig_directives = {
        '%arg',
        '%bang',
        '%init',
        '%warn',
        '%apply',
        '%begin',
        '%clear',
        '%types',
        '%csenum',
        '%define',
        '%delete',
        '%enddef',
        '%extend',
        '%header',
        '%ignore',
        '%import',
        '%inline',
        '%insert',
        '%kwargs',
        '%module',
        '%nspace',
        '%pragma',
        '%rename',
        '%shadow',
        '%sizeof',
        '%catches',
        '%csconst',
        '%default',
        '%defined',
        '%feature',
        '%include',
        '%luacode',
        '%mutable',
        '%typemap',
        '%varargs',
        '%callback',
        '%constant',
        '%copyctor',
        '%director',
        '%fragment',
        '%implicit',
        '%javaenum',
        '%perlcode',
        '%template',
        '%attribute',
        '%delobject',
        '%exception',
        '%fragments',
        '%immutable',
        '%javaconst',
        '%newobject',
        '%pythonabc',
        '%refobject',
        '%typecheck',
        '%descriptor',
        '%ignorewarn',
        '%naturalvar',
        '%pythoncode',
        '%shared_ptr',
        '%warnfilter',
        '%defaultctor',
        '%defaultdtor',
        '%ifcplusplus',
        '%unrefobject',
        '%csconstvalue',
        '%exceptionvar',
        '%implicitconv',
        '%pythonappend',
        '%trackobjects',
        '%javaexception',
        '%pythondynamic',
        '%pythonprepend',
        '%exceptionclass',
        '%javaconstvalue',
        '%pythoncallback',
        '%pythonmaybecall',
        '%nestedworkaround',
        '%pythonnondynamic',
        '%csmethodmodifiers',
        '%csnothrowexception',
        '%javamethodmodifiers',
        '%extend_smart_pointer'}
    
    def analyse_text(text):
        rv = 0
        matches = re.findall('^\\s*(%[a-z_][a-z0-9_]*)', text, re.M)
        for m in matches:
            if m in SwigLexer.swig_directives:
                rv = 0.98
            else:
                rv = 0.91
            return rv



class MqlLexer(CppLexer):
    '''
    For `MQL4 <http://docs.mql4.com/>`_ and
    `MQL5 <http://www.mql5.com/en/docs>`_ source code.
    '''
    name = 'MQL'
    aliases = [
        'mql',
        'mq4',
        'mq5',
        'mql4',
        'mql5']
    filenames = [
        '*.mq4',
        '*.mq5',
        '*.mqh']
    mimetypes = [
        'text/x-mql']
    version_added = '2.0'
    tokens = {
        'statements': [
            (words(_mql_builtins.keywords, suffix = '\\b'), Keyword),
            (words(_mql_builtins.c_types, suffix = '\\b'), Keyword.Type),
            (words(_mql_builtins.types, suffix = '\\b'), Name.Function),
            (words(_mql_builtins.constants, suffix = '\\b'), Name.Constant),
            (words(_mql_builtins.colors, prefix = '(clr)?', suffix = '\\b'), Name.Constant),
            inherit] }


class ArduinoLexer(CppLexer):
    '''
    For `Arduino(tm) <https://arduino.cc/>`_ source.

    This is an extension of the CppLexer, as the Arduino® Language is a superset
    of C++
    '''
    name = 'Arduino'
    aliases = [
        'arduino']
    filenames = [
        '*.ino']
    mimetypes = [
        'text/x-arduino']
    version_added = '2.1'
    structure = {
        'setup',
        'loop'}
    operators = {
        'or',
        'and',
        'not',
        'xor'}
    variables = {
        'unsigned int',
        'unsigned char',
        'unsigned long',
        'LOW',
        'int',
        'HIGH',
        'auto',
        'bool',
        'byte',
        'char',
        'enum',
        'long',
        'true',
        'void',
        'word',
        'INPUT',
        '_Bool',
        'array',
        'class',
        'const',
        'false',
        'float',
        'short',
        'union',
        'OUTPUT',
        'String',
        'delete',
        'double',
        'extern',
        'friend',
        'inline',
        'int8_t',
        'public',
        'signed',
        'sizeof',
        'static',
        'string',
        'struct',
        'PROGMEM',
        'boolean',
        'complex',
        'int16_t',
        'int32_t',
        'int64_t',
        'private',
        'typedef',
        'uint8_t',
        'virtual',
        'EXTERNAL',
        'INTERNAL',
        '_Complex',
        'explicit',
        'operator',
        'register',
        'uint16_t',
        'uint32_t',
        'uint64_t',
        'unsigned',
        'volatile',
        'protected',
        '_Imaginary',
        'atomic_int',
        'const_cast',
        'INTERNAL1V1',
        'LED_BUILTIN',
        'SYSEX_START',
        'atomic_bool',
        'atomic_char',
        'atomic_long',
        'atomic_uint',
        'static_cast',
        'INPUT_PULLUP',
        'INTERNAL2V56',
        'SET_PIN_MODE',
        'SYSTEM_RESET',
        'atomic_llong',
        'atomic_schar',
        'atomic_short',
        'atomic_uchar',
        'atomic_ulong',
        'dynamic_cast',
        'REPORT_ANALOG',
        'atomic_ullong',
        'atomic_ushort',
        'ANALOG_MESSAGE',
        'FIRMATA_STRING',
        'REPORT_DIGITAL',
        'DIGITAL_MESSAGE',
        'reinterpret_cast'}
    functions = {
        'SD',
        'GSM',
        'SPI',
        'TFT',
        'abs',
        'bit',
        'cos',
        'end',
        'get',
        'map',
        'max',
        'min',
        'pow',
        'put',
        'run',
        'sin',
        'tan',
        'File',
        'GPRS',
        'RSSI',
        'SSID',
        'Task',
        'WiFi',
        'Wire',
        'beep',
        'fill',
        'find',
        'home',
        'line',
        'move',
        'open',
        'peek',
        'read',
        'rect',
        'seek',
        'size',
        'sqrt',
        'step',
        'stop',
        'text',
        'tone',
        'turn',
        'Audio',
        'BSSID',
        'Mouse',
        'Servo',
        'begin',
        'blink',
        'clear',
        'click',
        'close',
        'delay',
        'flush',
        'image',
        'isPIN',
        'mkdir',
        'point',
        'press',
        'print',
        'ready',
        'rmdir',
        'width',
        'write',
        'yield',
        'Bridge',
        'Client',
        'EEPROM',
        'FileIO',
        'GSMPIN',
        'IRread',
        'PImage',
        'Serial',
        'Server',
        'Stream',
        'attach',
        'bitSet',
        'buffer',
        'circle',
        'config',
        'cursor',
        'detach',
        'endSMS',
        'exists',
        'getKey',
        'height',
        'listen',
        'micros',
        'millis',
        'noFill',
        'noTone',
        'random',
        'remove',
        'setDNS',
        'stroke',
        'Console',
        'Esplora',
        'Firmata',
        'GSMBand',
        'GSM_SMS',
        'Mailbox',
        'Process',
        'Stepper',
        'USBHost',
        'WiFiUDP',
        'beginSD',
        'bitRead',
        'connect',
        'display',
        'drawBMP',
        'getBand',
        'getIMEI',
        'isAlpha',
        'isAscii',
        'isDigit',
        'isGraph',
        'isPunct',
        'isSpace',
        'isValid',
        'localIP',
        'lowByte',
        'noBlink',
        'pinMode',
        'pointTo',
        'prepare',
        'println',
        'process',
        'pulseIn',
        'readRed',
        'release',
        'running',
        'setBand',
        'setMode',
        'shiftIn',
        'Ethernet',
        'GSMModem',
        'Keyboard',
        'attached',
        'beginSMS',
        'beginTFT',
        'bitClear',
        'bitWrite',
        'checkPIN',
        'checkPUK',
        'checkReg',
        'endWrite',
        'hangCall',
        'highByte',
        'knobRead',
        'maintain',
        'noBuffer',
        'noCursor',
        'noStroke',
        'overflow',
        'parseInt',
        'playFile',
        'position',
        'readBlue',
        'remoteIP',
        'setSpeed',
        'shiftOut',
        'shutdown',
        'transfer',
        'updateIR',
        'writeRGB',
        'writeRed',
        'GSMClient',
        'GSMServer',
        'IPAddress',
        'Scheduler',
        'YunClient',
        'YunServer',
        'available',
        'changePIN',
        'connected',
        'constrain',
        'endPacket',
        'exitValue',
        'findUntil',
        'gatewayIP',
        'getButton',
        'getOemKey',
        'getResult',
        'getSocket',
        'isControl',
        'isPressed',
        'loadImage',
        'noDisplay',
        'onReceive',
        'onRequest',
        'pauseMode',
        'readBytes',
        'readGreen',
        'sendSysex',
        'setCursor',
        'startLoop',
        'switchPIN',
        'tuneWrite',
        'voiceCall',
        'writeBlue',
        'writeJSON',
        'EsploraTFT',
        'FileSystem',
        'GSMScanner',
        'HttpClient',
        'RobotMotor',
        'WiFiClient',
        'WiFiServer',
        'analogRead',
        'answerCall',
        'attachGPRS',
        'autoscroll',
        'background',
        'beginWrite',
        'createChar',
        'debugPrint',
        'disconnect',
        'getPINUsed',
        'getXChange',
        'getYChange',
        'interrupts',
        'keyPressed',
        'macAddress',
        'motorsStop',
        'mouseMoved',
        'parseFloat',
        'playMelody',
        'randomSeed',
        'readButton',
        'readSlider',
        'readString',
        'releaseAll',
        'remotePort',
        'sendAnalog',
        'sendString',
        'setPINUsed',
        'setTimeout',
        'subnetMask',
        'tempoWrite',
        'writeGreen',
        'EthernetUDP',
        'analogWrite',
        'beginPacket',
        'clearScreen',
        'compassRead',
        'digitalRead',
        'drawCompass',
        'isDirectory',
        'isListening',
        'isLowerCase',
        'isPrintable',
        'isUpperCase',
        'keyReleased',
        'leftToRight',
        'motorsWrite',
        'parsePacket',
        'readMessage',
        'requestFrom',
        'rightToLeft',
        'serialEvent',
        'setBitOrder',
        'setDataMode',
        'setTextSize',
        'GSMVoiceCall',
        'RobotControl',
        'addParameter',
        'beginSpeaker',
        'blinkVersion',
        'cityNameRead',
        'digitalWrite',
        'displayLogos',
        'getModifiers',
        'isActionDone',
        'isWhitespace',
        'keyboardRead',
        'mouseDragged',
        'mousePressed',
        'noAutoscroll',
        'noInterrupts',
        'openNextFile',
        'parseCommand',
        'printVersion',
        'processInput',
        'readNetworks',
        'remoteNumber',
        'scanNetworks',
        'userNameRead',
        'waitContinue',
        'writeMessage',
        'LiquidCrystal',
        'cityNameWrite',
        'mouseReleased',
        'readJoystickX',
        'readJoystickY',
        'robotNameRead',
        'userNameWrite',
        'EthernetClient',
        'EthernetServer',
        'SoftwareSerial',
        'encryptionType',
        'isAlphaNumeric',
        'readBytesUntil',
        'readMicrophone',
        'robotNameWrite',
        'MouseController',
        'analogReference',
        'attachInterrupt',
        'countryNameRead',
        'detachInterrupt',
        'endTransmission',
        'readLightSensor',
        'readStringUntil',
        'readTemperature',
        'rewindDirectory',
        'runShellCommand',
        'setClockDivider',
        'countryNameWrite',
        'lineFollowConfig',
        'messageAvailable',
        'sendDigitalPorts',
        'beginTransmission',
        'delayMicroseconds',
        'getAsynchronously',
        'getCurrentCarrier',
        'getSignalStrength',
        'listenOnLocalhost',
        'readAccelerometer',
        'runAsynchronously',
        'scrollDisplayLeft',
        'writeMicroseconds',
        'KeyboardController',
        'getVoiceCallStatus',
        'isHexadecimalDigit',
        'readJoystickButton',
        'readJoystickSwitch',
        'scrollDisplayRight',
        'setFirmwareVersion',
        'noListenOnLocalhost',
        'sendDigitalPortPair',
        'analogReadResolution',
        'printFirmwareVersion',
        'analogWriteResolution',
        'retrieveCallingNumber',
        'runShellCommandAsynchronously'}
    suppress_highlight = {
        'asm',
        'this',
        'using',
        'typeid',
        'alignof',
        'mutable',
        'decltype',
        'noexcept',
        'restrict',
        'template',
        'typename',
        'constexpr',
        'namespace',
        'thread_local',
        'static_assert'}
    
    def get_tokens_unprocessed(self, text, stack = (('root',),)):
        pass
    # WARNING: Decompyle incomplete



class CharmciLexer(CppLexer):
    '''
    For `Charm++ <https://charm.cs.illinois.edu>`_ interface files (.ci).
    '''
    name = 'Charmci'
    aliases = [
        'charmci']
    filenames = [
        '*.ci']
    version_added = '2.4'
    mimetypes = []
    tokens = {
        'keywords': [
            ('(module)(\\s+)', bygroups(Keyword, Text), 'classname'),
            (words(('mainmodule', 'mainchare', 'chare', 'array', 'group', 'nodegroup', 'message', 'conditional')), Keyword),
            (words(('entry', 'aggregate', 'threaded', 'sync', 'exclusive', 'nokeep', 'notrace', 'immediate', 'expedited', 'inline', 'local', 'python', 'accel', 'readwrite', 'writeonly', 'accelblock', 'memcritical', 'packed', 'varsize', 'initproc', 'initnode', 'initcall', 'stacksize', 'createhere', 'createhome', 'reductiontarget', 'iget', 'nocopy', 'mutable', 'migratable', 'readonly')), Keyword),
            inherit] }


class OmgIdlLexer(CLexer):
    '''
    Lexer for Object Management Group Interface Definition Language.
    '''
    name = 'OMG Interface Definition Language'
    url = 'https://www.omg.org/spec/IDL/About-IDL/'
    aliases = [
        'omg-idl']
    filenames = [
        '*.idl',
        '*.pidl']
    mimetypes = []
    version_added = '2.9'
    scoped_name = '((::)?\\w+)+'
    tokens = {
        'values': [
            (words(('true', 'false'), prefix = '(?i)', suffix = '\\b'), Number),
            ('([Ll]?)(")', bygroups(String.Affix, String.Double), 'string'),
            ("([Ll]?)(\\')(\\\\[^\\']+)(\\')", bygroups(String.Affix, String.Char, String.Escape, String.Char)),
            ("([Ll]?)(\\')(\\\\\\')(\\')", bygroups(String.Affix, String.Char, String.Escape, String.Char)),
            ("([Ll]?)(\\'.\\')", bygroups(String.Affix, String.Char)),
            ('[+-]?\\d+(\\.\\d*)?[Ee][+-]?\\d+', Number.Float),
            ('[+-]?(\\d+\\.\\d*)|(\\d*\\.\\d+)([Ee][+-]?\\d+)?', Number.Float),
            ('(?i)[+-]?0x[0-9a-f]+', Number.Hex),
            ('[+-]?[1-9]\\d*', Number.Integer),
            ('[+-]?0[0-7]*', Number.Oct),
            ('[\\+\\-\\*\\/%^&\\|~]', Operator),
            (words(('<<', '>>')), Operator),
            (scoped_name, Name),
            ('[{};:,<>\\[\\]]', Punctuation)],
        'annotation_params': [
            include('whitespace'),
            ('\\(', Punctuation, '#push'),
            include('values'),
            ('=', Punctuation),
            ('\\)', Punctuation, '#pop')],
        'annotation_params_maybe': [
            ('\\(', Punctuation, 'annotation_params'),
            include('whitespace'),
            default('#pop')],
        'annotation_appl': [
            ('@' + scoped_name, Name.Decorator, 'annotation_params_maybe')],
        'enum': [
            include('whitespace'),
            ('[{,]', Punctuation),
            ('\\w+', Name.Constant),
            include('annotation_appl'),
            ('\\}', Punctuation, '#pop')],
        'root': [
            include('whitespace'),
            (words(('typedef', 'const', 'in', 'out', 'inout', 'local'), prefix = '(?i)', suffix = '\\b'), Keyword.Declaration),
            (words(('void', 'any', 'native', 'bitfield', 'unsigned', 'boolean', 'char', 'wchar', 'octet', 'short', 'long', 'int8', 'uint8', 'int16', 'int32', 'int64', 'uint16', 'uint32', 'uint64', 'float', 'double', 'fixed', 'sequence', 'string', 'wstring', 'map'), prefix = '(?i)', suffix = '\\b'), Keyword.Type),
            (words(('@annotation', 'struct', 'union', 'bitset', 'interface', 'exception', 'valuetype', 'eventtype', 'component'), prefix = '(?i)', suffix = '(\\s+)(\\w+)'), bygroups(Keyword, Whitespace, Name.Class)),
            (words(('abstract', 'alias', 'attribute', 'case', 'connector', 'consumes', 'context', 'custom', 'default', 'emits', 'factory', 'finder', 'getraises', 'home', 'import', 'manages', 'mirrorport', 'multiple', 'Object', 'oneway', 'primarykey', 'private', 'port', 'porttype', 'provides', 'public', 'publishes', 'raises', 'readonly', 'setraises', 'supports', 'switch', 'truncatable', 'typeid', 'typename', 'typeprefix', 'uses', 'ValueBase'), prefix = '(?i)', suffix = '\\b'), Keyword),
            ('(?i)(enum|bitmask)(\\s+)(\\w+)', bygroups(Keyword, Whitespace, Name.Class), 'enum'),
            ('(?i)(module)(\\s+)(\\w+)', bygroups(Keyword.Namespace, Whitespace, Name.Namespace)),
            ('(\\w+)(\\s*)(=)', bygroups(Name.Constant, Whitespace, Operator)),
            ('[\\(\\)]', Punctuation),
            include('values'),
            include('annotation_appl')] }


class PromelaLexer(CLexer):
    '''
    For the Promela language used with SPIN.
    '''
    name = 'Promela'
    aliases = [
        'promela']
    filenames = [
        '*.pml',
        '*.prom',
        '*.prm',
        '*.promela',
        '*.pr',
        '*.pm']
    mimetypes = [
        'text/x-promela']
    url = 'https://spinroot.com/spin/whatispin.html'
    version_added = '2.18'
    tokens = {
        'statements': [
            ('(\\[\\]|<>|/\\\\|\\\\/)|(U|W|V)\\b', Operator),
            ('@', Punctuation),
            ('(\\.)([a-zA-Z_]\\w*)', bygroups(Operator, Name.Attribute)),
            inherit],
        'types': [
            (words(('bit', 'bool', 'byte', 'pid', 'short', 'int', 'unsigned'), suffix = '\\b'), Keyword.Type)],
        'keywords': [
            (words(('atomic', 'break', 'd_step', 'do', 'od', 'for', 'in', 'goto', 'if', 'fi', 'unless'), suffix = '\\b'), Keyword),
            (words(('assert', 'get_priority', 'printf', 'printm', 'set_priority'), suffix = '\\b'), Name.Function),
            (words(('c_code', 'c_decl', 'c_expr', 'c_state', 'c_track'), suffix = '\\b'), Keyword),
            (words(('_', '_last', '_nr_pr', '_pid', '_priority', 'else', 'np_', 'STDIN'), suffix = '\\b'), Name.Builtin),
            (words(('empty', 'enabled', 'eval', 'full', 'len', 'nempty', 'nfull', 'pc_value'), suffix = '\\b'), Name.Function),
            ('run\\b', Operator.Word),
            (words(('active', 'chan', 'D_proctype', 'hidden', 'init', 'local', 'mtype', 'never', 'notrace', 'proctype', 'show', 'trace', 'typedef', 'xr', 'xs'), suffix = '\\b'), Keyword.Declaration),
            (words(('priority', 'provided'), suffix = '\\b'), Keyword),
            (words(('inline', 'ltl', 'select'), suffix = '\\b'), Keyword.Declaration),
            ('skip\\b', Keyword)] }
