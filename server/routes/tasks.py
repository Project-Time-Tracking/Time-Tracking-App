from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models.index import Project, Task


#(matt)
@app.route('/projects/<int:project_id>/tasks', methods=['POST'])
def create_task(project_id):
    project = Project.query.get_or_404(project_id)
    data = request.get_json()
    task = Task(description=data['description'], time_estimate=data['time_estimate'], project_id=project_id)
    db.session.add(task)
    db.session.commit()
    return jsonify(task.serialize()), 201
#(matt)
@app.route('/projects/<int:project_id>/tasks/<int:task_id>', methods=['PUT'])
def update_task(project_id, task_id):
    project = Project.query.get_or_404(project_id)
    task = Task.query.filter_by(id=task_id, project_id=project_id).first_or_404()
    data = request.get_json()
    if 'description' in data:
        task.description = data['description']
    if 'time_estimate' in data:
        task.time_estimate = data['time_estimate']
    if 'completed' in data:
        task.completed = data['completed']
    if 'time_actual' in data:
        task.time_actual = data['time_actual']
    db.session.commit()
    return jsonify(task.serialize()), 200
#(matt)
@app.route('/projects/<int:project_id>/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(project_id, task_id):
    project = Project.query.get_or_404(project_id)
    task = Task.query.filter_by(id=task_id, project_id=project_id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    return jsonify({}), 204

#(matt)
if __name__ == '__main__':
    app.run(debug=True)