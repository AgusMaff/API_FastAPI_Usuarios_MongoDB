from fastapi import FastAPI
from app.routers import users

app = FastAPI()
app.include_router(users.router)

#Iniciar el servidor con el comando uvicorn main:app --reload