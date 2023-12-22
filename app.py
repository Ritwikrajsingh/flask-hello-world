from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/projects')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/methods', methods=['GET', 'POST', 'PUT', 'DELETE'])
def login():
    if request.method == 'POST':
        if request.data:
            body = request.get_json()
            return body
        return {}
    else:
        return f'{request.method} request'

if __name__ == '__main__':
    app.run(debug=True)