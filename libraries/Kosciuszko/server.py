import os

from prisma import Client

client = Client()

from flask import Flask, jsonify, redirect, render_template, request
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

app = Flask(__name__,template_folder='../../pages/')
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return client.user.find_first(where={'id': user_id})

@app.route('/login', methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':    
        email = request.form['email']
        password = request.form['password']
        user = client.user.find_unique(where={'email': email})
        if user and user.password == password:
            login_user(user)
            return jsonify(user)
        return jsonify({'error': 'Invalid credentials'})
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out'})

@app.route('/register', methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        user = client.user.create(data={'email': email, 'password': password, 'admin': False, 'username': username})
        return redirect('/')
    return render_template('register.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)