# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

"""Google AI Python SDK

## Setup

```posix-terminal
pip install google-generativeai
```

## GenerativeModel

Use `genai.GenerativeModel` to access the API:

```
import google.generativeai as genai
import os

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel(model_name='gemini-1.5-flash')
response = model.generate_content('Teach me about how an LLM works')

print(response.text)
```

See the [python quickstart](https://ai.google.dev/tutorials/python_quickstart) for more details.
"""
from __future__ import annotations
import warnings
import textwrap
from google.generativeai import version
from google.generativeai import caching
from google.generativeai import protos
from google.generativeai import types
from google.generativeai.client import configure
from google.generativeai.embedding import embed_content
from google.generativeai.embedding import embed_content_async
from google.generativeai.files import upload_file
from google.generativeai.files import get_file
from google.generativeai.files import list_files
from google.generativeai.files import delete_file
from google.generativeai.generative_models import GenerativeModel
from google.generativeai.generative_models import ChatSession
from google.generativeai.models import list_models
from google.generativeai.models import list_tuned_models
from google.generativeai.models import get_model
from google.generativeai.models import get_base_model
from google.generativeai.models import get_tuned_model
from google.generativeai.models import create_tuned_model
from google.generativeai.models import update_tuned_model
from google.generativeai.models import delete_tuned_model
from google.generativeai.operations import list_operations
from google.generativeai.operations import get_operation
from google.generativeai.types import GenerationConfig
__version__ = version.__version__
warnings.warn(textwrap.dedent('\n\n        All support for the `google.generativeai` package has ended. It will no longer be receiving \n        updates or bug fixes. Please switch to the `google.genai` package as soon as possible.\n        See README for more details:\n\n        https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md\n        '), FutureWarning, stacklevel = 2)
del embedding
del files
del generative_models
del models
del client
del operations
del version
