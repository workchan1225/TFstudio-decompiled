# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: jvm.pyc (Python 3.11)

'''
    pygments.lexers.jvm
    ~~~~~~~~~~~~~~~~~~~

    Pygments lexers for JVM languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import Lexer, RegexLexer, include, bygroups, using, this, combined, default, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Whitespace
from pygments.util import shebang_matches
from pygments import unistring as uni
__all__ = [
    'JavaLexer',
    'ScalaLexer',
    'GosuLexer',
    'GosuTemplateLexer',
    'GroovyLexer',
    'IokeLexer',
    'ClojureLexer',
    'ClojureScriptLexer',
    'KotlinLexer',
    'XtendLexer',
    'AspectJLexer',
    'CeylonLexer',
    'PigLexer',
    'GoloLexer',
    'JasminLexer',
    'SarlLexer']

class JavaLexer(RegexLexer):
    '''
    For Java source code.
    '''
    name = 'Java'
    url = 'https://www.oracle.com/technetwork/java/'
    aliases = [
        'java']
    filenames = [
        '*.java']
    mimetypes = [
        'text/x-java']
    version_added = ''
    flags = re.MULTILINE | re.DOTALL
    tokens = {
        'root': [
            ('(^\\s*)((?:(?:public|private|protected|static|strictfp)(?:\\s+))*)(record)\\b', bygroups(Whitespace, using(this), Keyword.Declaration), 'class'),
            ('[^\\S\\n]+', Whitespace),
            ('(//.*?)(\\n)', bygroups(Comment.Single, Whitespace)),
            ('/\\*.*?\\*/', Comment.Multiline),
            ('(assert|break|case|catch|continue|default|do|else|finally|for|if|goto|instanceof|new|return|switch|this|throw|try|while)\\b', Keyword),
            ('((?:(?:[^\\W\\d]|\\$)[\\w.\\[\\]$<>?]*\\s+)+?)((?:[^\\W\\d]|\\$)[\\w$]*)(\\s*)(\\()', bygroups(using(this), Name.Function, Whitespace, Punctuation)),
            ('@[^\\W\\d][\\w.]*', Name.Decorator),
            ('(abstract|const|enum|extends|final|implements|native|private|protected|public|sealed|static|strictfp|super|synchronized|throws|transient|volatile|yield)\\b', Keyword.Declaration),
            ('(boolean|byte|char|double|float|int|long|short|void)\\b', Keyword.Type),
            ('(package)(\\s+)', bygroups(Keyword.Namespace, Whitespace), 'import'),
            ('(true|false|null)\\b', Keyword.Constant),
            ('(class|interface)\\b', Keyword.Declaration, 'class'),
            ('(var)(\\s+)', bygroups(Keyword.Declaration, Whitespace), 'var'),
            ('(import(?:\\s+static)?)(\\s+)', bygroups(Keyword.Namespace, Whitespace), 'import'),
            ('"""\\n', String, 'multiline_string'),
            ('"', String, 'string'),
            ("'\\\\.'|'[^\\\\]'|'\\\\u[0-9a-fA-F]{4}'", String.Char),
            ('(\\.)((?:[^\\W\\d]|\\$)[\\w$]*)', bygroups(Punctuation, Name.Attribute)),
            ('^(\\s*)(default)(:)', bygroups(Whitespace, Keyword, Punctuation)),
            ('^(\\s*)((?:[^\\W\\d]|\\$)[\\w$]*)(:)', bygroups(Whitespace, Name.Label, Punctuation)),
            ('([^\\W\\d]|\\$)[\\w$]*', Name),
            ('([0-9][0-9_]*\\.([0-9][0-9_]*)?|\\.[0-9][0-9_]*)([eE][+\\-]?[0-9][0-9_]*)?[fFdD]?|[0-9][eE][+\\-]?[0-9][0-9_]*[fFdD]?|[0-9]([eE][+\\-]?[0-9][0-9_]*)?[fFdD]|0[xX]([0-9a-fA-F][0-9a-fA-F_]*\\.?|([0-9a-fA-F][0-9a-fA-F_]*)?\\.[0-9a-fA-F][0-9a-fA-F_]*)[pP][+\\-]?[0-9][0-9_]*[fFdD]?', Number.Float),
            ('0[xX][0-9a-fA-F][0-9a-fA-F_]*[lL]?', Number.Hex),
            ('0[bB][01][01_]*[lL]?', Number.Bin),
            ('0[0-7_]+[lL]?', Number.Oct),
            ('0|[1-9][0-9_]*[lL]?', Number.Integer),
            ('[~^*!%&\\[\\]<>|+=/?-]', Operator),
            ('[{}();:.,]', Punctuation),
            ('\\n', Whitespace)],
        'class': [
            ('\\s+', Text),
            ('([^\\W\\d]|\\$)[\\w$]*', Name.Class, '#pop')],
        'var': [
            ('([^\\W\\d]|\\$)[\\w$]*', Name, '#pop')],
        'import': [
            ('[\\w.]+\\*?', Name.Namespace, '#pop')],
        'multiline_string': [
            ('"""', String, '#pop'),
            ('"', String),
            include('string')],
        'string': [
            ('[^\\\\"]+', String),
            ('\\\\\\\\', String),
            ('\\\\"', String),
            ('\\\\', String),
            ('"', String, '#pop')] }


class AspectJLexer(JavaLexer):
    '''
    For AspectJ source code.
    '''
    name = 'AspectJ'
    url = 'http://www.eclipse.org/aspectj/'
    aliases = [
        'aspectj']
    filenames = [
        '*.aj']
    mimetypes = [
        'text/x-aspectj']
    version_added = '1.6'
    aj_keywords = {
        'get',
        'set',
        'args',
        'call',
        'lock',
        'soft',
        'after',
        'cflow',
        'error',
        'around',
        'aspect',
        'before',
        'target',
        'unlock',
        'within',
        'declare',
        'handler',
        'parents',
        'perthis',
        'proceed',
        'warning',
        'percflow',
        'pointcut',
        'throwing',
        'execution',
        'pertarget',
        'returning',
        'annotation',
        'cflowbelow',
        'precedence',
        'privileged',
        'withincode',
        'issingleton',
        'percflowbelow',
        'pertypewithin',
        'thisJoinPoint',
        'initialization',
        'adviceexecution',
        'preinitialization',
        'thisAspectInstance',
        'staticinitialization',
        'thisJoinPointStaticPart',
        'thisEnclosingJoinPointStaticPart'}
    aj_inter_type = {
        'soft:',
        'error:',
        'parents:',
        'warning:',
        'precedence:'}
    aj_inter_type_annotation = {
        '@type',
        '@field',
        '@method',
        '@constructor'}
    
    def get_tokens_unprocessed(self, text):
        pass
    # WARNING: Decompyle incomplete



class ScalaLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'ScalaLexer'
    __doc__ = '\n    For Scala source code.\n    '
    name = 'Scala'
    url = 'http://www.scala-lang.org'
    aliases = [
        'scala']
    filenames = [
        '*.scala']
    mimetypes = [
        'text/x-scala']
    version_added = ''
    flags = re.MULTILINE | re.DOTALL
    opchar = '[!#%&*\\-\\/:?@^' + uni.combine('Sm', 'So') + ']'
    letter = '[_\\$' + uni.combine('Ll', 'Lu', 'Lo', 'Nl', 'Lt') + ']'
    upperLetter = '[' + uni.combine('Lu', 'Lt') + ']'
    letterOrDigit = f'''(?:{letter}|[0-9])'''
    letterOrDigitNoDollarSign = '(?:{}|[0-9])'.format(letter.replace('\\$', ''))
    alphaId = f'''{letter}+'''
    simpleInterpolatedVariable = f'''{letter}{letterOrDigitNoDollarSign}*'''
    idrest = f'''{letter}{letterOrDigit}*(?:(?<=_){opchar}+)?'''
    idUpper = f'''{upperLetter}{letterOrDigit}*(?:(?<=_){opchar}+)?'''
    plainid = f'''(?:{idrest}|{opchar}+)'''
    backQuotedId = '`[^`]+`'
    anyId = f'''(?:{plainid}|{backQuotedId})'''
    notStartOfComment = '(?!//|/\\*)'
    endOfLineMaybeWithComment = '(?=\\s*(//|$))'
    keywords = ('new', 'return', 'throw', 'classOf', 'isInstanceOf', 'asInstanceOf', 'else', 'if', 'then', 'do', 'while', 'for', 'yield', 'match', 'case', 'catch', 'finally', 'try')
    operators = ('<%', '=:=', '<:<', '<%<', '>:', '<:', '=', '==', '!=', '<=', '>=', '<>', '<', '>', '<-', '←', '->', '→', '=>', '⇒', '?', '@', '|', '-', '+', '*', '%', '~', '\\')
    storage_modifiers = ('private', 'protected', 'synchronized', '@volatile', 'abstract', 'final', 'lazy', 'sealed', 'implicit', 'override', '@transient', '@native')
# WARNING: Decompyle incomplete


class GosuLexer(RegexLexer):
    '''
    For Gosu source code.
    '''
    name = 'Gosu'
    aliases = [
        'gosu']
    filenames = [
        '*.gs',
        '*.gsx',
        '*.gsp',
        '*.vark']
    mimetypes = [
        'text/x-gosu']
    url = 'https://gosu-lang.github.io'
    version_added = '1.5'
    flags = re.MULTILINE | re.DOTALL
    tokens = {
        'root': [
            ('^(\\s*(?:[a-zA-Z_][\\w.\\[\\]]*\\s+)+?)([a-zA-Z_]\\w*)(\\s*)(\\()', bygroups(using(this), Name.Function, Whitespace, Operator)),
            ('[^\\S\\n]+', Whitespace),
            ('//.*?\\n', Comment.Single),
            ('/\\*.*?\\*/', Comment.Multiline),
            ('@[a-zA-Z_][\\w.]*', Name.Decorator),
            ('(in|as|typeof|statictypeof|typeis|typeas|if|else|foreach|for|index|while|do|continue|break|return|try|catch|finally|this|throw|new|switch|case|default|eval|super|outer|classpath|using)\\b', Keyword),
            ('(var|delegate|construct|function|private|internal|protected|public|abstract|override|final|static|extends|transient|implements|represents|readonly)\\b', Keyword.Declaration),
            ('(property)(\\s+)(get|set)?', bygroups(Keyword.Declaration, Whitespace, Keyword.Declaration)),
            ('(boolean|byte|char|double|float|int|long|short|void|block)\\b', Keyword.Type),
            ('(package)(\\s+)', bygroups(Keyword.Namespace, Whitespace)),
            ('(true|false|null|NaN|Infinity)\\b', Keyword.Constant),
            ('(class|interface|enhancement|enum)(\\s+)([a-zA-Z_]\\w*)', bygroups(Keyword.Declaration, Whitespace, Name.Class)),
            ('(uses)(\\s+)([\\w.]+\\*?)', bygroups(Keyword.Namespace, Whitespace, Name.Namespace)),
            ('"', String, 'string'),
            ('(\\??[.#])([a-zA-Z_]\\w*)', bygroups(Operator, Name.Attribute)),
            ('(:)([a-zA-Z_]\\w*)', bygroups(Operator, Name.Attribute)),
            ('[a-zA-Z_$]\\w*', Name),
            ('and|or|not|[\\\\~^*!%&\\[\\](){}<>|+=:;,./?-]', Operator),
            ('[0-9][0-9]*\\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            ('[0-9]+', Number.Integer),
            ('\\n', Whitespace)],
        'templateText': [
            ('(\\\\<)|(\\\\\\$)', String),
            ('(<%@\\s+)(extends|params)', bygroups(Operator, Name.Decorator), 'stringTemplate'),
            ('<%!--.*?--%>', Comment.Multiline),
            ('(<%)|(<%=)', Operator, 'stringTemplate'),
            ('\\$\\{', Operator, 'stringTemplateShorthand'),
            ('.', String)],
        'string': [
            ('"', String, '#pop'),
            include('templateText')],
        'stringTemplate': [
            ('"', String, 'string'),
            ('%>', Operator, '#pop'),
            include('root')],
        'stringTemplateShorthand': [
            ('"', String, 'string'),
            ('\\{', Operator, 'stringTemplateShorthand'),
            ('\\}', Operator, '#pop'),
            include('root')] }


class GosuTemplateLexer(Lexer):
    '''
    For Gosu templates.
    '''
    name = 'Gosu Template'
    aliases = [
        'gst']
    filenames = [
        '*.gst']
    mimetypes = [
        'text/x-gosu-template']
    url = 'https://gosu-lang.github.io'
    version_added = '1.5'
    
    def get_tokens_unprocessed(self, text):
        pass
    # WARNING: Decompyle incomplete



class GroovyLexer(RegexLexer):
    '''
    For Groovy source code.
    '''
    name = 'Groovy'
    url = 'https://groovy-lang.org/'
    aliases = [
        'groovy']
    filenames = [
        '*.groovy',
        '*.gradle']
    mimetypes = [
        'text/x-groovy']
    version_added = '1.5'
    flags = re.MULTILINE | re.DOTALL
    tokens = {
        'root': [
            ('#!(.*?)$', Comment.Preproc, 'base'),
            default('base')],
        'base': [
            ('[^\\S\\n]+', Whitespace),
            ('(//.*?)(\\n)', bygroups(Comment.Single, Whitespace)),
            ('/\\*.*?\\*/', Comment.Multiline),
            ('(assert|break|case|catch|continue|default|do|else|finally|for|if|goto|instanceof|new|return|switch|this|throw|try|while|in|as)\\b', Keyword),
            ('^(\\s*(?:[a-zA-Z_][\\w.\\[\\]]*\\s+)+?)([a-zA-Z_]\\w*|"(?:\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"|\'(?:\\\\\\\\|\\\\[^\\\\]|[^\'\\\\])*\')(\\s*)(\\()', bygroups(using(this), Name.Function, Whitespace, Operator)),
            ('@[a-zA-Z_][\\w.]*', Name.Decorator),
            ('(abstract|const|enum|extends|final|implements|native|private|protected|public|static|strictfp|super|synchronized|throws|transient|volatile)\\b', Keyword.Declaration),
            ('(def|boolean|byte|char|double|float|int|long|short|void)\\b', Keyword.Type),
            ('(package)(\\s+)', bygroups(Keyword.Namespace, Whitespace)),
            ('(true|false|null)\\b', Keyword.Constant),
            ('(class|interface)(\\s+)', bygroups(Keyword.Declaration, Whitespace), 'class'),
            ('(import)(\\s+)', bygroups(Keyword.Namespace, Whitespace), 'import'),
            ('""".*?"""', String.Double),
            ("'''.*?'''", String.Single),
            ('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            ("'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single),
            ('\\$/((?!/\\$).)*/\\$', String),
            ('/(\\\\\\\\|\\\\[^\\\\]|[^/\\\\])*/', String),
            ("'\\\\.'|'[^\\\\]'|'\\\\u[0-9a-fA-F]{4}'", String.Char),
            ('(\\.)([a-zA-Z_]\\w*)', bygroups(Operator, Name.Attribute)),
            ('[a-zA-Z_]\\w*:', Name.Label),
            ('[a-zA-Z_$]\\w*', Name),
            ('[~^*!%&\\[\\](){}<>|+=:;,./?-]', Operator),
            ('[0-9][0-9]*\\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            ('0x[0-9a-fA-F]+', Number.Hex),
            ('[0-9]+L?', Number.Integer),
            ('\\n', Whitespace)],
        'class': [
            ('[a-zA-Z_]\\w*', Name.Class, '#pop')],
        'import': [
            ('[\\w.]+\\*?', Name.Namespace, '#pop')] }
    
    def analyse_text(text):
        return shebang_matches(text, 'groovy')



class IokeLexer(RegexLexer):
    '''
    For Ioke (a strongly typed, dynamic,
    prototype based programming language) source.
    '''
    name = 'Ioke'
    url = 'https://ioke.org/'
    filenames = [
        '*.ik']
    aliases = [
        'ioke',
        'ik']
    mimetypes = [
        'text/x-iokesrc']
    version_added = '1.4'
    tokens = {
        'interpolatableText': [][('\\n', Whitespace)][('\\s+', Whitespace)][(';(.*?)\\n', Comment)][('\\A#!(.*?)\\n', Comment)][('#/', String.Regex, 'slashRegexp')][('#r\\[', String.Regex, 'squareRegexp')][(':[\\w!:?]+', String.Symbol)][('[\\w!:?]+:(?![\\w!?])', String.Other)][(':"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Symbol)][('((?<=fn\\()|(?<=fnx\\()|(?<=method\\()|(?<=macro\\()|(?<=lecro\\()|(?<=syntax\\()|(?<=dmacro\\()|(?<=dlecro\\()|(?<=dlecrox\\()|(?<=dsyntax\\())(\\s*)"', String.Doc, 'documentation')][('"', String, 'text')][('#\\[', String, 'squareText')][('\\w[\\w!:?]+(?=\\s*=.*mimic\\s)', Name.Entity)][('[a-zA-Z_][\\w!:?]*(?=[\\s]*[+*/-]?=[^=].*($|\\.))', Name.Variable)][('(break|cond|continue|do|ensure|for|for:dict|for:set|if|let|loop|p:for|p:for:dict|p:for:set|return|unless|until|while|with)(?![\\w!:?])', Keyword.Reserved)][('(eval|mimic|print|println)(?![\\w!:?])', Keyword)][('(cell\\?|cellNames|cellOwner\\?|cellOwner|cells|cell|documentation|hash|identity|mimic|removeCell\\!|undefineCell\\!)(?![\\w!:?])', Keyword)][('(stackTraceAsText)(?![\\w!:?])', Keyword)][('(dict|list|message|set)(?![\\w!:?])', Keyword.Reserved)][('(case|case:and|case:else|case:nand|case:nor|case:not|case:or|case:otherwise|case:xor)(?![\\w!:?])', Keyword.Reserved)][('(asText|become\\!|derive|freeze\\!|frozen\\?|in\\?|is\\?|kind\\?|mimic\\!|mimics|mimics\\?|prependMimic\\!|removeAllMimics\\!|removeMimic\\!|same\\?|send|thaw\\!|uniqueHexId)(?![\\w!:?])', Keyword)][('(after|around|before)(?![\\w!:?])', Keyword.Reserved)][('(kind|cellDescriptionDict|cellSummary|genSym|inspect|notice)(?![\\w!:?])', Keyword)][('(use|destructuring)', Keyword.Reserved)][('(cell\\?|cellOwner\\?|cellOwner|cellNames|cells|cell|documentation|identity|removeCell!|undefineCell)(?![\\w!:?])', Keyword)][('(internal:compositeRegexp|internal:concatenateText|internal:createDecimal|internal:createNumber|internal:createRegexp|internal:createText)(?![\\w!:?])', Keyword.Reserved)][('(availableRestarts|bind|error\\!|findRestart|handle|invokeRestart|rescue|restart|signal\\!|warn\\!)(?![\\w!:?])', Keyword.Reserved)][('(nil|false|true)(?![\\w!:?])', Name.Constant)][('(Arity|Base|Call|Condition|DateTime|Aspects|Pointcut|Assignment|BaseBehavior|Boolean|Case|AndCombiner|Else|NAndCombiner|NOrCombiner|NotCombiner|OrCombiner|XOrCombiner|Conditions|Definitions|FlowControl|Internal|Literals|Reflection|DefaultMacro|DefaultMethod|DefaultSyntax|Dict|FileSystem|Ground|Handler|Hook|IO|IokeGround|Struct|LexicalBlock|LexicalMacro|List|Message|Method|Mixins|NativeMethod|Number|Origin|Pair|Range|Reflector|Regexp Match|Regexp|Rescue|Restart|Runtime|Sequence|Set|Symbol|System|Text|Tuple)(?![\\w!:?])', Name.Builtin)][('(generateMatchMethod|aliasMethod|λ|ʎ|fnx|fn|method|dmacro|dlecro|syntax|macro|dlecrox|lecrox|lecro|syntax)(?![\\w!:?])', Name.Function)][('-?0[xX][0-9a-fA-F]+', Number.Hex)][('-?(\\d+\\.?\\d*|\\d*\\.\\d+)([eE][+-]?[0-9]+)?', Number.Float)],
        'text': [][('\\n', Whitespace)][('\\s+', Whitespace)][(';(.*?)\\n', Comment)][('\\A#!(.*?)\\n', Comment)][('#/', String.Regex, 'slashRegexp')][('#r\\[', String.Regex, 'squareRegexp')][(':[\\w!:?]+', String.Symbol)][('[\\w!:?]+:(?![\\w!?])', String.Other)][(':"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Symbol)][('((?<=fn\\()|(?<=fnx\\()|(?<=method\\()|(?<=macro\\()|(?<=lecro\\()|(?<=syntax\\()|(?<=dmacro\\()|(?<=dlecro\\()|(?<=dlecrox\\()|(?<=dsyntax\\())(\\s*)"', String.Doc, 'documentation')][('"', String, 'text')][('#\\[', String, 'squareText')][('\\w[\\w!:?]+(?=\\s*=.*mimic\\s)', Name.Entity)][('[a-zA-Z_][\\w!:?]*(?=[\\s]*[+*/-]?=[^=].*($|\\.))', Name.Variable)][('(break|cond|continue|do|ensure|for|for:dict|for:set|if|let|loop|p:for|p:for:dict|p:for:set|return|unless|until|while|with)(?![\\w!:?])', Keyword.Reserved)][('(eval|mimic|print|println)(?![\\w!:?])', Keyword)][('(cell\\?|cellNames|cellOwner\\?|cellOwner|cells|cell|documentation|hash|identity|mimic|removeCell\\!|undefineCell\\!)(?![\\w!:?])', Keyword)][('(stackTraceAsText)(?![\\w!:?])', Keyword)][('(dict|list|message|set)(?![\\w!:?])', Keyword.Reserved)][('(case|case:and|case:else|case:nand|case:nor|case:not|case:or|case:otherwise|case:xor)(?![\\w!:?])', Keyword.Reserved)][('(asText|become\\!|derive|freeze\\!|frozen\\?|in\\?|is\\?|kind\\?|mimic\\!|mimics|mimics\\?|prependMimic\\!|removeAllMimics\\!|removeMimic\\!|same\\?|send|thaw\\!|uniqueHexId)(?![\\w!:?])', Keyword)][('(after|around|before)(?![\\w!:?])', Keyword.Reserved)][('(kind|cellDescriptionDict|cellSummary|genSym|inspect|notice)(?![\\w!:?])', Keyword)][('(use|destructuring)', Keyword.Reserved)][('(cell\\?|cellOwner\\?|cellOwner|cellNames|cells|cell|documentation|identity|removeCell!|undefineCell)(?![\\w!:?])', Keyword)][('(internal:compositeRegexp|internal:concatenateText|internal:createDecimal|internal:createNumber|internal:createRegexp|internal:createText)(?![\\w!:?])', Keyword.Reserved)][('(availableRestarts|bind|error\\!|findRestart|handle|invokeRestart|rescue|restart|signal\\!|warn\\!)(?![\\w!:?])', Keyword.Reserved)][('(nil|false|true)(?![\\w!:?])', Name.Constant)][('(Arity|Base|Call|Condition|DateTime|Aspects|Pointcut|Assignment|BaseBehavior|Boolean|Case|AndCombiner|Else|NAndCombiner|NOrCombiner|NotCombiner|OrCombiner|XOrCombiner|Conditions|Definitions|FlowControl|Internal|Literals|Reflection|DefaultMacro|DefaultMethod|DefaultSyntax|Dict|FileSystem|Ground|Handler|Hook|IO|IokeGround|Struct|LexicalBlock|LexicalMacro|List|Message|Method|Mixins|NativeMethod|Number|Origin|Pair|Range|Reflector|Regexp Match|Regexp|Rescue|Restart|Runtime|Sequence|Set|Symbol|System|Text|Tuple)(?![\\w!:?])', Name.Builtin)][('(generateMatchMethod|aliasMethod|λ|ʎ|fnx|fn|method|dmacro|dlecro|syntax|macro|dlecrox|lecrox|lecro|syntax)(?![\\w!:?])', Name.Function)][('-?0[xX][0-9a-fA-F]+', Number.Hex)][('-?(\\d+\\.?\\d*|\\d*\\.\\d+)([eE][+-]?[0-9]+)?', Number.Float)][('-?\\d+', Number.Integer)],
        'documentation': [][('\\n', Whitespace)][('\\s+', Whitespace)][(';(.*?)\\n', Comment)][('\\A#!(.*?)\\n', Comment)][('#/', String.Regex, 'slashRegexp')][('#r\\[', String.Regex, 'squareRegexp')][(':[\\w!:?]+', String.Symbol)][('[\\w!:?]+:(?![\\w!?])', String.Other)][(':"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Symbol)][('((?<=fn\\()|(?<=fnx\\()|(?<=method\\()|(?<=macro\\()|(?<=lecro\\()|(?<=syntax\\()|(?<=dmacro\\()|(?<=dlecro\\()|(?<=dlecrox\\()|(?<=dsyntax\\())(\\s*)"', String.Doc, 'documentation')][('"', String, 'text')][('#\\[', String, 'squareText')][('\\w[\\w!:?]+(?=\\s*=.*mimic\\s)', Name.Entity)][('[a-zA-Z_][\\w!:?]*(?=[\\s]*[+*/-]?=[^=].*($|\\.))', Name.Variable)][('(break|cond|continue|do|ensure|for|for:dict|for:set|if|let|loop|p:for|p:for:dict|p:for:set|return|unless|until|while|with)(?![\\w!:?])', Keyword.Reserved)][('(eval|mimic|print|println)(?![\\w!:?])', Keyword)][('(cell\\?|cellNames|cellOwner\\?|cellOwner|cells|cell|documentation|hash|identity|mimic|removeCell\\!|undefineCell\\!)(?![\\w!:?])', Keyword)][('(stackTraceAsText)(?![\\w!:?])', Keyword)][('(dict|list|message|set)(?![\\w!:?])', Keyword.Reserved)][('(case|case:and|case:else|case:nand|case:nor|case:not|case:or|case:otherwise|case:xor)(?![\\w!:?])', Keyword.Reserved)][('(asText|become\\!|derive|freeze\\!|frozen\\?|in\\?|is\\?|kind\\?|mimic\\!|mimics|mimics\\?|prependMimic\\!|removeAllMimics\\!|removeMimic\\!|same\\?|send|thaw\\!|uniqueHexId)(?![\\w!:?])', Keyword)][('(after|around|before)(?![\\w!:?])', Keyword.Reserved)][('(kind|cellDescriptionDict|cellSummary|genSym|inspect|notice)(?![\\w!:?])', Keyword)][('(use|destructuring)', Keyword.Reserved)][('(cell\\?|cellOwner\\?|cellOwner|cellNames|cells|cell|documentation|identity|removeCell!|undefineCell)(?![\\w!:?])', Keyword)][('(internal:compositeRegexp|internal:concatenateText|internal:createDecimal|internal:createNumber|internal:createRegexp|internal:createText)(?![\\w!:?])', Keyword.Reserved)][('(availableRestarts|bind|error\\!|findRestart|handle|invokeRestart|rescue|restart|signal\\!|warn\\!)(?![\\w!:?])', Keyword.Reserved)][('(nil|false|true)(?![\\w!:?])', Name.Constant)][('(Arity|Base|Call|Condition|DateTime|Aspects|Pointcut|Assignment|BaseBehavior|Boolean|Case|AndCombiner|Else|NAndCombiner|NOrCombiner|NotCombiner|OrCombiner|XOrCombiner|Conditions|Definitions|FlowControl|Internal|Literals|Reflection|DefaultMacro|DefaultMethod|DefaultSyntax|Dict|FileSystem|Ground|Handler|Hook|IO|IokeGround|Struct|LexicalBlock|LexicalMacro|List|Message|Method|Mixins|NativeMethod|Number|Origin|Pair|Range|Reflector|Regexp Match|Regexp|Rescue|Restart|Runtime|Sequence|Set|Symbol|System|Text|Tuple)(?![\\w!:?])', Name.Builtin)][('(generateMatchMethod|aliasMethod|λ|ʎ|fnx|fn|method|dmacro|dlecro|syntax|macro|dlecrox|lecrox|lecro|syntax)(?![\\w!:?])', Name.Function)][('-?0[xX][0-9a-fA-F]+', Number.Hex)][('-?(\\d+\\.?\\d*|\\d*\\.\\d+)([eE][+-]?[0-9]+)?', Number.Float)][('-?\\d+', Number.Integer)][('#\\(', Punctuation)],
        'textInterpolationRoot': [][('\\n', Whitespace)][('\\s+', Whitespace)][(';(.*?)\\n', Comment)][('\\A#!(.*?)\\n', Comment)][('#/', String.Regex, 'slashRegexp')][('#r\\[', String.Regex, 'squareRegexp')][(':[\\w!:?]+', String.Symbol)][('[\\w!:?]+:(?![\\w!?])', String.Other)][(':"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Symbol)][('((?<=fn\\()|(?<=fnx\\()|(?<=method\\()|(?<=macro\\()|(?<=lecro\\()|(?<=syntax\\()|(?<=dmacro\\()|(?<=dlecro\\()|(?<=dlecrox\\()|(?<=dsyntax\\())(\\s*)"', String.Doc, 'documentation')][('"', String, 'text')][('#\\[', String, 'squareText')][('\\w[\\w!:?]+(?=\\s*=.*mimic\\s)', Name.Entity)][('[a-zA-Z_][\\w!:?]*(?=[\\s]*[+*/-]?=[^=].*($|\\.))', Name.Variable)][('(break|cond|continue|do|ensure|for|for:dict|for:set|if|let|loop|p:for|p:for:dict|p:for:set|return|unless|until|while|with)(?![\\w!:?])', Keyword.Reserved)][('(eval|mimic|print|println)(?![\\w!:?])', Keyword)][('(cell\\?|cellNames|cellOwner\\?|cellOwner|cells|cell|documentation|hash|identity|mimic|removeCell\\!|undefineCell\\!)(?![\\w!:?])', Keyword)][('(stackTraceAsText)(?![\\w!:?])', Keyword)][('(dict|list|message|set)(?![\\w!:?])', Keyword.Reserved)][('(case|case:and|case:else|case:nand|case:nor|case:not|case:or|case:otherwise|case:xor)(?![\\w!:?])', Keyword.Reserved)][('(asText|become\\!|derive|freeze\\!|frozen\\?|in\\?|is\\?|kind\\?|mimic\\!|mimics|mimics\\?|prependMimic\\!|removeAllMimics\\!|removeMimic\\!|same\\?|send|thaw\\!|uniqueHexId)(?![\\w!:?])', Keyword)][('(after|around|before)(?![\\w!:?])', Keyword.Reserved)][('(kind|cellDescriptionDict|cellSummary|genSym|inspect|notice)(?![\\w!:?])', Keyword)][('(use|destructuring)', Keyword.Reserved)][('(cell\\?|cellOwner\\?|cellOwner|cellNames|cells|cell|documentation|identity|removeCell!|undefineCell)(?![\\w!:?])', Keyword)][('(internal:compositeRegexp|internal:concatenateText|internal:createDecimal|internal:createNumber|internal:createRegexp|internal:createText)(?![\\w!:?])', Keyword.Reserved)][('(availableRestarts|bind|error\\!|findRestart|handle|invokeRestart|rescue|restart|signal\\!|warn\\!)(?![\\w!:?])', Keyword.Reserved)][('(nil|false|true)(?![\\w!:?])', Name.Constant)][('(Arity|Base|Call|Condition|DateTime|Aspects|Pointcut|Assignment|BaseBehavior|Boolean|Case|AndCombiner|Else|NAndCombiner|NOrCombiner|NotCombiner|OrCombiner|XOrCombiner|Conditions|Definitions|FlowControl|Internal|Literals|Reflection|DefaultMacro|DefaultMethod|DefaultSyntax|Dict|FileSystem|Ground|Handler|Hook|IO|IokeGround|Struct|LexicalBlock|LexicalMacro|List|Message|Method|Mixins|NativeMethod|Number|Origin|Pair|Range|Reflector|Regexp Match|Regexp|Rescue|Restart|Runtime|Sequence|Set|Symbol|System|Text|Tuple)(?![\\w!:?])', Name.Builtin)][('(generateMatchMethod|aliasMethod|λ|ʎ|fnx|fn|method|dmacro|dlecro|syntax|macro|dlecrox|lecrox|lecro|syntax)(?![\\w!:?])', Name.Function)][('-?0[xX][0-9a-fA-F]+', Number.Hex)][('-?(\\d+\\.?\\d*|\\d*\\.\\d+)([eE][+-]?[0-9]+)?', Number.Float)][('-?\\d+', Number.Integer)][('#\\(', Punctuation)][('(&&>>|\\|\\|>>|\\*\\*>>|:::|::|\\.\\.\\.|===|\\*\\*>|\\*\\*=|&&>|&&=|\\|\\|>|\\|\\|=|\\->>|\\+>>|!>>|<>>>|<>>|&>>|%>>|#>>|@>>|/>>|\\*>>|\\?>>|\\|>>|\\^>>|~>>|\\$>>|=>>|<<=|>>=|<=>|<\\->|=~|!~|=>|\\+\\+|\\-\\-|<=|>=|==|!=|&&|\\.\\.|\\+=|\\-=|\\*=|\\/=|%=|&=|\\^=|\\|=|<\\-|\\+>|!>|<>|&>|%>|#>|\\@>|\\/>|\\*>|\\?>|\\|>|\\^>|~>|\\$>|<\\->|\\->|<<|>>|\\*\\*|\\?\\||\\?&|\\|\\||>|<|\\*|\\/|%|\\+|\\-|&|\\^|\\||=|\\$|!|~|\\?|#|\\u2260|\\u2218|\\u2208|\\u2209)', Operator)],
        'slashRegexp': [][('\\n', Whitespace)][('\\s+', Whitespace)][(';(.*?)\\n', Comment)][('\\A#!(.*?)\\n', Comment)][('#/', String.Regex, 'slashRegexp')][('#r\\[', String.Regex, 'squareRegexp')][(':[\\w!:?]+', String.Symbol)][('[\\w!:?]+:(?![\\w!?])', String.Other)][(':"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Symbol)][('((?<=fn\\()|(?<=fnx\\()|(?<=method\\()|(?<=macro\\()|(?<=lecro\\()|(?<=syntax\\()|(?<=dmacro\\()|(?<=dlecro\\()|(?<=dlecrox\\()|(?<=dsyntax\\())(\\s*)"', String.Doc, 'documentation')][('"', String, 'text')][('#\\[', String, 'squareText')][('\\w[\\w!:?]+(?=\\s*=.*mimic\\s)', Name.Entity)][('[a-zA-Z_][\\w!:?]*(?=[\\s]*[+*/-]?=[^=].*($|\\.))', Name.Variable)][('(break|cond|continue|do|ensure|for|for:dict|for:set|if|let|loop|p:for|p:for:dict|p:for:set|return|unless|until|while|with)(?![\\w!:?])', Keyword.Reserved)][('(eval|mimic|print|println)(?![\\w!:?])', Keyword)][('(cell\\?|cellNames|cellOwner\\?|cellOwner|cells|cell|documentation|hash|identity|mimic|removeCell\\!|undefineCell\\!)(?![\\w!:?])', Keyword)][('(stackTraceAsText)(?![\\w!:?])', Keyword)][('(dict|list|message|set)(?![\\w!:?])', Keyword.Reserved)][('(case|case:and|case:else|case:nand|case:nor|case:not|case:or|case:otherwise|case:xor)(?![\\w!:?])', Keyword.Reserved)][('(asText|become\\!|derive|freeze\\!|frozen\\?|in\\?|is\\?|kind\\?|mimic\\!|mimics|mimics\\?|prependMimic\\!|removeAllMimics\\!|removeMimic\\!|same\\?|send|thaw\\!|uniqueHexId)(?![\\w!:?])', Keyword)][('(after|around|before)(?![\\w!:?])', Keyword.Reserved)][('(kind|cellDescriptionDict|cellSummary|genSym|inspect|notice)(?![\\w!:?])', Keyword)][('(use|destructuring)', Keyword.Reserved)][('(cell\\?|cellOwner\\?|cellOwner|cellNames|cells|cell|documentation|identity|removeCell!|undefineCell)(?![\\w!:?])', Keyword)][('(internal:compositeRegexp|internal:concatenateText|internal:createDecimal|internal:createNumber|internal:createRegexp|internal:createText)(?![\\w!:?])', Keyword.Reserved)][('(availableRestarts|bind|error\\!|findRestart|handle|invokeRestart|rescue|restart|signal\\!|warn\\!)(?![\\w!:?])', Keyword.Reserved)][('(nil|false|true)(?![\\w!:?])', Name.Constant)][('(Arity|Base|Call|Condition|DateTime|Aspects|Pointcut|Assignment|BaseBehavior|Boolean|Case|AndCombiner|Else|NAndCombiner|NOrCombiner|NotCombiner|OrCombiner|XOrCombiner|Conditions|Definitions|FlowControl|Internal|Literals|Reflection|DefaultMacro|DefaultMethod|DefaultSyntax|Dict|FileSystem|Ground|Handler|Hook|IO|IokeGround|Struct|LexicalBlock|LexicalMacro|List|Message|Method|Mixins|NativeMethod|Number|Origin|Pair|Range|Reflector|Regexp Match|Regexp|Rescue|Restart|Runtime|Sequence|Set|Symbol|System|Text|Tuple)(?![\\w!:?])', Name.Builtin)][('(generateMatchMethod|aliasMethod|λ|ʎ|fnx|fn|method|dmacro|dlecro|syntax|macro|dlecrox|lecrox|lecro|syntax)(?![\\w!:?])', Name.Function)][('-?0[xX][0-9a-fA-F]+', Number.Hex)][('-?(\\d+\\.?\\d*|\\d*\\.\\d+)([eE][+-]?[0-9]+)?', Number.Float)][('-?\\d+', Number.Integer)][('#\\(', Punctuation)][('(&&>>|\\|\\|>>|\\*\\*>>|:::|::|\\.\\.\\.|===|\\*\\*>|\\*\\*=|&&>|&&=|\\|\\|>|\\|\\|=|\\->>|\\+>>|!>>|<>>>|<>>|&>>|%>>|#>>|@>>|/>>|\\*>>|\\?>>|\\|>>|\\^>>|~>>|\\$>>|=>>|<<=|>>=|<=>|<\\->|=~|!~|=>|\\+\\+|\\-\\-|<=|>=|==|!=|&&|\\.\\.|\\+=|\\-=|\\*=|\\/=|%=|&=|\\^=|\\|=|<\\-|\\+>|!>|<>|&>|%>|#>|\\@>|\\/>|\\*>|\\?>|\\|>|\\^>|~>|\\$>|<\\->|\\->|<<|>>|\\*\\*|\\?\\||\\?&|\\|\\||>|<|\\*|\\/|%|\\+|\\-|&|\\^|\\||=|\\$|!|~|\\?|#|\\u2260|\\u2218|\\u2208|\\u2209)', Operator)][('(and|nand|or|xor|nor|return|import)(?![\\w!?])', Operator)],
        'squareRegexp': [][('\\n', Whitespace)][('\\s+', Whitespace)][(';(.*?)\\n', Comment)][('\\A#!(.*?)\\n', Comment)][('#/', String.Regex, 'slashRegexp')][('#r\\[', String.Regex, 'squareRegexp')][(':[\\w!:?]+', String.Symbol)][('[\\w!:?]+:(?![\\w!?])', String.Other)][(':"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Symbol)][('((?<=fn\\()|(?<=fnx\\()|(?<=method\\()|(?<=macro\\()|(?<=lecro\\()|(?<=syntax\\()|(?<=dmacro\\()|(?<=dlecro\\()|(?<=dlecrox\\()|(?<=dsyntax\\())(\\s*)"', String.Doc, 'documentation')][('"', String, 'text')][('#\\[', String, 'squareText')][('\\w[\\w!:?]+(?=\\s*=.*mimic\\s)', Name.Entity)][('[a-zA-Z_][\\w!:?]*(?=[\\s]*[+*/-]?=[^=].*($|\\.))', Name.Variable)][('(break|cond|continue|do|ensure|for|for:dict|for:set|if|let|loop|p:for|p:for:dict|p:for:set|return|unless|until|while|with)(?![\\w!:?])', Keyword.Reserved)][('(eval|mimic|print|println)(?![\\w!:?])', Keyword)][('(cell\\?|cellNames|cellOwner\\?|cellOwner|cells|cell|documentation|hash|identity|mimic|removeCell\\!|undefineCell\\!)(?![\\w!:?])', Keyword)][('(stackTraceAsText)(?![\\w!:?])', Keyword)][('(dict|list|message|set)(?![\\w!:?])', Keyword.Reserved)][('(case|case:and|case:else|case:nand|case:nor|case:not|case:or|case:otherwise|case:xor)(?![\\w!:?])', Keyword.Reserved)][('(asText|become\\!|derive|freeze\\!|frozen\\?|in\\?|is\\?|kind\\?|mimic\\!|mimics|mimics\\?|prependMimic\\!|removeAllMimics\\!|removeMimic\\!|same\\?|send|thaw\\!|uniqueHexId)(?![\\w!:?])', Keyword)][('(after|around|before)(?![\\w!:?])', Keyword.Reserved)][('(kind|cellDescriptionDict|cellSummary|genSym|inspect|notice)(?![\\w!:?])', Keyword)][('(use|destructuring)', Keyword.Reserved)][('(cell\\?|cellOwner\\?|cellOwner|cellNames|cells|cell|documentation|identity|removeCell!|undefineCell)(?![\\w!:?])', Keyword)][('(internal:compositeRegexp|internal:concatenateText|internal:createDecimal|internal:createNumber|internal:createRegexp|internal:createText)(?![\\w!:?])', Keyword.Reserved)][('(availableRestarts|bind|error\\!|findRestart|handle|invokeRestart|rescue|restart|signal\\!|warn\\!)(?![\\w!:?])', Keyword.Reserved)][('(nil|false|true)(?![\\w!:?])', Name.Constant)][('(Arity|Base|Call|Condition|DateTime|Aspects|Pointcut|Assignment|BaseBehavior|Boolean|Case|AndCombiner|Else|NAndCombiner|NOrCombiner|NotCombiner|OrCombiner|XOrCombiner|Conditions|Definitions|FlowControl|Internal|Literals|Reflection|DefaultMacro|DefaultMethod|DefaultSyntax|Dict|FileSystem|Ground|Handler|Hook|IO|IokeGround|Struct|LexicalBlock|LexicalMacro|List|Message|Method|Mixins|NativeMethod|Number|Origin|Pair|Range|Reflector|Regexp Match|Regexp|Rescue|Restart|Runtime|Sequence|Set|Symbol|System|Text|Tuple)(?![\\w!:?])', Name.Builtin)][('(generateMatchMethod|aliasMethod|λ|ʎ|fnx|fn|method|dmacro|dlecro|syntax|macro|dlecrox|lecrox|lecro|syntax)(?![\\w!:?])', Name.Function)][('-?0[xX][0-9a-fA-F]+', Number.Hex)][('-?(\\d+\\.?\\d*|\\d*\\.\\d+)([eE][+-]?[0-9]+)?', Number.Float)][('-?\\d+', Number.Integer)][('#\\(', Punctuation)][('(&&>>|\\|\\|>>|\\*\\*>>|:::|::|\\.\\.\\.|===|\\*\\*>|\\*\\*=|&&>|&&=|\\|\\|>|\\|\\|=|\\->>|\\+>>|!>>|<>>>|<>>|&>>|%>>|#>>|@>>|/>>|\\*>>|\\?>>|\\|>>|\\^>>|~>>|\\$>>|=>>|<<=|>>=|<=>|<\\->|=~|!~|=>|\\+\\+|\\-\\-|<=|>=|==|!=|&&|\\.\\.|\\+=|\\-=|\\*=|\\/=|%=|&=|\\^=|\\|=|<\\-|\\+>|!>|<>|&>|%>|#>|\\@>|\\/>|\\*>|\\?>|\\|>|\\^>|~>|\\$>|<\\->|\\->|<<|>>|\\*\\*|\\?\\||\\?&|\\|\\||>|<|\\*|\\/|%|\\+|\\-|&|\\^|\\||=|\\$|!|~|\\?|#|\\u2260|\\u2218|\\u2208|\\u2209)', Operator)][('(and|nand|or|xor|nor|return|import)(?![\\w!?])', Operator)][("(\\`\\`|\\`|\\'\\'|\\'|\\.|\\,|@@|@|\\[|\\]|\\(|\\)|\\{|\\})", Punctuation)],
        'squareText': [][('\\n', Whitespace)][('\\s+', Whitespace)][(';(.*?)\\n', Comment)][('\\A#!(.*?)\\n', Comment)][('#/', String.Regex, 'slashRegexp')][('#r\\[', String.Regex, 'squareRegexp')][(':[\\w!:?]+', String.Symbol)][('[\\w!:?]+:(?![\\w!?])', String.Other)][(':"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Symbol)][('((?<=fn\\()|(?<=fnx\\()|(?<=method\\()|(?<=macro\\()|(?<=lecro\\()|(?<=syntax\\()|(?<=dmacro\\()|(?<=dlecro\\()|(?<=dlecrox\\()|(?<=dsyntax\\())(\\s*)"', String.Doc, 'documentation')][('"', String, 'text')][('#\\[', String, 'squareText')][('\\w[\\w!:?]+(?=\\s*=.*mimic\\s)', Name.Entity)][('[a-zA-Z_][\\w!:?]*(?=[\\s]*[+*/-]?=[^=].*($|\\.))', Name.Variable)][('(break|cond|continue|do|ensure|for|for:dict|for:set|if|let|loop|p:for|p:for:dict|p:for:set|return|unless|until|while|with)(?![\\w!:?])', Keyword.Reserved)][('(eval|mimic|print|println)(?![\\w!:?])', Keyword)][('(cell\\?|cellNames|cellOwner\\?|cellOwner|cells|cell|documentation|hash|identity|mimic|removeCell\\!|undefineCell\\!)(?![\\w!:?])', Keyword)][('(stackTraceAsText)(?![\\w!:?])', Keyword)][('(dict|list|message|set)(?![\\w!:?])', Keyword.Reserved)][('(case|case:and|case:else|case:nand|case:nor|case:not|case:or|case:otherwise|case:xor)(?![\\w!:?])', Keyword.Reserved)][('(asText|become\\!|derive|freeze\\!|frozen\\?|in\\?|is\\?|kind\\?|mimic\\!|mimics|mimics\\?|prependMimic\\!|removeAllMimics\\!|removeMimic\\!|same\\?|send|thaw\\!|uniqueHexId)(?![\\w!:?])', Keyword)][('(after|around|before)(?![\\w!:?])', Keyword.Reserved)][('(kind|cellDescriptionDict|cellSummary|genSym|inspect|notice)(?![\\w!:?])', Keyword)][('(use|destructuring)', Keyword.Reserved)][('(cell\\?|cellOwner\\?|cellOwner|cellNames|cells|cell|documentation|identity|removeCell!|undefineCell)(?![\\w!:?])', Keyword)][('(internal:compositeRegexp|internal:concatenateText|internal:createDecimal|internal:createNumber|internal:createRegexp|internal:createText)(?![\\w!:?])', Keyword.Reserved)][('(availableRestarts|bind|error\\!|findRestart|handle|invokeRestart|rescue|restart|signal\\!|warn\\!)(?![\\w!:?])', Keyword.Reserved)][('(nil|false|true)(?![\\w!:?])', Name.Constant)][('(Arity|Base|Call|Condition|DateTime|Aspects|Pointcut|Assignment|BaseBehavior|Boolean|Case|AndCombiner|Else|NAndCombiner|NOrCombiner|NotCombiner|OrCombiner|XOrCombiner|Conditions|Definitions|FlowControl|Internal|Literals|Reflection|DefaultMacro|DefaultMethod|DefaultSyntax|Dict|FileSystem|Ground|Handler|Hook|IO|IokeGround|Struct|LexicalBlock|LexicalMacro|List|Message|Method|Mixins|NativeMethod|Number|Origin|Pair|Range|Reflector|Regexp Match|Regexp|Rescue|Restart|Runtime|Sequence|Set|Symbol|System|Text|Tuple)(?![\\w!:?])', Name.Builtin)][('(generateMatchMethod|aliasMethod|λ|ʎ|fnx|fn|method|dmacro|dlecro|syntax|macro|dlecrox|lecrox|lecro|syntax)(?![\\w!:?])', Name.Function)][('-?0[xX][0-9a-fA-F]+', Number.Hex)][('-?(\\d+\\.?\\d*|\\d*\\.\\d+)([eE][+-]?[0-9]+)?', Number.Float)][('-?\\d+', Number.Integer)][('#\\(', Punctuation)][('(&&>>|\\|\\|>>|\\*\\*>>|:::|::|\\.\\.\\.|===|\\*\\*>|\\*\\*=|&&>|&&=|\\|\\|>|\\|\\|=|\\->>|\\+>>|!>>|<>>>|<>>|&>>|%>>|#>>|@>>|/>>|\\*>>|\\?>>|\\|>>|\\^>>|~>>|\\$>>|=>>|<<=|>>=|<=>|<\\->|=~|!~|=>|\\+\\+|\\-\\-|<=|>=|==|!=|&&|\\.\\.|\\+=|\\-=|\\*=|\\/=|%=|&=|\\^=|\\|=|<\\-|\\+>|!>|<>|&>|%>|#>|\\@>|\\/>|\\*>|\\?>|\\|>|\\^>|~>|\\$>|<\\->|\\->|<<|>>|\\*\\*|\\?\\||\\?&|\\|\\||>|<|\\*|\\/|%|\\+|\\-|&|\\^|\\||=|\\$|!|~|\\?|#|\\u2260|\\u2218|\\u2208|\\u2209)', Operator)][('(and|nand|or|xor|nor|return|import)(?![\\w!?])', Operator)][("(\\`\\`|\\`|\\'\\'|\\'|\\.|\\,|@@|@|\\[|\\]|\\(|\\)|\\{|\\})", Punctuation)][('[A-Z][\\w!:?]*', Name.Class)],
        'root': [][('\\n', Whitespace)][('\\s+', Whitespace)][(';(.*?)\\n', Comment)][('\\A#!(.*?)\\n', Comment)][('#/', String.Regex, 'slashRegexp')][('#r\\[', String.Regex, 'squareRegexp')][(':[\\w!:?]+', String.Symbol)][('[\\w!:?]+:(?![\\w!?])', String.Other)][(':"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Symbol)][('((?<=fn\\()|(?<=fnx\\()|(?<=method\\()|(?<=macro\\()|(?<=lecro\\()|(?<=syntax\\()|(?<=dmacro\\()|(?<=dlecro\\()|(?<=dlecrox\\()|(?<=dsyntax\\())(\\s*)"', String.Doc, 'documentation')][('"', String, 'text')][('#\\[', String, 'squareText')][('\\w[\\w!:?]+(?=\\s*=.*mimic\\s)', Name.Entity)][('[a-zA-Z_][\\w!:?]*(?=[\\s]*[+*/-]?=[^=].*($|\\.))', Name.Variable)][('(break|cond|continue|do|ensure|for|for:dict|for:set|if|let|loop|p:for|p:for:dict|p:for:set|return|unless|until|while|with)(?![\\w!:?])', Keyword.Reserved)][('(eval|mimic|print|println)(?![\\w!:?])', Keyword)][('(cell\\?|cellNames|cellOwner\\?|cellOwner|cells|cell|documentation|hash|identity|mimic|removeCell\\!|undefineCell\\!)(?![\\w!:?])', Keyword)][('(stackTraceAsText)(?![\\w!:?])', Keyword)][('(dict|list|message|set)(?![\\w!:?])', Keyword.Reserved)][('(case|case:and|case:else|case:nand|case:nor|case:not|case:or|case:otherwise|case:xor)(?![\\w!:?])', Keyword.Reserved)][('(asText|become\\!|derive|freeze\\!|frozen\\?|in\\?|is\\?|kind\\?|mimic\\!|mimics|mimics\\?|prependMimic\\!|removeAllMimics\\!|removeMimic\\!|same\\?|send|thaw\\!|uniqueHexId)(?![\\w!:?])', Keyword)][('(after|around|before)(?![\\w!:?])', Keyword.Reserved)][('(kind|cellDescriptionDict|cellSummary|genSym|inspect|notice)(?![\\w!:?])', Keyword)][('(use|destructuring)', Keyword.Reserved)][('(cell\\?|cellOwner\\?|cellOwner|cellNames|cells|cell|documentation|identity|removeCell!|undefineCell)(?![\\w!:?])', Keyword)][('(internal:compositeRegexp|internal:concatenateText|internal:createDecimal|internal:createNumber|internal:createRegexp|internal:createText)(?![\\w!:?])', Keyword.Reserved)][('(availableRestarts|bind|error\\!|findRestart|handle|invokeRestart|rescue|restart|signal\\!|warn\\!)(?![\\w!:?])', Keyword.Reserved)][('(nil|false|true)(?![\\w!:?])', Name.Constant)][('(Arity|Base|Call|Condition|DateTime|Aspects|Pointcut|Assignment|BaseBehavior|Boolean|Case|AndCombiner|Else|NAndCombiner|NOrCombiner|NotCombiner|OrCombiner|XOrCombiner|Conditions|Definitions|FlowControl|Internal|Literals|Reflection|DefaultMacro|DefaultMethod|DefaultSyntax|Dict|FileSystem|Ground|Handler|Hook|IO|IokeGround|Struct|LexicalBlock|LexicalMacro|List|Message|Method|Mixins|NativeMethod|Number|Origin|Pair|Range|Reflector|Regexp Match|Regexp|Rescue|Restart|Runtime|Sequence|Set|Symbol|System|Text|Tuple)(?![\\w!:?])', Name.Builtin)][('(generateMatchMethod|aliasMethod|λ|ʎ|fnx|fn|method|dmacro|dlecro|syntax|macro|dlecrox|lecrox|lecro|syntax)(?![\\w!:?])', Name.Function)][('-?0[xX][0-9a-fA-F]+', Number.Hex)][('-?(\\d+\\.?\\d*|\\d*\\.\\d+)([eE][+-]?[0-9]+)?', Number.Float)][('-?\\d+', Number.Integer)][('#\\(', Punctuation)][('(&&>>|\\|\\|>>|\\*\\*>>|:::|::|\\.\\.\\.|===|\\*\\*>|\\*\\*=|&&>|&&=|\\|\\|>|\\|\\|=|\\->>|\\+>>|!>>|<>>>|<>>|&>>|%>>|#>>|@>>|/>>|\\*>>|\\?>>|\\|>>|\\^>>|~>>|\\$>>|=>>|<<=|>>=|<=>|<\\->|=~|!~|=>|\\+\\+|\\-\\-|<=|>=|==|!=|&&|\\.\\.|\\+=|\\-=|\\*=|\\/=|%=|&=|\\^=|\\|=|<\\-|\\+>|!>|<>|&>|%>|#>|\\@>|\\/>|\\*>|\\?>|\\|>|\\^>|~>|\\$>|<\\->|\\->|<<|>>|\\*\\*|\\?\\||\\?&|\\|\\||>|<|\\*|\\/|%|\\+|\\-|&|\\^|\\||=|\\$|!|~|\\?|#|\\u2260|\\u2218|\\u2208|\\u2209)', Operator)][('(and|nand|or|xor|nor|return|import)(?![\\w!?])', Operator)][("(\\`\\`|\\`|\\'\\'|\\'|\\.|\\,|@@|@|\\[|\\]|\\(|\\)|\\{|\\})", Punctuation)][('[A-Z][\\w!:?]*', Name.Class)][('[a-z_][\\w!:?]*', Name)] }


class ClojureLexer(RegexLexer):
    '''
    Lexer for Clojure source code.
    '''
    name = 'Clojure'
    url = 'http://clojure.org/'
    aliases = [
        'clojure',
        'clj']
    filenames = [
        '*.clj',
        '*.cljc']
    mimetypes = [
        'text/x-clojure',
        'application/x-clojure']
    version_added = '0.11'
    special_forms = ('.', 'def', 'do', 'fn', 'if', 'let', 'new', 'quote', 'var', 'loop')
    declarations = ('def-', 'defn', 'defn-', 'defmacro', 'defmulti', 'defmethod', 'defstruct', 'defonce', 'declare', 'definline', 'definterface', 'defprotocol', 'defrecord', 'deftype', 'defproject', 'ns')
    builtins = ('*', '+', '-', '->', '/', '<', '<=', '=', '==', '>', '>=', '..', 'accessor', 'agent', 'agent-errors', 'aget', 'alength', 'all-ns', 'alter', 'and', 'append-child', 'apply', 'array-map', 'aset', 'aset-boolean', 'aset-byte', 'aset-char', 'aset-double', 'aset-float', 'aset-int', 'aset-long', 'aset-short', 'assert', 'assoc', 'await', 'await-for', 'bean', 'binding', 'bit-and', 'bit-not', 'bit-or', 'bit-shift-left', 'bit-shift-right', 'bit-xor', 'boolean', 'branch?', 'butlast', 'byte', 'cast', 'char', 'children', 'class', 'clear-agent-errors', 'comment', 'commute', 'comp', 'comparator', 'complement', 'concat', 'conj', 'cons', 'constantly', 'cond', 'if-not', 'construct-proxy', 'contains?', 'count', 'create-ns', 'create-struct', 'cycle', 'dec', 'deref', 'difference', 'disj', 'dissoc', 'distinct', 'doall', 'doc', 'dorun', 'doseq', 'dosync', 'dotimes', 'doto', 'double', 'down', 'drop', 'drop-while', 'edit', 'end?', 'ensure', 'eval', 'every?', 'false?', 'ffirst', 'file-seq', 'filter', 'find', 'find-doc', 'find-ns', 'find-var', 'first', 'float', 'flush', 'for', 'fnseq', 'frest', 'gensym', 'get-proxy-class', 'get', 'hash-map', 'hash-set', 'identical?', 'identity', 'if-let', 'import', 'in-ns', 'inc', 'index', 'insert-child', 'insert-left', 'insert-right', 'inspect-table', 'inspect-tree', 'instance?', 'int', 'interleave', 'intersection', 'into', 'into-array', 'iterate', 'join', 'key', 'keys', 'keyword', 'keyword?', 'last', 'lazy-cat', 'lazy-cons', 'left', 'lefts', 'line-seq', 'list*', 'list', 'load', 'load-file', 'locking', 'long', 'loop', 'macroexpand', 'macroexpand-1', 'make-array', 'make-node', 'map', 'map-invert', 'map?', 'mapcat', 'max', 'max-key', 'memfn', 'merge', 'merge-with', 'meta', 'min', 'min-key', 'name', 'namespace', 'neg?', 'new', 'newline', 'next', 'nil?', 'node', 'not', 'not-any?', 'not-every?', 'not=', 'ns-imports', 'ns-interns', 'ns-map', 'ns-name', 'ns-publics', 'ns-refers', 'ns-resolve', 'ns-unmap', 'nth', 'nthrest', 'or', 'parse', 'partial', 'path', 'peek', 'pop', 'pos?', 'pr', 'pr-str', 'print', 'print-str', 'println', 'println-str', 'prn', 'prn-str', 'project', 'proxy', 'proxy-mappings', 'quot', 'rand', 'rand-int', 'range', 're-find', 're-groups', 're-matcher', 're-matches', 're-pattern', 're-seq', 'read', 'read-line', 'reduce', 'ref', 'ref-set', 'refer', 'rem', 'remove', 'remove-method', 'remove-ns', 'rename', 'rename-keys', 'repeat', 'replace', 'replicate', 'resolve', 'rest', 'resultset-seq', 'reverse', 'rfirst', 'right', 'rights', 'root', 'rrest', 'rseq', 'second', 'select', 'select-keys', 'send', 'send-off', 'seq', 'seq-zip', 'seq?', 'set', 'short', 'slurp', 'some', 'sort', 'sort-by', 'sorted-map', 'sorted-map-by', 'sorted-set', 'special-symbol?', 'split-at', 'split-with', 'str', 'string?', 'struct', 'struct-map', 'subs', 'subvec', 'symbol', 'symbol?', 'sync', 'take', 'take-nth', 'take-while', 'test', 'time', 'to-array', 'to-array-2d', 'tree-seq', 'true?', 'union', 'up', 'update-proxy', 'val', 'vals', 'var-get', 'var-set', 'var?', 'vector', 'vector-zip', 'vector?', 'when', 'when-first', 'when-let', 'when-not', 'with-local-vars', 'with-meta', 'with-open', 'with-out-str', 'xml-seq', 'xml-zip', 'zero?', 'zipmap', 'zipper')
    valid_name = '(?!#)[\\w!$%*+<=>?/.#|-]+'
    tokens = {
        'root': [
            (';.*$', Comment.Single),
            (',+', Text),
            ('\\s+', Whitespace),
            ('-?\\d+\\.\\d+', Number.Float),
            ('-?\\d+/\\d+', Number),
            ('-?\\d+', Number.Integer),
            ('0x-?[abcdef\\d]+', Number.Hex),
            ('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String),
            ("'" + valid_name, String.Symbol),
            ('\\\\(.|[a-z]+)', String.Char),
            ('::?#?' + valid_name, String.Symbol),
            ("~@|[`\\'#^~&@]", Operator),
            (words(special_forms, suffix = ' '), Keyword),
            (words(declarations, suffix = ' '), Keyword.Declaration),
            (words(builtins, suffix = ' '), Name.Builtin),
            ('(?<=\\()' + valid_name, Name.Function),
            (valid_name, Name.Variable),
            ('(\\[|\\])', Punctuation),
            ('(\\{|\\})', Punctuation),
            ('(\\(|\\))', Punctuation)] }


class ClojureScriptLexer(ClojureLexer):
    '''
    Lexer for ClojureScript source code.
    '''
    name = 'ClojureScript'
    url = 'http://clojure.org/clojurescript'
    aliases = [
        'clojurescript',
        'cljs']
    filenames = [
        '*.cljs']
    mimetypes = [
        'text/x-clojurescript',
        'application/x-clojurescript']
    version_added = '2.0'


class TeaLangLexer(RegexLexer):
    '''
    For Tea source code. Only used within a
    TeaTemplateLexer.

    .. versionadded:: 1.5
    '''
    flags = re.MULTILINE | re.DOTALL
    tokens = {
        'root': [
            ('^(\\s*(?:[a-zA-Z_][\\w\\.\\[\\]]*\\s+)+?)([a-zA-Z_]\\w*)(\\s*)(\\()', bygroups(using(this), Name.Function, Whitespace, Operator)),
            ('[^\\S\\n]+', Whitespace),
            ('(//.*?)(\\n)', bygroups(Comment.Single, Whitespace)),
            ('/\\*.*?\\*/', Comment.Multiline),
            ('@[a-zA-Z_][\\w\\.]*', Name.Decorator),
            ('(and|break|else|foreach|if|in|not|or|reverse)\\b', Keyword),
            ('(as|call|define)\\b', Keyword.Declaration),
            ('(true|false|null)\\b', Keyword.Constant),
            ('(template)(\\s+)', bygroups(Keyword.Declaration, Whitespace), 'template'),
            ('(import)(\\s+)', bygroups(Keyword.Namespace, Whitespace), 'import'),
            ('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            ("'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single),
            ('(\\.)([a-zA-Z_]\\w*)', bygroups(Operator, Name.Attribute)),
            ('[a-zA-Z_]\\w*:', Name.Label),
            ('[a-zA-Z_\\$]\\w*', Name),
            ('(isa|[.]{3}|[.]{2}|[=#!<>+-/%&;,.\\*\\\\\\(\\)\\[\\]\\{\\}])', Operator),
            ('[0-9][0-9]*\\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            ('0x[0-9a-fA-F]+', Number.Hex),
            ('[0-9]+L?', Number.Integer),
            ('\\n', Whitespace)],
        'template': [
            ('[a-zA-Z_]\\w*', Name.Class, '#pop')],
        'import': [
            ('[\\w.]+\\*?', Name.Namespace, '#pop')] }


class CeylonLexer(RegexLexer):
    '''
    For Ceylon source code.
    '''
    name = 'Ceylon'
    url = 'http://ceylon-lang.org/'
    aliases = [
        'ceylon']
    filenames = [
        '*.ceylon']
    mimetypes = [
        'text/x-ceylon']
    version_added = '1.6'
    flags = re.MULTILINE | re.DOTALL
    _ws = '(?:\\s|//.*?\\n|/[*].*?[*]/)+'
    tokens = {
        'root': [
            ('^(\\s*(?:[a-zA-Z_][\\w.\\[\\]]*\\s+)+?)([a-zA-Z_]\\w*)(\\s*)(\\()', bygroups(using(this), Name.Function, Whitespace, Operator)),
            ('[^\\S\\n]+', Whitespace),
            ('(//.*?)(\\n)', bygroups(Comment.Single, Whitespace)),
            ('/\\*', Comment.Multiline, 'comment'),
            ('(shared|abstract|formal|default|actual|variable|deprecated|small|late|literal|doc|by|see|throws|optional|license|tagged|final|native|annotation|sealed)\\b', Name.Decorator),
            ('(break|case|catch|continue|else|finally|for|in|if|return|switch|this|throw|try|while|is|exists|dynamic|nonempty|then|outer|assert|let)\\b', Keyword),
            ('(abstracts|extends|satisfies|super|given|of|out|assign)\\b', Keyword.Declaration),
            ('(function|value|void|new)\\b', Keyword.Type),
            ('(assembly|module|package)(\\s+)', bygroups(Keyword.Namespace, Whitespace)),
            ('(true|false|null)\\b', Keyword.Constant),
            ('(class|interface|object|alias)(\\s+)', bygroups(Keyword.Declaration, Whitespace), 'class'),
            ('(import)(\\s+)', bygroups(Keyword.Namespace, Whitespace), 'import'),
            ('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String),
            ("'\\\\.'|'[^\\\\]'|'\\\\\\{#[0-9a-fA-F]{4}\\}'", String.Char),
            ('(\\.)([a-z_]\\w*)', bygroups(Operator, Name.Attribute)),
            ('[a-zA-Z_]\\w*:', Name.Label),
            ('[a-zA-Z_]\\w*', Name),
            ('[~^*!%&\\[\\](){}<>|+=:;,./?-]', Operator),
            ('\\d{1,3}(_\\d{3})+\\.\\d{1,3}(_\\d{3})+[kMGTPmunpf]?', Number.Float),
            ('\\d{1,3}(_\\d{3})+\\.[0-9]+([eE][+-]?[0-9]+)?[kMGTPmunpf]?', Number.Float),
            ('[0-9][0-9]*\\.\\d{1,3}(_\\d{3})+[kMGTPmunpf]?', Number.Float),
            ('[0-9][0-9]*\\.[0-9]+([eE][+-]?[0-9]+)?[kMGTPmunpf]?', Number.Float),
            ('#([0-9a-fA-F]{4})(_[0-9a-fA-F]{4})+', Number.Hex),
            ('#[0-9a-fA-F]+', Number.Hex),
            ('\\$([01]{4})(_[01]{4})+', Number.Bin),
            ('\\$[01]+', Number.Bin),
            ('\\d{1,3}(_\\d{3})+[kMGTP]?', Number.Integer),
            ('[0-9]+[kMGTP]?', Number.Integer),
            ('\\n', Whitespace)],
        'class': [
            ('[A-Za-z_]\\w*', Name.Class, '#pop')],
        'import': [
            ('[a-z][\\w.]*', Name.Namespace, '#pop')],
        'comment': [
            ('[^*/]', Comment.Multiline),
            ('/\\*', Comment.Multiline, '#push'),
            ('\\*/', Comment.Multiline, '#pop'),
            ('[*/]', Comment.Multiline)] }


class KotlinLexer(RegexLexer):
    '''
    For Kotlin source code.
    '''
    name = 'Kotlin'
    url = 'http://kotlinlang.org/'
    aliases = [
        'kotlin']
    filenames = [
        '*.kt',
        '*.kts']
    mimetypes = [
        'text/x-kotlin']
    version_added = '1.5'
    flags = re.MULTILINE | re.DOTALL
    kt_name = '@?[_' + uni.combine('Lu', 'Ll', 'Lt', 'Lm', 'Nl') + ']' + '[' + uni.combine('Lu', 'Ll', 'Lt', 'Lm', 'Nl', 'Nd', 'Pc', 'Cf', 'Mn', 'Mc') + ']*'
    kt_space_name = '@?[_' + uni.combine('Lu', 'Ll', 'Lt', 'Lm', 'Nl') + ']' + '[' + uni.combine('Lu', 'Ll', 'Lt', 'Lm', 'Nl', 'Nd', 'Pc', 'Cf', 'Mn', 'Mc', 'Zs') + "\\'~!%^&*()+=|\\[\\]:;,.<>/\\?-]*"
    kt_id = '(' + kt_name + '|`' + kt_space_name + '`)'
    modifiers = 'actual|abstract|annotation|companion|const|crossinline|data|enum|expect|external|final|infix|inline|inner|internal|lateinit|noinline|open|operator|override|private|protected|public|sealed|suspend|tailrec|value'
    tokens = {
        'root': [][('[^\\S\\n]+', Whitespace)][('\\s+', Whitespace)][('\\\\$', String.Escape)][('\\n', Whitespace)][('(//.*?)(\\n)', bygroups(Comment.Single, Whitespace))][('^(#!/.+?)(\\n)', bygroups(Comment.Single, Whitespace))][('/[*].*?[*]/', Comment.Multiline)][('as\\?', Keyword)][('(as|break|by|catch|constructor|continue|do|dynamic|else|finally|get|for|if|init|[!]*in|[!]*is|out|reified|return|set|super|this|throw|try|typealias|typeof|vararg|when|where|while)\\b', Keyword)][('it\\b', Name.Builtin)][(words(('Boolean?', 'Byte?', 'Char?', 'Double?', 'Float?', 'Int?', 'Long?', 'Short?', 'String?', 'Any?', 'Unit?')), Keyword.Type)][(words(('Boolean', 'Byte', 'Char', 'Double', 'Float', 'Int', 'Long', 'Short', 'String', 'Any', 'Unit'), suffix = '\\b'), Keyword.Type)][('(true|false|null)\\b', Keyword.Constant)][('(package|import)(\\s+)(\\S+)', bygroups(Keyword, Whitespace, Name.Namespace))][('(\\?\\.)((?:[^\\W\\d]|\\$)[\\w$]*)', bygroups(Operator, Name.Attribute))][('(\\.)((?:[^\\W\\d]|\\$)[\\w$]*)', bygroups(Punctuation, Name.Attribute))][('@[^\\W\\d][\\w.]*', Name.Decorator)][('[^\\W\\d][\\w.]+@', Name.Decorator)][('(object)(\\s+)(:)(\\s+)', bygroups(Keyword, Whitespace, Punctuation, Whitespace), 'class')][('((?:(?:' + modifiers + '|fun)\\s+)*)(class|interface|object)(\\s+)', bygroups(using(this, state = 'modifiers'), Keyword.Declaration, Whitespace), 'class')][('(var|val)(\\s+)(\\()', bygroups(Keyword.Declaration, Whitespace, Punctuation), 'destructuring_assignment')][('((?:(?:' + modifiers + ')\\s+)*)(var|val)(\\s+)', bygroups(using(this, state = 'modifiers'), Keyword.Declaration, Whitespace), 'variable')][('((?:(?:' + modifiers + ')\\s+)*)(fun)(\\s+)', bygroups(using(this, state = 'modifiers'), Keyword.Declaration, Whitespace), 'function')][('::|!!|\\?[:.]', Operator)][('[~^*!%&\\[\\]<>|+=/?-]', Operator)][('[{}();:.,]', Punctuation)][('"""', String, 'multiline_string')][('"', String, 'string')][("'\\\\.'|'[^\\\\]'", String.Char)][('[0-9](\\.[0-9]*)?([eE][+-][0-9]+)?[flFL]?|0[xX][0-9a-fA-F]+[Ll]?', Number)][('' + kt_id + '((\\?[^.])?)', Name)],
        'class': [
            (kt_id, Name.Class, '#pop')],
        'variable': [
            (kt_id, Name.Variable, '#pop')],
        'destructuring_assignment': [
            (',', Punctuation),
            ('\\s+', Whitespace),
            (kt_id, Name.Variable),
            ('(:)(\\s+)(' + kt_id + ')', bygroups(Punctuation, Whitespace, Name)),
            ('<', Operator, 'generic'),
            ('\\)', Punctuation, '#pop')],
        'function': [
            ('<', Operator, 'generic'),
            ('' + kt_id + '(\\.)' + kt_id, bygroups(Name, Punctuation, Name.Function), '#pop'),
            (kt_id, Name.Function, '#pop')],
        'generic': [
            ('(>)(\\s*)', bygroups(Operator, Whitespace), '#pop'),
            (':', Punctuation),
            ('(reified|out|in)\\b', Keyword),
            (',', Punctuation),
            ('\\s+', Whitespace),
            (kt_id, Name)],
        'modifiers': [
            ('\\w+', Keyword.Declaration),
            ('\\s+', Whitespace),
            default('#pop')],
        'string': [
            ('"', String, '#pop'),
            include('string_common')],
        'multiline_string': [
            ('"""', String, '#pop'),
            ('"', String),
            include('string_common')],
        'string_common': [
            ('\\\\\\\\', String),
            ('\\\\"', String),
            ('\\\\', String),
            ('\\$\\{', String.Interpol, 'interpolation'),
            ('(\\$)(\\w+)', bygroups(String.Interpol, Name)),
            ('[^\\\\"$]+', String)],
        'interpolation': [
            ('"', String),
            ('\\$\\{', String.Interpol, 'interpolation'),
            ('\\{', Punctuation, 'scope'),
            ('\\}', String.Interpol, '#pop'),
            include('root')],
        'scope': [
            ('\\{', Punctuation, 'scope'),
            ('\\}', Punctuation, '#pop'),
            include('root')] }


class XtendLexer(RegexLexer):
    '''
    For Xtend source code.
    '''
    name = 'Xtend'
    url = 'https://www.eclipse.org/xtend/'
    aliases = [
        'xtend']
    filenames = [
        '*.xtend']
    mimetypes = [
        'text/x-xtend']
    version_added = '1.6'
    flags = re.MULTILINE | re.DOTALL
    tokens = {
        'root': [
            ('^(\\s*(?:[a-zA-Z_][\\w.\\[\\]]*\\s+)+?)([a-zA-Z_$][\\w$]*)(\\s*)(\\()', bygroups(using(this), Name.Function, Whitespace, Operator)),
            ('[^\\S\\n]+', Whitespace),
            ('(//.*?)(\\n)', bygroups(Comment.Single, Whitespace)),
            ('/\\*.*?\\*/', Comment.Multiline),
            ('@[a-zA-Z_][\\w.]*', Name.Decorator),
            ('(assert|break|case|catch|continue|default|do|else|finally|for|if|goto|instanceof|new|return|switch|this|throw|try|while|IF|ELSE|ELSEIF|ENDIF|FOR|ENDFOR|SEPARATOR|BEFORE|AFTER)\\b', Keyword),
            ('(def|abstract|const|enum|extends|final|implements|native|private|protected|public|static|strictfp|super|synchronized|throws|transient|volatile|val|var)\\b', Keyword.Declaration),
            ('(boolean|byte|char|double|float|int|long|short|void)\\b', Keyword.Type),
            ('(package)(\\s+)', bygroups(Keyword.Namespace, Whitespace)),
            ('(true|false|null)\\b', Keyword.Constant),
            ('(class|interface)(\\s+)', bygroups(Keyword.Declaration, Whitespace), 'class'),
            ('(import)(\\s+)', bygroups(Keyword.Namespace, Whitespace), 'import'),
            ("(''')", String, 'template'),
            ('(\\u00BB)', String, 'template'),
            ('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            ("'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single),
            ('[a-zA-Z_]\\w*:', Name.Label),
            ('[a-zA-Z_$]\\w*', Name),
            ('[~^*!%&\\[\\](){}<>\\|+=:;,./?-]', Operator),
            ('[0-9][0-9]*\\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            ('0x[0-9a-fA-F]+', Number.Hex),
            ('[0-9]+L?', Number.Integer),
            ('\\n', Whitespace)],
        'class': [
            ('[a-zA-Z_]\\w*', Name.Class, '#pop')],
        'import': [
            ('[\\w.]+\\*?', Name.Namespace, '#pop')],
        'template': [
            ("'''", String, '#pop'),
            ('\\u00AB', String, '#pop'),
            ('.', String)] }


