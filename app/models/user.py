from pydantic import BaseModel

class User(BaseModel):
    id:str | None
    username: str
    password: str
    age:int
    mail: str