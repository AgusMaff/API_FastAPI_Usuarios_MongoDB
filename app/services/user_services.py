from app.models.user import User
from app.db.database import db_client
import app.db.schemas 

def search_user(user: str) -> bool:
    if(db_client.local.users.find_one({"username":user}) != None):
        return True
    else:
        return False
    
def insert_user(user: User) -> User:
    user_json = dict(user)
    del user_json["id"]
    id = db_client.local.users.insert_one(user_json).inserted_id
    new_user = app.db.schemas.user_schema(db_client.local.users.find_one({"_id":id}))
    return User(**new_user)