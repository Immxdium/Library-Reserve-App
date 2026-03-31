from flask import Flask, make_response, render_template
from database import db, init_db

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = "the-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///library_reserve_app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)