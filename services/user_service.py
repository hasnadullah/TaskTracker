# services/user_service.py
from repository.user_repository import (
    insert_user,
    find_user_by_email,
    find_user_by_id,
    find_all_users as repo_find_all_users
)
from utils.id_converter import convert_object_ids

def create_user_service(user_data):
    if find_user_by_email(user_data["email"]):
        return None

    result = insert_user(user_data)
    user = dict(user_data)
    user["_id"] = str(result.inserted_id)
    return convert_object_ids(user)

def get_user_by_email_service(email):
    user = find_user_by_email(email)
    return convert_object_ids(user)

def get_user_by_id_service(user_id):
    user = find_user_by_id(user_id)
    return convert_object_ids(user)

def get_all_users_service():
    users = repo_find_all_users()
    return convert_object_ids(users)
