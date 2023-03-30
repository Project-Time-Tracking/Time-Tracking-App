# Import SQLAlchemy / Flask
from flask_sqlalchemy import SQLAlchemy


# Assign to variable db
db = SQLAlchemy()

# Create a model for Project (Adrian)
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

#Create a model for tasks (Adrian)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    time_estimate = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    time_actual = db.Column(db.Integer)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref('tasks', lazy=True))
    #Create a funtion to return a string (Adrian)
    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'time_estimate': self.time_estimate,
            'completed': self.completed,
            'time_actual': self.time_actual
        }