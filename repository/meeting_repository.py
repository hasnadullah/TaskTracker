from config.db import Meetings_collection


def find_all_meetings():
    meetings = list(Meetings_collection.find({}))

    for m in meetings:
        m["_id"] = str(m["_id"])
        m["user_id"] = str(m.get("user_id"))

    return meetings
