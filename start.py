from flask import Flask, request, jsonify, url_for, session, redirect


def start_server():
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return '<h1>Hello, World!</h1>'

    @app.route('/about')
    def about():
        return '<h3>This is a Flask web application.</h3>'

    @app.route('/users/<name>')
    def hello_name(name):
        return "Hello, %s" % name

    @app.route('/<string:name>')
    def hello_name_1(name):
        return "Hello, World %s" % name

    @app.route('/projects/')
    def projects():
        return "Hello Project"

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            return "POST method is called"
        else:
            return "GET method is called"

    @app.route('/users')
    def get_users():
        users = [
            {
                "name": "John"
            }
        ]
        return jsonify(users)

    # doubt
    @app.route("/static/<string:name>")
    def static_files(name):
        return url_for('users_s', filename=name)

    @app.route("/users_s")
    def users_s():
        return []

    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/*'

    @app.route('/')
    def index():
        if 'username' in session:
            return f'Logged in as {session["username"]}'
        return '''
            You are not logged in
             <form method=get action="/login_n">
                <p><input type=submit value=Login>
        '''

    @app.route('/login_n', methods=['GET', 'POST'])
    def login_n():
        if request.method == 'POST':
            session["username"] = request.form['username']
            return redirect(url_for('index'))
        return '''
            <form method=post>
                <p><input type=text name=username>
                <p><input type=submit value=Login>
        '''

    @app.route('/logout', methods=['GET', 'POST'])
    def logout():
        session.pop('username', None)
        return redirect(url_for('login_n'))

    app.run(debug=True)
