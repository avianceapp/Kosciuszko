from flask import Blueprint, request, render_template
from prisma.models import User
from flask_login import login_user, logout_user, login_required, current_user
from libraries.db.models import UserModel, get_user

login_blueprint = Blueprint('login', __name__ , template_folder='../pages/')

@login_blueprint.route('/', methods=['GET','POST'])
def list_create():
  if request.method == 'GET':
    return render_template('login.html')

  if request.method == 'POST':
    data = request.form

    if data is None:
      return  
    #create a way to login with flask-login the User from prisma.models, and redirect to the dashboard.
    #if the user is not found, return a message to the user.

    user = get_user(data['email'])
    if user is None:
      return 'User not found'
    login_user(UserModel(user))
    return f'Hello, {user.username}!'