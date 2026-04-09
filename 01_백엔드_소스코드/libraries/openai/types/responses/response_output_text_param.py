# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_output_text_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict
__all__ = [
    'ResponseOutputTextParam',
    'Annotation',
    'AnnotationFileCitation',
    'AnnotationURLCitation',
    'AnnotationContainerFileCitation',
    'AnnotationFilePath',
    'Logprob',
    'LogprobTopLogprob']

def AnnotationFileCitation():
    '''AnnotationFileCitation'''
    type: "Required[Literal['file_citation']]" = 'A citation to a file.'

AnnotationFileCitation = <NODE:27>(AnnotationFileCitation, 'AnnotationFileCitation', TypedDict, total = False)

def AnnotationURLCitation():
    '''AnnotationURLCitation'''
    url: 'Required[str]' = 'A citation for a web resource used to generate a model response.'

AnnotationURLCitation = <NODE:27>(AnnotationURLCitation, 'AnnotationURLCitation', TypedDict, total = False)

def AnnotationContainerFileCitation():
    '''AnnotationContainerFileCitation'''
    type: "Required[Literal['container_file_citation']]" = 'A citation for a container file used to generate a model response.'

AnnotationContainerFileCitation = <NODE:27>(AnnotationContainerFileCitation, 'AnnotationContainerFileCitation', TypedDict, total = False)

def AnnotationFilePath():
    '''AnnotationFilePath'''
    type: "Required[Literal['file_path']]" = 'A path to a file.'

AnnotationFilePath = <NODE:27>(AnnotationFilePath, 'AnnotationFilePath', TypedDict, total = False)
Annotation: 'TypeAlias' = Union[(AnnotationFileCitation, AnnotationURLCitation, AnnotationContainerFileCitation, AnnotationFilePath)]

def LogprobTopLogprob():
    '''LogprobTopLogprob'''
    logprob: 'Required[float]' = 'The top log probability of a token.'

LogprobTopLogprob = <NODE:27>(LogprobTopLogprob, 'LogprobTopLogprob', TypedDict, total = False)

def Logprob():
    '''Logprob'''
    top_logprobs: 'Required[Iterable[LogprobTopLogprob]]' = 'The log probability of a token.'

Logprob = <NODE:27>(Logprob, 'Logprob', TypedDict, total = False)

def ResponseOutputTextParam():
    '''ResponseOutputTextParam'''
    logprobs: 'Iterable[Logprob]' = 'A text output from the model.'

ResponseOutputTextParam = <NODE:27>(ResponseOutputTextParam, 'ResponseOutputTextParam', TypedDict, total = False)
