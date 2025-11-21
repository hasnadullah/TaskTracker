from config.db import users_collection

def create_user(user_data):
    if users_collection.find_one({"email": user_data["email"]}):
        return None
    users_collection.insert_one(user_data)
    return True

def get_user_by_email(email):
    return users_collection.find_one({"email": email})

def get_user_by_id(user_id):
    return users_collection.find_one({"_id": user_id})
