from database.connection import SessionLocal
from models.user import User

class UserService:

    @staticmethod
    def create_user(name, role):
        db = SessionLocal()
        try:
            user = User(name=name, role=role)
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        finally:
            db.close()

    @staticmethod
    def get_users():
        db = SessionLocal()
        try:
            return db.query(User).all()
        finally:
            db.close()