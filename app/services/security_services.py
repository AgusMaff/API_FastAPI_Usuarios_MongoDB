from jose import jwt, JWTError

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)