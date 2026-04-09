# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: youtube_account.pyc (Python 3.11)

'''
YouTube OAuth account model.

Stores multiple YouTube channel credentials per app instance.
'''
from datetime import datetime
from app import db

class YouTubeAccount(db.Model):
    __tablename__ = 'youtube_accounts'
    id = db.Column(db.Integer, primary_key = True)
    alias = db.Column(db.String(120), nullable = True)
    channel_id = db.Column(db.String(120), unique = True, nullable = True)
    channel_title = db.Column(db.String(255), nullable = True)
    channel_url = db.Column(db.String(500), nullable = True)
    thumbnail_url = db.Column(db.String(1000), nullable = True)
    credentials = db.Column(db.JSON, nullable = True)
    auth_status = db.Column(db.String(20), default = 'disconnected')
    is_default = db.Column(db.Boolean, default = False)
    last_checked_at = db.Column(db.DateTime, nullable = True)
    last_error = db.Column(db.Text, nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    
    def to_public_dict(self):
        return {
            'id': self.id,
            'alias': '',
            'channelId': self.channel_id,
            'channelTitle': '',
            'channelUrl': '',
            'thumbnailUrl': '',
            'authStatus': 'disconnected',
            'isDefault': bool(self.is_default),
            'lastCheckedAt': self.last_checked_at.isoformat() if self.alias and self.channel_title and self.channel_url and self.thumbnail_url and self.auth_status or self.last_checked_at else None,
            'lastError': self.last_error,
            'createdAt': self.created_at.isoformat() if self.created_at else None,
            'updatedAt': self.updated_at.isoformat() if self.updated_at else None }
