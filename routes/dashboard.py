from flask import Blueprint, request, render_template, redirect
from prisma.models import User
from flask_login import login_user, logout_user, login_required, current_user
from libraries.db.models import UserModel, get_user

dashboard_blueprint = Blueprint('dashboard', __name__ , template_folder='../pages/')

@dashboard_blueprint.route('/', methods=['GET','POST'])
@login_required
def dashboard():
  if request.method == 'GET':
    return render_template('dashboard.html')