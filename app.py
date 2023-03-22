from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models.index import Project, Task

# Import database models into app (Adrian)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

#Create a route for Home page (Adrian)
@app.route("/")
def home():
    return "Hello, Flask!" #this is imcomplete and will need to be worked on

# Create a route for Projects (Adrian)
@app.route('/projects')
def project():
    projects = Project.query.all()
    return render_template('home.html', projects=projects)

# Create a Route for Tasks (Adrian)
@app.route('/projects/<int:id>')
def project_tasks(id):
    project = Project.query.get(id)
    tasks = Task.query.filter_by(project_id=id).all()
    return render_template('project_tasks.html', project=project, tasks=tasks)

