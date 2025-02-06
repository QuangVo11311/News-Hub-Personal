import os


class Config:
    # Thay đổi thông tin kết nối MySQL của bạn
    DB_USERNAME = os.getenv('DB_USERNAME', 'root')  # Username MySQL
    DB_PASSWORD = os.getenv('DB_PASSWORD', '12345')  # Mật khẩu MySQL
    DB_HOST = os.getenv('DB_HOST', 'localhost')  # Địa chỉ server MySQL. Đang sử dụng mặc định là localhost
    DB_NAME = os.getenv('DB_NAME', 'news_personal_db')  # Tên database của bạn

    # Kết nối với MySQL
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Cấu hình JWT cho xác thực API
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'thisisasecretkey')

    # Cấu hình API Key cho dịch vụ tin tức (có thể dùng biến môi trường)
    NEWS_API_KEY = os.getenv('NEWS_API_KEY', 'your_news_api_key_here')
