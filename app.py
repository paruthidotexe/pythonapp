from flask import Flask, render_template, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from data import Tasks
import MySQLdb
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12225833:W5ty4XwEqT@sql12.freesqldatabase.com/sql12225833'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
## c00lsqldb
## 274031
## Host: sql12.freesqldatabase.com
## Database name: sql12225833
## Database user: sql12225833
## Database password: W5ty4XwEqT
## Port number: 3306

class ExampleTasks(db.Model):
    __tablename__ = "exampletasks"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.Unicode(32))
    desc = db.Column("desc", db.Unicode(256))
    author = db.Column("author", db.Unicode(32))
    create_date = db.Column("create_date", db.Unicode(32))
    status = db.Column("status", db.Integer)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.Unicode(32))
    password = db.Column("password", db.Unicode(32))
    email = db.Column("email", db.Unicode(64))
    phone = db.Column("phone", db.Unicode(32))


Tasks = Tasks()

## REST API : JSON
@app.route("/api/v1/users", methods=['GET'])
def GetAllUsers():
    users = User.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['username'] = user.username
        user_data['password'] = user.password
        user_data['email'] = user.email
        user_data['phone'] = user.phone
        output.append(user_data)

    return jsonify({'users' : output})

@app.route("/api/v1/user/<username>", methods=['GET'])
def GetOneUser():
    return ""

@app.route("/api/v1/users", methods=['POST'])
def CreateUser():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    print (new_user.id)
    print (new_user.username + new_user.password)
    return jsonify({'message' : new_user.username + ' Created!'})

@app.route("/api/v1/user/<username>", methods=['PUT'])
def UpdateUser():
    return ""
  
@app.route("/api/v1/user/<username>", methods=['DELETE'])
def DeleteUser():
    return ""

## html pages
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contacts")
def contacts():
    return render_template('contacts.html')

@app.route("/tasks")
def allTasks():
    return render_template('tasks.html', tasks = Tasks)

@app.route("/task/<string:id>/")
def selectedTasks(id):
    for task in Tasks:
        if(task['id'] == id):
            return render_template('task.html', task=task)
    #on error shows tasks list again
    return render_template('tasks.html', tasks = Tasks)

@app.route("/signin", methods=["GET"])
def signinpage():
    return render_template('signin.html', tasks = Tasks)

@app.route("/signin", methods=["POST"])
def signin():
    return render_template('signin.html', tasks = Tasks)

if __name__ == '__main__':
    app.run(debug=True, port=7777)


