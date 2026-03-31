from flask import Blueprint, request, make_response

reservations_bp = Blueprint('reservations', __name__)

# View all reservations for a user
@reservations_bp.route('/<string:lamar_id>', methods=['GET'])
def get_reservations(lamar_id):
    return f"Viewing reservations for user {lamar_id}."

# Create a reservation for a user
@reservations_bp.route('/<string:lamar_id>/<string:room_number>', methods=['POST'])
def reserve_room(lamar_id, room_number):
    response = make_response()
    response.status_code = 200
    response.headers['Content-Type'] = 'text/html'
    return f"Reserving room {room_number} for user {lamar_id}."

# Soft delete - cancels the reservation
@reservations_bp.route('/<string:lamar_id>/<string:room_number>/cancel', methods=['PATCH'])
def cancel_reservation(lamar_id, room_number):
    response = make_response()
    response.status_code = 200
    response.headers['Content-Type'] = 'text/html'
    return f"Cancelling reservation for room {room_number} for user {lamar_id}."

# Modify reservation - allows changing the room number or reservation details
@reservations_bp.route('/<string:lamar_id>/<string:room_number>', methods=['PATCH'])
def modify_reservation(lamar_id, room_number):
    response = make_response()
    response.status_code = 200
    response.headers['Content-Type'] = 'text/html'
    return f"Modifying reservation for room {room_number} for user {lamar_id}."

# Hard delete - admin only
@reservations_bp.route('/<string:lamar_id>/<string:room_number>', methods=['DELETE'])
def delete_reservation(lamar_id, room_number):
    response = make_response()
    response.status_code = 200
    response.headers['Content-Type'] = 'text/html'
    return f"Reservation for room {room_number} for user {lamar_id} has been deleted."