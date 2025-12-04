from services.hr_service import get_all_users_service, get_all_tasks_service


def get_all_users_controller():
    return get_all_users_service()


def get_all_tasks_controller():
    return get_all_tasks_service()
