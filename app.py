from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from data import Tasks

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


Tasks = Tasks()

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


if __name__ == '__main__':
    app.run(debug=True, port=7777)


