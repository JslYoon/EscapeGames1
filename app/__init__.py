from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Routes.GamePlay import users_bp
from Routes.Error import error_bp

# Initialize the database
# db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(error_bp)
    app.register_blueprint(users_bp)
    return app

