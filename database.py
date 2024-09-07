from app import db
from models import UserModel


def create_db():
    db.create_all()


if __name__ == "__main__":
    create_db()
