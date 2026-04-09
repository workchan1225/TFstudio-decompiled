# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Infrastructure Repositories

SQLAlchemy implementations of domain repository interfaces.
These repositories handle database operations for domain entities.
'''
from typing import Optional, List
from app.domain.entities import Project as ProjectEntity, Character as CharacterEntity
from app.domain.interfaces import IProjectRepository
from app.infrastructure.mappers import ProjectMapper, CharacterMapper
from app.models.project import Project as ProjectORM, Character as CharacterORM

class SQLAlchemyProjectRepository(IProjectRepository):
    '''
    SQLAlchemy implementation of IProjectRepository.

    This repository handles Project entity persistence using SQLAlchemy ORM.
    '''
    
    def __init__(self, session):
        '''
        Initialize repository with SQLAlchemy session.

        Args:
            session: SQLAlchemy session (typically db.session)
        '''
        self._session = session

    
    def get_by_id(self = None, project_id = None):
        '''Get a project by its ID'''
        orm_project = self._session.query(ProjectORM).filter_by(id = project_id).first()
    # WARNING: Decompyle incomplete

    
    def get_all(self = None):
        '''Get all projects'''
        orm_projects = self._session.query(ProjectORM).order_by(ProjectORM.updated_at.desc()).all()
        return orm_projects()

    
    def save(self = None, project = None, commit = None):
        '''
        Save a project (create or update).

        If the project already exists in the database, it will be updated.
        Otherwise, a new record will be created.
        '''
        existing = self._session.query(ProjectORM).filter_by(id = project.id).first()
        if existing:
            ProjectMapper.update_orm(existing, project)
            self._sync_characters(existing, project)
            if commit:
                self._session.commit()
            else:
                self._session.flush()
            return ProjectMapper.to_domain(existing)
        orm_project = None.to_orm(project)
        for char_entity in project.characters:
            char_orm = CharacterMapper.to_orm(char_entity, project.id)
            orm_project.characters.append(char_orm)
            self._session.add(orm_project)
            if commit:
                self._session.commit()
            else:
                self._session.flush()
        return ProjectMapper.to_domain(orm_project)

    
    def delete(self = None, project_id = None):
        '''Delete a project by its ID'''
        orm_project = self._session.query(ProjectORM).filter_by(id = project_id).first()
    # WARNING: Decompyle incomplete

    
    def exists(self = None, project_id = None):
        '''Check if a project exists'''
        count = self._session.query(ProjectORM).filter_by(id = project_id).count()
        return count > 0

    
    def exists_by_title(self = None, title = None):
        '''Check if a project with the given title already exists'''
        count = self._session.query(ProjectORM).filter_by(title = title).count()
        return count > 0

    
    def _sync_characters(self = None, orm_project = None, entity = None):
        '''Synchronize characters between ORM and domain entity'''
        existing_ids = orm_project.characters()
        entity_ids = entity.characters()
        for char_orm in list(orm_project.characters):
            if char_orm.id not in entity_ids:
                self._session.delete(char_orm)
            for char_entity in entity.characters:
                if char_entity.id not in existing_ids:
                    char_orm = CharacterMapper.to_orm(char_entity, entity.id)
                    orm_project.characters.append(char_orm)
                    continue
                for char_orm in orm_project.characters:
                    if char_orm.id == char_entity.id:
                        char_orm.name = char_entity.name
                        char_orm.description = char_entity.description
                        char_orm.image_url = char_entity.image_url
                        (lambda .0: pass# WARNING: Decompyle incomplete
)
                    
                    return None
