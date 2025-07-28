from datetime import datetime
from app import db

class Task(db.Model):
    """
    Database model for tasks
    Think of this as a blueprint for how task data is stored
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Task {self.title}>'
    
    def to_dict(self):
        """Convert task to dictionary (useful for API responses later)"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }