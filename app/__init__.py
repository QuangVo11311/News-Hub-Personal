from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

# Khởi tạo SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Khởi tạo database với app
    db.init_app(app)

    # Import và đăng ký các route
    from app.routes import main
    app.register_blueprint(main)

    return app
