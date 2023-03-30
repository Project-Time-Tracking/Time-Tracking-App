#Import fraemowrk (Adrian)
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired

#Form for creating a new project (Adrian)
class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')

#Form for creating tasks (Adrian)
class TaskForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired()])
    time_estimate = IntegerField('Estimated Completion Time (hours)', validators=[DataRequired()])
    time_actual = IntegerField('Actual Completion Time (hours)', validators=[DataRequired()])
    project_id = SelectField('Project', coerce=int, validators=[DataRequired()])