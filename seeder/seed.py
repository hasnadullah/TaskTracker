from config.db import users_collection, tasks_collection, Meetings_collection
from bson.objectid import ObjectId

def seed():
    # Check if admin already exists
    if users_collection.find_one({"email": "admin@skilltrack.com"}):
        print("🌱 Seeder already executed — Admin exists")
        return
    
    # Insert default admin
    users_collection.insert_one({
        "_id": ObjectId(),
        "name": "Super Admin",
        "email": "admin@skilltrack.com",
        "password": "admin123",
        "role": "pseb"
    })

    # Insert default HR
    users_collection.insert_one({
        "_id": ObjectId(),
        "name": "HR Manager",
        "email": "hr@skilltrack.com",
        "password": "hr123",
        "role": "hr"
    })

    # Insert default Mentor
    users_collection.insert_one({
        "_id": ObjectId(),
        "name": "Default Mentor",
        "email": "mentor@skilltrack.com",
        "password": "mentor123",
        "role": "mentor"
    })

    print("🌱 Seeder executed — Default users created")

    if Meetings_collection.count_documents({}) == 0:
        Meetings_collection.insert_many([
            {
                "task_id": None,
                "date": None,
                "time": None,
                "notes": "Sample meeting slot created",
            }
        ])
        print("Meetings seeded successfully")
    print("Database seeded successfully")

    


   
