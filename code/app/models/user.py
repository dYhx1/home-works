from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "user"  # Це на дз
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(320), unique=True)
    created_at = db.Column(db.Date, default=datetime.now())

    posts = db.relationship("post", back_populates="user", cascade="all")
