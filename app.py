from flask import Flask
from prisma import Prisma, register
from routes.register import user_blueprint
from prisma.models import User
from routes.login import login_blueprint
# from routes.post import post_blueprint

db = Prisma()
db.connect()
register(db)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return {
    "ping": "pong"
  }

app.register_blueprint(user_blueprint, url_prefix='/register')
app.register_blueprint(login_blueprint, url_prefix='/login')

if __name__ == "__main__":

  app.run(debug=True, port=5000, threaded=True)
