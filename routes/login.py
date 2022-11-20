from flask import Blueprint, request, render_template, redirect
from prisma.models import User
from flask_login import login_user, logout_user, login_required, current_user
from libraries.db.models import UserModel, get_user

login_blueprint = Blueprint('login', __name__ , template_folder='../pages/', static_folder='../assets/')

@login_blueprint.route('/', methods=['GET','POST'])
def list_create():
  if request.method == 'GET':
    if current_user.is_authenticated:
      return redirect('/dashboard')
    return render_template('login.html')

  if request.method == 'POST':
    data = request.form

    if data is None:
      return  

    user = get_user(data['email'])
    if user is None:
      return 'User not found'
    login_user(UserModel(user))
    return redirect('/dashboard')