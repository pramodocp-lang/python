from database import SessionLocal
from models import User

class UserService:

    @staticmethod
    def create_user(name, role):
        db = SessionLocal()
        user = User(name=name, role=role)
        db.add(user)
        db.commit()
        db.refresh(user)
        db.close()
        return user

    @staticmethod
    def get_users():
        db = SessionLocal()
        users = db.query(User).all()
        db.close()
        return users