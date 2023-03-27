from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from server.models.index import Project, Task

# Import database models into app (Adrian)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

#Create a route for Home page (Adrian)
@app.route("/")
def home():
    return render_template("home.html")

# Create a route for Projects (Adrian)
@app.route('/projects')
def project():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)

# Create a Route for Tasks (Adrian)
@app.route('/projects/<int:id>')
def project_tasks(id):
    project = Project.query.get(id)
    tasks = Task.query.filter_by(project_id=id).all()
    return render_template('project_tasks.html', project=project, tasks=tasks)

