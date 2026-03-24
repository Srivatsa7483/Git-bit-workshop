from flask import Blueprint
from app.controllers import todo_controller

todos_bp = Blueprint('todos', __name__)

todos_bp.route('/', methods=['GET'])(todo_controller.get_all_todos)
todos_bp.route('/<int:todo_id>', methods=['GET'])(todo_controller.get_todo_by_id)
todos_bp.route('/', methods=['POST'])(todo_controller.create_todo)
todos_bp.route('/<int:todo_id>', methods=['PUT'])(todo_controller.update_todo)
todos_bp.route('/<int:todo_id>', methods=['DELETE'])(todo_controller.delete_todo)
