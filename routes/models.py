from database import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    lamar_id = db.Column(db.String(100), primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    lamar_email = db.Column(db.String(120), unique=True, nullable=False)
    lamar_password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    group_type = db.Column(db.String(20), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)