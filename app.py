from flask import Flask
from models.user import User
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

@app.route('/test', methods=['GET'])
def test():
  return "Dale"

if __name__ == '__main__':
  app.run(debug=True)