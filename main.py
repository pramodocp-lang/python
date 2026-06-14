from fastapi import FastAPI
from database.connection import Base, engine, SessionLocal
from models.user import User
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    role: str






app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
    
 
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()

    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(db_user)
    db.commit()
    db.close()

    return {
        "message": "User deleted successfully"
    }

@app.put("/users/{user_id}")
def update_user(user_id:int, user:UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id ==user_id).first()
    
    if not db_user:
        db.close()
        
        return HTTPException(
        status_code = 400,
        default = "User Not Found"
        )
    db_user.name = user.name
    db_user.role = user.role
    
    db.commit()
    db.refresh(db_user)
    db.close()
    
    return db_user



 
@app.get("/users")
def get_users():
    db = SessionLocal()
    
    users = db.query(User).all()
    
    result = []
    
    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "role": user.role,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        })
    
    db.close()
    
    return result
    
    
@app.post("/users")
def create_user(user: UserCreate):
    db = SessionLocal()

    existing_user = db.query(User).filter(
            User.name == user.name,
            User.role == user.role
            ).first()
    
    if existing_user:
        db.close()
        return {"message": "User Already exists"}
    
    db_user = User(
        name=user.name,
        role=user.role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    db.close()

    return db_user