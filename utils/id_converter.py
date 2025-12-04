
from bson import ObjectId

def convert_object_ids(data):
    """Recursively convert all ObjectId fields in dict/list."""
    
    if isinstance(data, list):
        return [convert_object_ids(item) for item in data]

    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            if isinstance(value, ObjectId):
                new_dict[key] = str(value)
            else:
                new_dict[key] = convert_object_ids(value)
        return new_dict

    return data
