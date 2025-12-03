from repository.user_repository import (
    insert_user,
    find_user_by_email,
    find_user_by_id
)


def create_user(user_data):
    if find_user_by_email(user_data["email"]):
        return None
    insert_user(user_data)
    return True


def get_user_by_email(email):
    return find_user_by_email(email)


def get_user_by_id(user_id):
    return find_user_by_id(user_id)