class PigLexer(RegexLexer):
    '''
    For Pig Latin source code.
    '''
    name = 'Pig'
    url = 'https://pig.apache.org/'
    aliases = [
        'pig']
    filenames = [
        '*.pig']
    mimetypes = [
        'text/x-pig']
    version_added = '2.0'
    flags = re.MULTILINE | re.IGNORECASE
    tokens = {
        'root': [
            ('\\s+', Whitespace),
            ('--.*', Comment),
            ('/\\*[\\w\\W]*?\\*/', Comment.Multiline),
            ('\\\\$', String.Escape),
            ('\\\\', Text),
            ("\\'(?:\\\\[ntbrf\\\\\\']|\\\\u[0-9a-f]{4}|[^\\'\\\\\\n\\r])*\\'", String),
            include('keywords'),
            include('types'),
            include('builtins'),
            include('punct'),
            include('operators'),
            ('[0-9]*\\.[0-9]+(e[0-9]+)?[fd]?', Number.Float),
            ('0x[0-9a-f]+', Number.Hex),
            ('[0-9]+L?', Number.Integer),
            ('\\n', Whitespace),
            ('([a-z_]\\w*)(\\s*)(\\()', bygroups(Name.Function, Whitespace, Punctuation)),
            ('[()#:]', Text),
            ('[^(:#\\\'")\\s]+', Text),
            ('\\S+\\s+', Text)],
        'keywords': [
            ('(assert|and|any|all|arrange|as|asc|bag|by|cache|CASE|cat|cd|cp|%declare|%default|define|dense|desc|describe|distinct|du|dump|eval|exex|explain|filter|flatten|foreach|full|generate|group|help|if|illustrate|import|inner|input|into|is|join|kill|left|limit|load|ls|map|matches|mkdir|mv|not|null|onschema|or|order|outer|output|parallel|pig|pwd|quit|register|returns|right|rm|rmf|rollup|run|sample|set|ship|split|stderr|stdin|stdout|store|stream|through|union|using|void)\\b', Keyword)],
        'builtins': [
            ('(AVG|BinStorage|cogroup|CONCAT|copyFromLocal|copyToLocal|COUNT|cross|DIFF|MAX|MIN|PigDump|PigStorage|SIZE|SUM|TextLoader|TOKENIZE)\\b', Name.Builtin)],
        'types': [
            ('(bytearray|BIGINTEGER|BIGDECIMAL|chararray|datetime|double|float|int|long|tuple)\\b', Keyword.Type)],
        'punct': [
            ('[;(){}\\[\\]]', Punctuation)],
        'operators': [
            ('[#=,./%+\\-?]', Operator),
            ('(eq|gt|lt|gte|lte|neq|matches)\\b', Operator),
            ('(==|<=|<|>=|>|!=)', Operator)] }


