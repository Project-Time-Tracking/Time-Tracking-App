from flask import jsonify, request
from models.index import db, Project
import app

# Create a new project
@app.route('/new', methods=['POST'])
def create_project():
    data = request.get_json()
    project = Project(title=data['title'], description=data['description'])
    db.session.add(project)
    db.session.commit()
    return jsonify({'message': 'Project created successfully!'})

# Update an existing project
@app.route('/projects/<int:id>', methods=['PUT'])
def update_project(id):
    project = Project.query.get(id)
    if not project:
        return jsonify({'message': 'Project not found!'})
    data = request.get_json()
    project.title = data['title']
    project.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Project updated successfully!'})

# Delete an existing project
@app.route('/projects/<int:id>', methods=['DELETE'])
def delete_project(id):
    project = Project.query.get(id)
    if not project:
        return jsonify({'message': 'Project not found!'})
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)