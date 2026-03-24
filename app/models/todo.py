from datetime import datetime

class TodoModel:
    def __init__(self):
        self.todos = []
        self.next_id = 1
    
    def get_all(self):
        return self.todos
    
    def get_by_id(self, todo_id):
        return next((todo for todo in self.todos if todo['id'] == todo_id), None)
    
    def create(self, title):
        todo = {
            'id': self.next_id,
            'title': title,
            'completed': False,
            'createdAt': datetime.utcnow().isoformat() + 'Z'
        }
        self.todos.append(todo)
        self.next_id += 1
        return todo
    
    def update(self, todo_id, updates):
        todo = self.get_by_id(todo_id)
        if not todo:
            return None
        
        todo.update(updates)
        return todo
    
    def delete(self, todo_id):
        todo = self.get_by_id(todo_id)
        if not todo:
            return False
        
        self.todos.remove(todo)
        return True

# Singleton instance
todo_model = TodoModel()
