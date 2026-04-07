from functools import wraps
from flask import session

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if user is logged in
        if 'lamar_id' not in session:
            return "You must be logged in.", 401

        # Check if user has admin role
        if session.get('role') != 'admin':
            return "Admin access required.", 403

        return f(*args, **kwargs)
    return decorated_function