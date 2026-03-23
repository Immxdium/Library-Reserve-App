from flask import Blueprint, request, make_response

users_bp = Blueprint('users', __name__)

@users_bp.route('/<string:lamar_id>', methods=['GET', 'POST'])
def reserve_room(lamar_id, room_number):
    response = make_response()
    response.status_code = 200
    response.headers['Content-Type'] = 'text/html'
    return f"Reserving room {room_number} for user {lamar_id}."