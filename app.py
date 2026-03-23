from flask import Flask, request, make_response, render_template


app = Flask(__name__, template_folder='templates')
@app.route('/')
def index():
    return render_template('index.html')

# URL Processors
@app.route('/LibraryReserveApp')
def library_reserve_app():                         # This is how you craft custom responses in Flask
    response = make_response()
    response.status_code = 200
    response.headers['Content-Type'] = 'text/html'
    return response
    

@app.route('/search', methods=['GET', 'POST'])
def search():
    response = make_response()
    response.status_code = 200
    response.headers['Content-Type'] = 'text/html'
    return "Search results will be displayed here."

@app.route('/user/<string:lamar_id>', methods=['GET', 'POST'])
def get_user(lamar_id):
    response = make_response()
    response.status_code = 200
    response.headers['Content-Type'] = 'text/html'
    return f"User: {lamar_id}"

@app.route('/reserve/<string:lamar_id>/<string:room_number>', methods=['GET', 'POST'])
def reserve_room(lamar_id, room_number):
    response = make_response()
    response.status_code = 200
    response.headers['Content-Type'] = 'text/html'
    return f"Reserving room {room_number} for user {lamar_id}."

# Put the blueprints registration here
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)