from flask import Blueprint, request, make_response

rooms_bp = Blueprint('rooms', __name__)

# View all rooms
@rooms_bp.route('/', methods=['GET'])
def get_all_rooms():
    return "Viewing all available rooms."

# View a specific room's details
@rooms_bp.route('/<string:room_number>', methods=['GET'])
def get_room(room_number):
    return f"Viewing details for room {room_number}."

# Check a room's availability
@rooms_bp.route('/<string:room_number>/availability', methods=['GET'])
def check_availability(room_number):
    # TODO: Query reservations to check if room is free for requested date/time
    return f"Checking availability for room {room_number}."

# Check if a room is currently occupied
@rooms_bp.route('/<string:room_number>/occupancy', methods=['GET'])
def check_occupancy(room_number):
    # TODO: Check if anyone is currently checked into this room
    return f"Checking occupancy status for room {room_number}."

# View all rooms with their current status
@rooms_bp.route('/status', methods=['GET'])
def all_rooms_status():
    # TODO: Return list of all rooms showing occupied, available, or reserved
    return "Viewing status of all rooms."