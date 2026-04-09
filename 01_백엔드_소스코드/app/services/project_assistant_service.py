# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: project_assistant_service.pyc (Python 3.11)

import ast
import json
import logging
import re
from typing import Any
from app.models.project import Project
from app.models.settings import Settings
from app.services.ai import get_ai_service
from app.services.assistant import AssistantContextService, AssistantKnowledgeService, resolve_assistant_scope
from app.services.assistant.context import SUPPORTED_ASSISTANT_SCOPES, sanitize_route_context
from app.services.google_auth_service import is_google_ai_configured
logger = logging.getLogger(__name__)

class ProjectAssistantService:
    '''Global read-only assistant with route-aware context and knowledge retrieval.'''
    SUPPORTED_SCOPES = SUPPORTED_ASSISTANT_SCOPES
    _MESSAGE_ROLE_ALLOWLIST = {
        'user',
        'assistant'}
    _MAX_MESSAGE_CONTENT_CHARS = 2500
    _MAX_HISTORY_MESSAGES = 10
    _MAX_CONTEXT_JSON_CHARS = 5000
    _MAX_KNOWLEDGE_ITEMS = 4
    chat = (lambda cls = None, *, project_id: sanitized_messages = cls._sanitize_messages(messages)if not sanitized_messages:
raise ValueError('At least one user message is required')merged_route_context = cls._merge_route_contexts(route_context, page_context, project_id)normalized_scope = resolve_assistant_scope(scope, merged_route_context.get('pathname'))if not project_id:
resolved_project_id = merged_route_context.get('projectId')project = Noneif resolved_project_id:
project = Project.query.get(resolved_project_id)if not project:
raise LookupError('Project not found')settings = Settings.get_or_create()context = AssistantContextService.build(scope = normalized_scope, route_context = merged_route_context, project = project, settings = settings)if project_context and isinstance(project_context, dict):
'uiProjectContext'({
(lambda .0: pass# WARNING: Decompyle incomplete
): project_context.items()() })
        context_summary = AssistantContextService.build_context_summary(normalized_scope, context)
        suggested_prompts = AssistantContextService.build_suggested_prompts(normalized_scope, context)
        latest_user_message = sanitized_messages[-1]['content']
        knowledge_hits = AssistantKnowledgeService.search(query = latest_user_message, scope = normalized_scope, route_context = merged_route_context, project_context = context, limit = cls._MAX_KNOWLEDGE_ITEMS)
        if project:
            pass
        elif merged_route_context.get('pageTitle') or project:
            pass
        
        sources = project.title(knowledge_hits = merged_route_context.get('pageTitle'), include_runtime = '현재 상태', runtime_title = '현재 열려 있는 화면과 실제 상태를 함께 반영했습니다.', runtime_reason = '현재 화면 기준 안내입니다.')
    # WARNING: Decompyle incomplete
)()
    build_system_prompt = (lambda cls = None, scope = None: f'''You are TFstudio\'s read-only assistant.\nRespond in Korean unless the user explicitly asks for another language.\nYou are helping with scope: {scope}.\nYou must never claim that you executed, saved, regenerated, synced, updated, or deleted anything.\nYou do not have permission to trigger actions. If the user asks you to change the project, clearly say this assistant is read-only and explain the manual next step.\nBase your answer only on the provided runtime context, curated knowledge notes, and conversation.\nPrioritize practical next actions and correction direction over passive description.\nAlways explain what to do next, in order.\nDo not use markdown, bold, asterisks, tables, or code fences.\nReturn only a valid JSON object with this exact shape:\n{{"summary":"...","nextSteps":["..."],"correctionDirections":["..."]}}\n''')()
    _sanitize_messages = (lambda cls = None, messages = None: if not isinstance(messages, list):
[]sanitized = Nonefor item in messages[-(cls._MAX_HISTORY_MESSAGES):]:
if not isinstance(item, dict):
continueif not item.get('role'):
role = str('').strip().lower()if not item.get('content'):
content = str('').strip()if not role not in cls._MESSAGE_ROLE_ALLOWLIST or content:
continuesanitized.append({
'role': role,
'content': cls._truncate_text(content, cls._MAX_MESSAGE_CONTENT_CHARS) })if sanitized or sanitized[-1]['role'] != 'user':
[]None)()
    _merge_route_contexts = (lambda route_context = None, page_context = None, project_id = staticmethod: merged = { }if isinstance(route_context, dict):
merged.update(route_context)if isinstance(page_context, dict):
merged.update(page_context)if not project_id and merged.get('projectId'):
merged['projectId'] = project_idsanitize_route_context(merged))()
    _build_prompt = (lambda cls = None, *, scope: compact_context = cls._truncate_text(json.dumps(context, ensure_ascii = False, indent = 2), cls._MAX_CONTEXT_JSON_CHARS)compact_summary = json.dumps(context_summary, ensure_ascii = False, indent = 2)compact_knowledge = (lambda .0: [ {
'title': item.get('title'),
'category': item.get('category'),
'summary': item.get('summary'),
'details': item.get('details', [])[:2] } for item in .0 ])(knowledge_hits(), ensure_ascii = False, indent = 2)
        conversation_text = (lambda .0: pass# WARNING: Decompyle incomplete
)(messages())
        return f'''{cls.build_system_prompt(scope)}\nRuntime context summary:\n{compact_summary}\n\nRuntime context:\n{compact_context}\n\nCurated knowledge notes:\n{compact_knowledge}\n\nConversation:\n{conversation_text}\n'''
)()
    _parse_ai_response = (lambda cls = None, raw_value = None:
