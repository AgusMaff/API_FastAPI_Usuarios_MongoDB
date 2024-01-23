from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    age:int
    mail: str