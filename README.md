# Library Room Reservation App

A Flask-based backend for the Mary and John Gray Library at Lamar University. This application allows users to reserve, manage, and check in/out of library spaces.

## Library Spaces

| Room | Floor | Capacity | Use | Student Groups |
|------|-------|----------|-----|----------------|
| Lobby | 1st | 45 | Events | Allowed |
| Event Space (near 623) | 6th | 75 | Classes, Events, Meetings | Not Allowed |
| Room 702 | 7th | 40 | Classes, Meetings, Events | Not Allowed |
| Room 708A | 7th | 27 | Classes & Training | Not Allowed |
| Room 717 | 7th | 15 | Non-instructional Meetings | Not Allowed |

## Project Structure

```
Library Reserve App/
├── app.py                  # Flask app setup, blueprint registration, main routes
├── config.py               # Configuration settings (SECRET_KEY, database URI)
├── database.py             # SQLAlchemy initialization
├── utils.py                # Helper functions (@admin_required decorator)
├── routes/
│   ├── __init__.py         # Makes routes a Python package
│   ├── auth.py             # Login, logout, session management
│   ├── users.py            # User profile, deactivation, deletion
│   ├── rooms.py            # Room details, availability, occupancy
│   └── reservations.py     # Reservations, check-in/out, renewals
└── templates/
    └── index.html          # Frontend homepage
```

## Setup and Installation

### Prerequisites

- Python 3.x
- pip

### Steps

1. Clone the repository:
   ```
   git clone https://github.com/Immxdium/Library-Reserve-App.git
   cd Library-Reserve-App
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv env
   source env/bin/activate
   ```

3. Install dependencies:
   ```
   pip install flask flask-sqlalchemy
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5555/
   ```

## Features

### Authentication (routes/auth.py)

- **Login** — POST `/auth/login` — Validates user credentials and creates a session
- **Logout** — POST `/auth/logout` — Clears the user session
- **Status** — GET `/auth/status` — Returns current login status and user role
- **Failed Attempt Tracking** — Locks account after 5 failed login attempts

### User Management (routes/users.py)

- **View User** — GET `/user/<lamar_id>` — Retrieves user profile information
- **Deactivate User** — PATCH `/user/<lamar_id>/deactivate` — Soft deletes a user (sets active to false)
- **Reactivate User** — PATCH `/user/<lamar_id>/reactivate` — Restores a soft-deleted user
- **Delete User** — DELETE `/user/<lamar_id>` — Permanently removes a user (admin only)

### Room Management (routes/rooms.py)

- **View All Rooms** — GET `/rooms/` — Lists all five reservable library spaces
- **View Room Details** — GET `/rooms/<room_number>` — Shows capacity, equipment, and booking rules for a specific room
- **Check Availability** — GET `/rooms/<room_number>/availability` — Checks if a room is free for a requested date and time
- **Check Occupancy** — GET `/rooms/<room_number>/occupancy` — Shows if a room is currently in use
- **All Rooms Status** — GET `/rooms/status` — Displays current status of all rooms

### Reservation Management (routes/reservations.py)

- **View Reservations** — GET `/reserve/<lamar_id>` — Shows all reservations for a user
- **Create Reservation** — POST `/reserve/<lamar_id>/<room_number>` — Books a room for a user
- **Check In** — PATCH `/reserve/<lamar_id>/<room_number>/checkin` — Marks a reservation as in use when user arrives
- **Check Out** — PATCH `/reserve/<lamar_id>/<room_number>/checkout` — Marks a reservation as completed when user leaves
- **Renew Reservation** — PATCH `/reserve/<lamar_id>/<room_number>/renew` — Extends the reservation end time
- **Cancel Reservation** — PATCH `/reserve/<lamar_id>/<room_number>/cancel` — Soft deletes a reservation (updates status to cancelled)
- **Modify Reservation** — PATCH `/reserve/<lamar_id>/<room_number>` — Updates reservation details
- **Delete Reservation** — DELETE `/reserve/<lamar_id>/<room_number>` — Permanently removes a reservation (admin only)

### Admin Protection (utils.py)

- **@admin_required Decorator** — Restricts access to admin-only routes. Checks that the user is logged in and has an admin role before allowing access. Returns 401 if not logged in and 403 if not an admin.

## Policy Rules (To Be Implemented)

The following validation rules from the library policy document will be enforced:

- All reservations must be submitted at least 24 hours in advance
- All reservations must end 30 minutes prior to library closing
- Rooms 702 and 708A are restricted to librarian-led instruction during the first 8 weeks of Fall and Spring semesters
- Student groups may only reserve the Lobby
- Non-university groups may not reserve any library spaces
- Library spaces may not be booked for regularly scheduled courses or recurring meetings
- Each room has a priority ordering that determines who can book and who may be bumped

## Reservation Statuses

- **active** — Booked but not yet started
- **in_use** — User has checked in
- **completed** — User has checked out
- **cancelled** — Reservation was soft deleted

## Testing Routes

GET routes can be tested in the browser. For POST, PATCH, and DELETE routes, use curl or Postman.

Example curl commands:

```
# Login
curl -X POST http://127.0.0.1:5555/auth/login -d "lamar_id=admin&password=password"

# Check in
curl -X PATCH http://127.0.0.1:5555/reserve/L12345/702/checkin

# Cancel reservation
curl -X PATCH http://127.0.0.1:5555/reserve/L12345/702/cancel

# Logout
curl -X POST http://127.0.0.1:5555/auth/logout
```

## Team Responsibilities

- **Backend (Flask/Python)** — Routes, blueprints, authentication, validation logic
- **Database (SQLite)** — Models, tables, relationships, queries
- **Frontend** — User interface, forms, display

## Tech Stack

- **Framework:** Python/Flask with Blueprints
- **Database:** SQLAlchemy over SQLite
- **Version Control:** GitHub
