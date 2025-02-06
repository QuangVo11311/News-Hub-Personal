from datetime import datetime

from app import db, create_app


# Bảng User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Quan hệ với NewsPreference & SavedArticle
    preferences = db.relationship('NewsPreference', backref='user', lazy=True)
    saved_articles = db.relationship('SavedArticle', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


# Bảng NewsPreference (Sở thích tin tức của user)
class NewsPreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # Ví dụ: 'technology', 'sports', 'business'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"NewsPreference('{self.user_id}', '{self.category}')"


# Bảng SavedArticle (Bài báo đã lưu của user)
class SavedArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"SavedArticle('{self.user_id}', '{self.title}')"


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()