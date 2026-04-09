# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool.pyc (Python 3.11)

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from  import web_search_tool
from _utils import PropertyInfo
from _models import BaseModel
from custom_tool import CustomTool
from computer_tool import ComputerTool
from function_tool import FunctionTool
from web_search_tool import WebSearchTool
from apply_patch_tool import ApplyPatchTool
from file_search_tool import FileSearchTool
from function_shell_tool import FunctionShellTool
from web_search_preview_tool import WebSearchPreviewTool
__all__ = [
    'Tool',
    'WebSearchTool',
    'Mcp',
    'McpAllowedTools',
    'McpAllowedToolsMcpToolFilter',
    'McpRequireApproval',
    'McpRequireApprovalMcpToolApprovalFilter',
    'McpRequireApprovalMcpToolApprovalFilterAlways',
    'McpRequireApprovalMcpToolApprovalFilterNever',
    'CodeInterpreter',
    'CodeInterpreterContainer',
    'CodeInterpreterContainerCodeInterpreterToolAuto',
    'ImageGeneration',
    'ImageGenerationInputImageMask',
    'LocalShell']
WebSearchToolFilters = web_search_tool.Filters
WebSearchToolUserLocation = web_search_tool.UserLocation

class McpAllowedToolsMcpToolFilter(BaseModel):
    '''A filter object to specify which tools are allowed.'''
    read_only: Optional[bool] = None
    tool_names: Optional[List[str]] = None

McpAllowedTools: TypeAlias = Union[(List[str], McpAllowedToolsMcpToolFilter, None)]

class McpRequireApprovalMcpToolApprovalFilterAlways(BaseModel):
    '''A filter object to specify which tools are allowed.'''
    read_only: Optional[bool] = None
    tool_names: Optional[List[str]] = None


class McpRequireApprovalMcpToolApprovalFilterNever(BaseModel):
    '''A filter object to specify which tools are allowed.'''
    read_only: Optional[bool] = None
    tool_names: Optional[List[str]] = None


class McpRequireApprovalMcpToolApprovalFilter(BaseModel):
    """Specify which of the MCP server's tools require approval.

    Can be
    `always`, `never`, or a filter object associated with tools
    that require approval.
    """
    always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways] = None
    never: Optional[McpRequireApprovalMcpToolApprovalFilterNever] = None

McpRequireApproval: TypeAlias = Union[(McpRequireApprovalMcpToolApprovalFilter, Literal[('always', 'never')], None)]

class Mcp(BaseModel):
    type: Literal['mcp'] = '\n    Give the model access to additional tools via remote Model Context Protocol\n    (MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).\n    '
    allowed_tools: Optional[McpAllowedTools] = None
    authorization: Optional[str] = None
    connector_id: Optional[Literal[('connector_dropbox', 'connector_gmail', 'connector_googlecalendar', 'connector_googledrive', 'connector_microsoftteams', 'connector_outlookcalendar', 'connector_outlookemail', 'connector_sharepoint')]] = None
    headers: Optional[Dict[(str, str)]] = None
    require_approval: Optional[McpRequireApproval] = None
    server_description: Optional[str] = None
    server_url: Optional[str] = None


class CodeInterpreterContainerCodeInterpreterToolAuto(BaseModel):
    type: Literal['auto'] = 'Configuration for a code interpreter container.\n\n    Optionally specify the IDs of the files to run the code on.\n    '
    file_ids: Optional[List[str]] = None
    memory_limit: Optional[Literal[('1g', '4g', '16g', '64g')]] = None

CodeInterpreterContainer: TypeAlias = Union[(str, CodeInterpreterContainerCodeInterpreterToolAuto)]

class CodeInterpreter(BaseModel):
    type: Literal['code_interpreter'] = 'A tool that runs Python code to help generate a response to a prompt.'


class ImageGenerationInputImageMask(BaseModel):
    '''Optional mask for inpainting.

    Contains `image_url`
    (string, optional) and `file_id` (string, optional).
    '''
    file_id: Optional[str] = None
    image_url: Optional[str] = None


class ImageGeneration(BaseModel):
    type: Literal['image_generation'] = 'A tool that generates images using the GPT image models.'
    background: Optional[Literal[('transparent', 'opaque', 'auto')]] = None
    input_fidelity: Optional[Literal[('high', 'low')]] = None
    input_image_mask: Optional[ImageGenerationInputImageMask] = None
    model: Union[(str, Literal[('gpt-image-1', 'gpt-image-1-mini')], None)] = None
    moderation: Optional[Literal[('auto', 'low')]] = None
    output_compression: Optional[int] = None
    output_format: Optional[Literal[('png', 'webp', 'jpeg')]] = None
    partial_images: Optional[int] = None
    quality: Optional[Literal[('low', 'medium', 'high', 'auto')]] = None
    size: Optional[Literal[('1024x1024', '1024x1536', '1536x1024', 'auto')]] = None


class LocalShell(BaseModel):
    type: Literal['local_shell'] = 'A tool that allows the model to execute shell commands in a local environment.'

Tool: TypeAlias = Annotated[(Union[(FunctionTool, FileSearchTool, ComputerTool, WebSearchTool, Mcp, CodeInterpreter, ImageGeneration, LocalShell, FunctionShellTool, CustomTool, WebSearchPreviewTool, ApplyPatchTool)], PropertyInfo(discriminator = 'type'))]
