from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Register blueprints
    from app.routes.todos import todos_bp
    app.register_blueprint(todos_bp, url_prefix='/api/todos')
    
    # Health check
    @app.route('/health')
    def health():
        return jsonify({'status': 'OK', 'message': 'Todo API is running'}), 200
    
    # 404 handler
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'success': False, 'error': 'Route not found'}), 404
    
    return app
