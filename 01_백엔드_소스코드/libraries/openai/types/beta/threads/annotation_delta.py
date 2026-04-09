# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: annotation_delta.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from file_path_delta_annotation import FilePathDeltaAnnotation
from file_citation_delta_annotation import FileCitationDeltaAnnotation
__all__ = [
    'AnnotationDelta']
AnnotationDelta: TypeAlias = Annotated[(Union[(FileCitationDeltaAnnotation, FilePathDeltaAnnotation)], PropertyInfo(discriminator = 'type'))]
