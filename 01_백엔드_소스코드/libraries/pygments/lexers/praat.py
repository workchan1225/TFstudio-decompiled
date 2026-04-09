# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: praat.pyc (Python 3.11)

'''
    pygments.lexers.praat
    ~~~~~~~~~~~~~~~~~~~~~

    Lexer for Praat

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer, words, bygroups, include
from pygments.token import Name, Text, Comment, Keyword, String, Punctuation, Number, Operator, Whitespace
__all__ = [
    'PraatLexer']

class PraatLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'PraatLexer'
    __doc__ = '\n    For Praat scripts.\n    '
    name = 'Praat'
    url = 'http://www.praat.org'
    aliases = [
        'praat']
    filenames = [
        '*.praat',
        '*.proc',
        '*.psc']
    version_added = '2.1'
    keywords = ('if', 'then', 'else', 'elsif', 'elif', 'endif', 'fi', 'for', 'from', 'to', 'endfor', 'endproc', 'while', 'endwhile', 'repeat', 'until', 'select', 'plus', 'minus', 'demo', 'assert', 'stopwatch', 'nocheck', 'nowarn', 'noprogress', 'editor', 'endeditor', 'clearinfo')
    functions_string = ('backslashTrigraphsToUnicode', 'chooseDirectory', 'chooseReadFile', 'chooseWriteFile', 'date', 'demoKey', 'do', 'environment', 'extractLine', 'extractWord', 'fixed', 'info', 'left', 'mid', 'percent', 'readFile', 'replace', 'replace_regex', 'right', 'selected', 'string', 'unicodeToBackslashTrigraphs')
    functions_numeric = ('abs', 'appendFile', 'appendFileLine', 'appendInfo', 'appendInfoLine', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'barkToHertz', 'beginPause', 'beginSendPraat', 'besselI', 'besselK', 'beta', 'beta2', 'binomialP', 'binomialQ', 'boolean', 'ceiling', 'chiSquareP', 'chiSquareQ', 'choice', 'comment', 'cos', 'cosh', 'createDirectory', 'deleteFile', 'demoClicked', 'demoClickedIn', 'demoCommandKeyPressed', 'demoExtraControlKeyPressed', 'demoInput', 'demoKeyPressed', 'demoOptionKeyPressed', 'demoShiftKeyPressed', 'demoShow', 'demoWaitForInput', 'demoWindowTitle', 'demoX', 'demoY', 'differenceLimensToPhon', 'do', 'editor', 'endPause', 'endSendPraat', 'endsWith', 'erb', 'erbToHertz', 'erf', 'erfc', 'exitScript', 'exp', 'extractNumber', 'fileReadable', 'fisherP', 'fisherQ', 'floor', 'gaussP', 'gaussQ', 'hertzToBark', 'hertzToErb', 'hertzToMel', 'hertzToSemitones', 'imax', 'imin', 'incompleteBeta', 'incompleteGammaP', 'index', 'index_regex', 'integer', 'invBinomialP', 'invBinomialQ', 'invChiSquareQ', 'invFisherQ', 'invGaussQ', 'invSigmoid', 'invStudentQ', 'length', 'ln', 'lnBeta', 'lnGamma', 'log10', 'log2', 'max', 'melToHertz', 'min', 'minusObject', 'natural', 'number', 'numberOfColumns', 'numberOfRows', 'numberOfSelected', 'objectsAreIdentical', 'option', 'optionMenu', 'pauseScript', 'phonToDifferenceLimens', 'plusObject', 'positive', 'randomBinomial', 'randomGauss', 'randomInteger', 'randomPoisson', 'randomUniform', 'real', 'readFile', 'removeObject', 'rindex', 'rindex_regex', 'round', 'runScript', 'runSystem', 'runSystem_nocheck', 'selectObject', 'selected', 'semitonesToHertz', 'sentence', 'sentencetext', 'sigmoid', 'sin', 'sinc', 'sincpi', 'sinh', 'soundPressureToPhon', 'sqrt', 'startsWith', 'studentP', 'studentQ', 'tan', 'tanh', 'text', 'variableExists', 'word', 'writeFile', 'writeFileLine', 'writeInfo', 'writeInfoLine')
    functions_array = ('linear', 'randomGauss', 'randomInteger', 'randomUniform', 'zero')
    objects = ('Activation', 'AffineTransform', 'AmplitudeTier', 'Art', 'Artword', 'Autosegment', 'BarkFilter', 'BarkSpectrogram', 'CCA', 'Categories', 'Cepstrogram', 'Cepstrum', 'Cepstrumc', 'ChebyshevSeries', 'ClassificationTable', 'Cochleagram', 'Collection', 'ComplexSpectrogram', 'Configuration', 'Confusion', 'ContingencyTable', 'Corpus', 'Correlation', 'Covariance', 'CrossCorrelationTable', 'CrossCorrelationTables', 'DTW', 'DataModeler', 'Diagonalizer', 'Discriminant', 'Dissimilarity', 'Distance', 'Distributions', 'DurationTier', 'EEG', 'ERP', 'ERPTier', 'EditCostsTable', 'EditDistanceTable', 'Eigen', 'Excitation', 'Excitations', 'ExperimentMFC', 'FFNet', 'FeatureWeights', 'FileInMemory', 'FilesInMemory', 'Formant', 'FormantFilter', 'FormantGrid', 'FormantModeler', 'FormantPoint', 'FormantTier', 'GaussianMixture', 'HMM', 'HMM_Observation', 'HMM_ObservationSequence', 'HMM_State', 'HMM_StateSequence', 'Harmonicity', 'ISpline', 'Index', 'Intensity', 'IntensityTier', 'IntervalTier', 'KNN', 'KlattGrid', 'KlattTable', 'LFCC', 'LPC', 'Label', 'LegendreSeries', 'LinearRegression', 'LogisticRegression', 'LongSound', 'Ltas', 'MFCC', 'MSpline', 'ManPages', 'Manipulation', 'Matrix', 'MelFilter', 'MelSpectrogram', 'MixingMatrix', 'Movie', 'Network', 'Object', 'OTGrammar', 'OTHistory', 'OTMulti', 'PCA', 'PairDistribution', 'ParamCurve', 'Pattern', 'Permutation', 'Photo', 'Pitch', 'PitchModeler', 'PitchTier', 'PointProcess', 'Polygon', 'Polynomial', 'PowerCepstrogram', 'PowerCepstrum', 'Procrustes', 'RealPoint', 'RealTier', 'ResultsMFC', 'Roots', 'SPINET', 'SSCP', 'SVD', 'Salience', 'ScalarProduct', 'Similarity', 'SimpleString', 'SortedSetOfString', 'Sound', 'Speaker', 'Spectrogram', 'Spectrum', 'SpectrumTier', 'SpeechSynthesizer', 'SpellingChecker', 'Strings', 'StringsIndex', 'Table', 'TableOfReal', 'TextGrid', 'TextInterval', 'TextPoint', 'TextTier', 'Tier', 'Transition', 'VocalTract', 'VocalTractTier', 'Weight', 'WordList')
    variables_numeric = ('macintosh', 'windows', 'unix', 'praatVersion', 'pi', 'e', 'undefined')
    variables_string = ('praatVersion', 'tab', 'shellDirectory', 'homeDirectory', 'preferencesDirectory', 'newline', 'temporaryDirectory', 'defaultDirectory')
    object_attributes = ('ncol', 'nrow', 'xmin', 'ymin', 'xmax', 'ymax', 'nx', 'ny', 'dx', 'dy')
# WARNING: Decompyle incomplete
