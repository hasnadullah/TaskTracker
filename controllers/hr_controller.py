from repository.hr_repository import get_all_users, get_all_tasks


def get_all_users_controller():
    return get_all_users()


def get_all_tasks_controller():
    return get_all_tasks()
