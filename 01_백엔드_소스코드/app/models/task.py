# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: task.pyc (Python 3.11)

'''
비동기 태스크 DB 모델

장시간 실행되는 작업의 상태를 DB에 저장하여
서버 재시작에도 상태가 유지되도록 합니다.
'''
import json
from datetime import datetime
from app import db

class TaskModel(db.Model):
    '''비동기 태스크 상태를 저장하는 DB 모델'''
    __tablename__ = 'tasks'
    id = db.Column(db.String(36), primary_key = True)
    type = db.Column(db.String(50), nullable = False)
    status = db.Column(db.String(20), default = 'pending')
    progress = db.Column(db.Integer, default = 0)
    message = db.Column(db.String(500), default = '')
    result = db.Column(db.Text, nullable = True)
    error = db.Column(db.Text, nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    started_at = db.Column(db.DateTime, nullable = True)
    completed_at = db.Column(db.DateTime, nullable = True)
    
    def to_dict(self):
        '''Task를 딕셔너리로 변환 (API 응답용)'''
        result_data = None
        if self.result:
            
            try:
                result_data = json.loads(self.result)
            except (json.JSONDecodeError, TypeError):
                result_data = self.result

        return {
            'id': self.id,
            'type': self.type,
            'status': self.status,
            'progress': self.progress,
            'message': self.message,
            'result': result_data,
            'error': self.error,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'started_at': self.started_at.isoformat() if self.started_at else None,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None }

    create = (lambda cls = None, task_id = None, task_type = classmethod: task = cls(id = task_id, type = task_type, status = 'pending', progress = 0, message = '', created_at = datetime.utcnow())db.session.add(task)db.session.commit()task)()
    get_by_id = (lambda cls = None, task_id = None: cls.query.get(task_id))()
    
    def update_status(self, status = None, progress = None, message = None, result = (None, None, None, None, None), error = ('status', str, 'progress', int, 'message', str, 'error', str)):
        '''태스크 상태 업데이트'''
        if status:
            self.status = status
            if not status == 'running' and self.started_at:
                self.started_at = datetime.utcnow()
            elif status in ('completed', 'failed'):
                self.completed_at = datetime.utcnow()
    # WARNING: Decompyle incomplete

    recover_interrupted_tasks = (lambda cls: interrupted = cls.query.filter(cls.status.in_([
'pending',
'running'])).all()count = 0for task in interrupted:
task.status = 'failed'task.error = '서버가 재시작되어 작업이 중단되었습니다.'task.completed_at = datetime.utcnow()count += 1if count > 0:
db.session.commit()count)()
    cleanup_old_tasks = (lambda cls = None, keep_count = classmethod: completed_tasks = cls.query.filter(cls.status.in_([
'completed',
'failed'])).order_by(cls.completed_at.asc()).all()if len(completed_tasks) > keep_count:
to_delete = completed_tasks[:len(completed_tasks) - keep_count]for task in to_delete:
db.session.delete(task)db.session.commit()len(to_delete)0)()
