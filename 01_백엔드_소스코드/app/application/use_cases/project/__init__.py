# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Project Use Cases

Use cases for project-related operations.
Each use case follows the Command pattern with a single execute() method.
'''
from uuid import uuid4
from typing import Optional
from app.domain.entities import Project
from app.domain.enums import ProjectType, ProjectStatus
from app.domain.interfaces import IProjectRepository
from app.application.dtos import CreateProjectRequest, GetProjectRequest, UpdateProjectRequest, DeleteProjectRequest, SetTopicRequest, SetScriptRequest, ProjectResponse, ProjectListResponse, DeleteProjectResponse
from app.application.exceptions import ValidationException, NotFoundException

class CreateProjectUseCase:
    '''
    Use case for creating a new project.

    This use case validates input, creates a new project entity,
    and persists it using the repository.
    '''
    
    def __init__(self = None, repository = None):
        self._repository = repository

    
    def execute(self = None, request = None):
        '''Create a new project'''
        if not request.title or request.title.strip():
            raise ValidationException('title', 'Title cannot be empty')
        title = request.title.strip()
        if self._repository.exists_by_title(title):
            title = self._generate_unique_title(title)
        project = Project(id = str(uuid4()), title = title, project_type = ProjectType.from_string(request.project_type))
        saved = self._repository.save(project)
        return ProjectResponse.from_entity(saved)

    
    def _generate_unique_title(self = None, base_title = None):
        '''Generate a unique title by appending a number'''
        counter = 1
        new_title = f'''{base_title} ({counter})'''
        if not self._repository.exists_by_title(new_title):
            return new_title
        None += 1
        if counter > 1000:
            raise ValidationException('title', '고유한 프로젝트명을 생성할 수 없습니다')
        continue



class GetProjectUseCase:
    '''
    Use case for retrieving a project by ID.
    '''
    
    def __init__(self = None, repository = None):
        self._repository = repository

    
    def execute(self = None, request = None):
        '''Get a project by ID'''
        project = self._repository.get_by_id(request.project_id)
    # WARNING: Decompyle incomplete



class GetAllProjectsUseCase:
    '''
    Use case for retrieving all projects.
    '''
    
    def __init__(self = None, repository = None):
        self._repository = repository

    
    def execute(self = None):
        '''Get all projects'''
        projects = self._repository.get_all()
        responses = projects()
        return ProjectListResponse(projects = responses)



class UpdateProjectUseCase:
    '''
    Use case for updating an existing project.
    '''
    
    def __init__(self = None, repository = None):
        self._repository = repository

    
    def execute(self = None, request = None, *, commit):
        '''Update a project'''
        project = self._repository.get_by_id(request.project_id)
    # WARNING: Decompyle incomplete



class DeleteProjectUseCase:
    '''
    Use case for deleting a project.
    '''
    
    def __init__(self = None, repository = None):
        self._repository = repository

    
    def execute(self = None, request = None):
        '''Delete a project'''
        success = self._repository.delete(request.project_id)
        if not success:
            raise NotFoundException('Project', request.project_id)
        return DeleteProjectResponse(success = True, message = f'''Project {request.project_id} deleted successfully''')



class SetProjectTopicUseCase:
    """
    Use case for setting a project's topic.
    """
    
    def __init__(self = None, repository = None):
        self._repository = repository

    
    def execute(self = None, request = None):
        '''Set project topic'''
        project = self._repository.get_by_id(request.project_id)
    # WARNING: Decompyle incomplete



class SetProjectScriptUseCase:
    """
    Use case for setting a project's script.
    """
    
    def __init__(self = None, repository = None):
        self._repository = repository

    
    def execute(self = None, request = None):
        '''Set project script'''
        project = self._repository.get_by_id(request.project_id)
    # WARNING: Decompyle incomplete
