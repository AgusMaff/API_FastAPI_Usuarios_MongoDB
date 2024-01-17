from fastapi import APIRouter, HTTPException, status, Depends 
from app.services import user_services
from app.models.user import User

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user:User):
    if(user_services.search_user(user.username)):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Ya existe el usuario especificado")
    else:
        new_user: User = user_services.insert_user(user)
        return new_user 
    

