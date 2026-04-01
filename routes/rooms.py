from flask import Flask, Blueprint, make_response

rooms_bp = Blueprint('rooms', __name__)

@rooms_bp.route('/<string:room_number>/availability', methods=['GET'])
def check_availability(room_number):
    return f"Checking availability for room {room_number}."

@rooms_bp.route('/<string:room_number>/book', methods=['POST'])
def book_room(room_number):
    return f"Booking room {room_number}."