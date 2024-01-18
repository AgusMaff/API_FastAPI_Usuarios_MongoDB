from app.models.user import User
from app.db.database import db_client
import app.db.schemas 

def search_user(username: str, password:str) -> bool:
    user_document = db_client.local.users.find_one({"username": username, "password": password})
    return user_document is not None
    
def insert_user(user: User) -> User:
    user_json = dict(user)
    id = db_client.local.users.insert_one(user_json).inserted_id
    new_user = app.db.schemas.user_schema(db_client.local.users.find_one({"_id":id}))
    return User(**new_user)