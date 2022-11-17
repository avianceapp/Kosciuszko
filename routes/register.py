from flask import Blueprint, request, render_template
from prisma.models import User

user_blueprint = Blueprint('register', __name__ , template_folder='../pages/')

@user_blueprint.route('/', methods=['GET','POST'])
def list_create():
  if request.method == 'POST':
    data = request.form

    if data is None:
      return

    name = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if name is None or email is None:
      return {"error": "You need to provide name and email"}

    user = User.prisma().create(data={'email': email, 'username': name, 'password': password})

    return dict(user)
  return render_template('register.html')