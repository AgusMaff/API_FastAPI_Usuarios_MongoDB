def user_schema(user_json) -> dict:
    return {"id": str(user_json["_id"]),
            "username": user_json["username"],
            "password": user_json["password"],
            "age": user_json["age"],
            "mail":user_json["mail"]}