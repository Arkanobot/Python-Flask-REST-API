from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(320), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"User(name = {self.name}, email = {self.email})"
