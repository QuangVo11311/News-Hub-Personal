from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from config import Config

# Khởi tạo SQLAlchemy
db = SQLAlchemy()

# Khởi tạo Bcrypt và JWTManager
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Khởi tạo database với app
    db.init_app(app)
    bcrypt.init_app(app)  # Khởi tạo bcrypt
    jwt.init_app(app)  # Khởi tạo JWT

    # Import và đăng ký các route
    from app.routes import main
    app.register_blueprint(main)

    return app
