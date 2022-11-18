from flask import Flask
from flask_login import LoginManager
from prisma import Prisma, register
from routes.register import user_blueprint
from prisma.models import User
from routes.login import login_blueprint
from routes.logout import logout_blueprint
# from routes.post import post_blueprint

db = Prisma()
db.connect()
register(db)

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.secret_key = "ABORT"
@app.login_manager.user_loader
def load_user(_id):
    if _id is not None:
      user = User.prisma().find_first(where={'id': _id})
      return user
    else:
      return None
@app.route('/', methods=['GET'])
def index():
  return {
    "ping": "pong"
  }

app.register_blueprint(logout_blueprint, url_prefix='/logout')
app.register_blueprint(user_blueprint, url_prefix='/register')
app.register_blueprint(login_blueprint, url_prefix='/login')

if __name__ == "__main__":

  app.run(debug=True, port=5000, threaded=True)
