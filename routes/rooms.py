from flask import Flask, Blueprint, make_response

rooms_bp = Blueprint('rooms', __name__)

@rooms_bp.route('/<string:room_number>/availablity', methods=['GET', 'POST'])
def reserve_room(lamar_id, room_number):
    response = make_response()
    response.status_code = 200
    response.headers['Content-Type'] = 'text/html'
    return f"Reserving room {room_number} for user {lamar_id}."