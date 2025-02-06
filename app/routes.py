from flask import Blueprint

# Tạo Blueprint cho routes
main = Blueprint('main', __name__)


@main.route('/')
def home():
    return "Chào mừng đến với API Tin tức Cá nhân hóa!"


@main.route('/register')
def register():
    pass


@main.route('/login')
def login():
    pass
