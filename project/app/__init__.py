from flask import Flask
from .users.views import users_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(users_bp, url_prefix="/users")
    return app