class GoloLexer(RegexLexer):
    '''
    For Golo source code.
    '''
    name = 'Golo'
    url = 'http://golo-lang.org/'
    filenames = [
        '*.golo']
    aliases = [
        'golo']
    version_added = '2.0'
    tokens = {
        'root': [
            ('[^\\S\\n]+', Whitespace),
            ('#.*$', Comment),
            ('(\\^|\\.\\.\\.|:|\\?:|->|==|!=|=|\\+|\\*|%|/|<=|<|>=|>|=|\\.)', Operator),
            ('(?<=[^-])(-)(?=[^-])', Operator),
            ('(?<=[^`])(is|isnt|and|or|not|oftype|in|orIfNull)\\b', Operator.Word),
            ('[]{}|(),[]', Punctuation),
            ('(module|import)(\\s+)', bygroups(Keyword.Namespace, Whitespace), 'modname'),
            ('\\b([a-zA-Z_][\\w$.]*)(::)', bygroups(Name.Namespace, Punctuation)),
            ('\\b([a-zA-Z_][\\w$]*(?:\\.[a-zA-Z_][\\w$]*)+)\\b', Name.Namespace),
            ('(let|var)(\\s+)', bygroups(Keyword.Declaration, Whitespace), 'varname'),
            ('(struct)(\\s+)', bygroups(Keyword.Declaration, Whitespace), 'structname'),
            ('(function)(\\s+)', bygroups(Keyword.Declaration, Whitespace), 'funcname'),
            ('(null|true|false)\\b', Keyword.Constant),
            ('(augment|pimp|if|else|case|match|return|case|when|then|otherwise|while|for|foreach|try|catch|finally|throw|local|continue|break)\\b', Keyword),
            ('(map|array|list|set|vector|tuple)(\\[)', bygroups(Name.Builtin, Punctuation)),
            ('(print|println|readln|raise|fun|asInterfaceInstance)\\b', Name.Builtin),
            ('(`?[a-zA-Z_][\\w$]*)(\\()', bygroups(Name.Function, Punctuation)),
            ('-?[\\d_]*\\.[\\d_]*([eE][+-]?\\d[\\d_]*)?F?', Number.Float),
            ('0[0-7]+j?', Number.Oct),
            ('0[xX][a-fA-F0-9]+', Number.Hex),
            ('-?\\d[\\d_]*L', Number.Integer.Long),
            ('-?\\d[\\d_]*', Number.Integer),
            ('`?[a-zA-Z_][\\w$]*', Name),
            ('@[a-zA-Z_][\\w$.]*', Name.Decorator),
            ('"""', String, combined('stringescape', 'triplestring')),
            ('"', String, combined('stringescape', 'doublestring')),
            ("'", String, combined('stringescape', 'singlestring')),
            ('----((.|\\n)*?)----', String.Doc)],
        'funcname': [
            ('`?[a-zA-Z_][\\w$]*', Name.Function, '#pop')],
        'modname': [
            ('[a-zA-Z_][\\w$.]*\\*?', Name.Namespace, '#pop')],
        'structname': [
            ('`?[\\w.]+\\*?', Name.Class, '#pop')],
        'varname': [
            ('`?[a-zA-Z_][\\w$]*', Name.Variable, '#pop')],
        'string': [
            ('[^\\\\\\\'"\\n]+', String),
            ('[\\\'"\\\\]', String)],
        'stringescape': [
            ('\\\\([\\\\abfnrtv"\\\']|\\n|N\\{.*?\\}|u[a-fA-F0-9]{4}|U[a-fA-F0-9]{8}|x[a-fA-F0-9]{2}|[0-7]{1,3})', String.Escape)],
        'triplestring': [
            ('"""', String, '#pop'),
            include('string'),
            ('\\n', String)],
        'doublestring': [
            ('"', String.Double, '#pop'),
            include('string')],
        'singlestring': [
            ("'", String, '#pop'),
            include('string')],
        'operators': [
            ('[#=,./%+\\-?]', Operator),
            ('(eq|gt|lt|gte|lte|neq|matches)\\b', Operator),
            ('(==|<=|<|>=|>|!=)', Operator)] }


class JasminLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'JasminLexer'
    __doc__ = '\n    For Jasmin assembly code.\n    '
    name = 'Jasmin'
    url = 'http://jasmin.sourceforge.net/'
    aliases = [
        'jasmin',
        'jasminxt']
    filenames = [
        '*.j']
    version_added = '2.0'
    _whitespace = ' \\n\\t\\r'
    _ws = f'''(?:[{_whitespace}]+)'''
    _separator = f'''{_whitespace}:='''
    _break = f'''(?=[{_separator}]|$)'''
    _name = f'''[^{_separator}]+'''
    _unqualified_name = f'''(?:[^{_separator}.;\\[/]+)'''
# WARNING: Decompyle incomplete


class SarlLexer(RegexLexer):
    '''
    For SARL source code.
    '''
    name = 'SARL'
    url = 'http://www.sarl.io'
    aliases = [
        'sarl']
    filenames = [
        '*.sarl']
    mimetypes = [
        'text/x-sarl']
    version_added = '2.4'
    flags = re.MULTILINE | re.DOTALL
    tokens = {
        'root': [
            ('^(\\s*(?:[a-zA-Z_][\\w.\\[\\]]*\\s+)+?)([a-zA-Z_$][\\w$]*)(\\s*)(\\()', bygroups(using(this), Name.Function, Whitespace, Operator)),
            ('[^\\S\\n]+', Whitespace),
            ('(//.*?)(\\n)', bygroups(Comment.Single, Whitespace)),
            ('/\\*.*?\\*/', Comment.Multiline),
            ('@[a-zA-Z_][\\w.]*', Name.Decorator),
            ('(as|break|case|catch|default|do|else|extends|extension|finally|fires|for|if|implements|instanceof|new|on|requires|return|super|switch|throw|throws|try|typeof|uses|while|with)\\b', Keyword),
            ('(abstract|def|dispatch|final|native|override|private|protected|public|static|strictfp|synchronized|transient|val|var|volatile)\\b', Keyword.Declaration),
            ('(boolean|byte|char|double|float|int|long|short|void)\\b', Keyword.Type),
            ('(package)(\\s+)', bygroups(Keyword.Namespace, Whitespace)),
            ('(false|it|null|occurrence|this|true|void)\\b', Keyword.Constant),
            ('(agent|annotation|artifact|behavior|capacity|class|enum|event|interface|skill|space)(\\s+)', bygroups(Keyword.Declaration, Whitespace), 'class'),
            ('(import)(\\s+)', bygroups(Keyword.Namespace, Whitespace), 'import'),
            ('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            ("'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single),
            ('[a-zA-Z_]\\w*:', Name.Label),
            ('[a-zA-Z_$]\\w*', Name),
            ('[~^*!%&\\[\\](){}<>\\|+=:;,./?-]', Operator),
            ('[0-9][0-9]*\\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            ('0x[0-9a-fA-F]+', Number.Hex),
            ('[0-9]+L?', Number.Integer),
            ('\\n', Whitespace)],
        'class': [
            ('[a-zA-Z_]\\w*', Name.Class, '#pop')],
        'import': [
            ('[\\w.]+\\*?', Name.Namespace, '#pop')] }
