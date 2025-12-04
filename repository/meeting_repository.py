# repository/meeting_repository.py
from config.db import Meetings_collection

def find_all_meetings():
    return list(Meetings_collection.find({}))
