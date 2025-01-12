from app import db
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False, unique=True
    )
    text = db.Column(db.String, nullable=True)
    date = db.Column(db.Date, default=datetime.now(), nullable=False)

    user = db.relationship("User", back_populates="Post")