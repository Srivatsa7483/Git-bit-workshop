from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Health check
    @app.route('/health')
    def health():
        return {'status': 'OK', 'message': 'Todo API is running'}, 200
    
    return app
