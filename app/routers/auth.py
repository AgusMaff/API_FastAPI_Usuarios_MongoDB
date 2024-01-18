from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.services.user_services import search_user
from app.services.security_services import create_jwt_token

router = APIRouter(prefix="/auth", tags=["auth"])
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/sign_in", response_model = dict, status_code=status.HTTP_202_ACCEPTED)
async def sign_in_user(form_data: OAuth2PasswordRequestForm = Depends()):
    if not search_user(form_data.username, form_data.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Nombre de usuario y/o la constraseña son incorrectas")
    
    token = create_jwt_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}