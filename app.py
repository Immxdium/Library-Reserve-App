from flask import Flask, make_response, render_template
from routes.users import users_bp
from routes.rooms import rooms_bp
from routes.reservations import reservations_bp
from routes.auth import auth_bp

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/LibraryReserveApp')
def library_reserve_app():
    response = make_response()
    response.status_code = 200
    response.headers['Content-Type'] = 'text/html'
    return response

@app.route('/search', methods=['GET', 'POST'])
def search():
    return "Search results will be displayed here."

# Put the blueprints registration here
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(users_bp, url_prefix='/user')
app.register_blueprint(rooms_bp, url_prefix='/rooms')
app.register_blueprint(reservations_bp, url_prefix='/reserve')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)