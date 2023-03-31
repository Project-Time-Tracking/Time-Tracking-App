from flask import Flask, render_template
from server.models.index import db, Project, Task

# Import database models into app (Adrian)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
with app.app_context():
    db.create_all()

#Create a route for Home page (Adrian)
@app.route("/")
def home():
    return render_template("home.html")

# Create a route for Projects (Adrian)
@app.route('/projects')
def project():
    projects = Project.query.all()
    return render_template("projects.html", projects=projects)

# Create a Route for Tasks (Adrian)
@app.route('/projects/<int:id>')
def project_tasks(id):
    project = Project.query.get(id)
    tasks = Task.query.filter_by(project_id=id).all()
    return render_template('project_tasks.html', project=project, tasks=tasks)

