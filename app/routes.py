from flask import Blueprint
from flask import request, jsonify
from flask_jwt_extended import create_access_token

from app import db, bcrypt
from app.models import User

# Tạo Blueprint cho routes
main = Blueprint('main', __name__)


@main.route('/')
def home():
    return "Chào mừng đến với API Tin tức Cá nhân hóa!"


@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Thiếu thông tin đăng ký!'}), 400

    # Kiểm tra email hoặc username đã tồn tại chưa
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        return jsonify({'message': 'Username hoặc Email đã tồn tại!'}), 400

    # Hash mật khẩu
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Đăng ký thành công!'}), 201


@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Thiếu email hoặc mật khẩu!'}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Email hoặc mật khẩu không đúng!'}), 401

    # Tạo JWT token
    access_token = create_access_token(identity=user.id)
    return jsonify({'message': 'Đăng nhập thành công!', 'access_token': access_token}), 200
