# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: eval_retrieve_response.pyc (Python 3.11)

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from pydantic import Field as FieldInfo
from _utils import PropertyInfo
from _models import BaseModel
from shared.metadata import Metadata
from graders.python_grader import PythonGrader
from graders.label_model_grader import LabelModelGrader
from graders.score_model_grader import ScoreModelGrader
from graders.string_check_grader import StringCheckGrader
from eval_custom_data_source_config import EvalCustomDataSourceConfig
from graders.text_similarity_grader import TextSimilarityGrader
from eval_stored_completions_data_source_config import EvalStoredCompletionsDataSourceConfig
__all__ = [
    'EvalRetrieveResponse',
    'DataSourceConfig',
    'DataSourceConfigLogs',
    'TestingCriterion',
    'TestingCriterionEvalGraderTextSimilarity',
    'TestingCriterionEvalGraderPython',
    'TestingCriterionEvalGraderScoreModel']

class DataSourceConfigLogs(BaseModel):
    '''
    A LogsDataSourceConfig which specifies the metadata property of your logs query.
    This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
    The schema returned by this data source config is used to defined what variables are available in your evals.
    `item` and `sample` are both defined when using this data source config.
    '''
    type: Literal['logs'] = FieldInfo(alias = 'schema')
    metadata: Optional[Metadata] = None

DataSourceConfig: TypeAlias = Annotated[(Union[(EvalCustomDataSourceConfig, DataSourceConfigLogs, EvalStoredCompletionsDataSourceConfig)], PropertyInfo(discriminator = 'type'))]

class TestingCriterionEvalGraderTextSimilarity(TextSimilarityGrader):
    pass_threshold: float = False


class TestingCriterionEvalGraderPython(PythonGrader):
    __test__ = False
    pass_threshold: Optional[float] = None


class TestingCriterionEvalGraderScoreModel(ScoreModelGrader):
    __test__ = False
    pass_threshold: Optional[float] = None

TestingCriterion: TypeAlias = Union[(LabelModelGrader, StringCheckGrader, TestingCriterionEvalGraderTextSimilarity, TestingCriterionEvalGraderPython, TestingCriterionEvalGraderScoreModel)]

class EvalRetrieveResponse(BaseModel):
    data_source_config: DataSourceConfig = '\n    An Eval object with a data source config and testing criteria.\n    An Eval represents a task to be done for your LLM integration.\n    Like:\n     - Improve the quality of my chatbot\n     - See how well my chatbot handles customer support\n     - Check if o4-mini is better at my usecase than gpt-4o\n    '
    testing_criteria: List[TestingCriterion] = None
