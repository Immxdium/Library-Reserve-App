from flask import Blueprint, request, session

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    # Check if already locked out
    if session.get('failed_attempts', 0) >= 5:
        return "Account locked. Try again later.", 403

    lamar_id = request.form.get('lamar_id')
    password = request.form.get('password')

    # TODO: Replace with database query from partner's models
    # Example: user = User.query.filter_by(lamar_id=lamar_id).first()
    if lamar_id == 'admin' and password == 'password':

        # TODO: Check if user is deactivated (soft deleted)
        # Example: if not user.active:
        #     return "This account is inactive.", 403

        session['lamar_id'] = lamar_id
        session['role'] = 'admin'  # TODO: Pull from database
        session['failed_attempts'] = 0
        return "Login successful!"
    else:
        session['failed_attempts'] = session.get('failed_attempts', 0) + 1
        remaining = 5 - session['failed_attempts']
        return f"Invalid username or password. {remaining} attempts remaining.", 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return "Logged out successfully."

@auth_bp.route('/status', methods=['GET'])
def status():
    if 'lamar_id' in session:
        return f"Logged in as {session['lamar_id']} with role {session['role']}."
    else:
        return "Not logged in.", 401