from flask import Blueprint, request, render_template
from prisma.models import User
from flask_login import login_user

login_blueprint = Blueprint('login', __name__ , template_folder='../pages/')

@login_blueprint.route('/', methods=['GET','POST'])
def list_create():
  if request.method == 'GET':
    return render_template('login.html')

  if request.method == 'POST':
    data = request.form

    if data is None:
      return

    email = data.get('email')
    password = data.get('password')
    if email is None or password is None:
      return {"error": "You need to provide email and password"}
    user = User.prisma().find_many(where={'email': email, 'password': password},)
    print(user)
    return login_user(user)