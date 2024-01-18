from fastapi import FastAPI
from app.routers import users, auth

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)

#Iniciar el servidor con el comando uvicorn main:app --reload