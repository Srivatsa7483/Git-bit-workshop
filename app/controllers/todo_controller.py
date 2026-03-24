from flask import request, jsonify
from app.models import todo_model

def get_all_todos():
    todos = todo_model.get_all()
    return jsonify({'success': True, 'data': todos}), 200

def get_todo_by_id(todo_id):
    todo = todo_model.get_by_id(todo_id)
    if not todo:
        return jsonify({'success': False, 'error': 'Todo not found'}), 404
    return jsonify({'success': True, 'data': todo}), 200

def create_todo():
    data = request.get_json()
    title = data.get('title', '').strip()
    
    if not title:
        return jsonify({'success': False, 'error': 'Title is required'}), 400
    
    todo = todo_model.create(title)
    return jsonify({'success': True, 'data': todo}), 201

def update_todo(todo_id):
    updates = request.get_json()
    todo = todo_model.update(todo_id, updates)
    
    if not todo:
        return jsonify({'success': False, 'error': 'Todo not found'}), 404
    
    return jsonify({'success': True, 'data': todo}), 200

def delete_todo(todo_id):
    deleted = todo_model.delete(todo_id)
    
    if not deleted:
        return jsonify({'success': False, 'error': 'Todo not found'}), 404
    
    return jsonify({'success': True, 'message': 'Todo deleted'}), 200
