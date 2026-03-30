from flask import Blueprint, request, make_response

users_bp = Blueprint('users', __name__)

@users_bp.route('/<string:lamar_id>', methods=['GET', 'POST'])
def get_user(lamar_id):
    response = make_response()
    response.status_code = 200
    response.headers['Content-Type'] = 'text/html'
    return f"User: {lamar_id}"

@users_bp.route('/<string:lamar_id>', methods=['PATCH'])
def deactivate_user(lamar_id):
    return f"User: {lamar_id} deactivated"


@users_bp.route('/string:lamar_id>', methods=['DELETE'])
def delete_user(lamar_id):
    return f"User: {lamar_id} deleted"