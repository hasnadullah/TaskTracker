from config.db import users_collection, tasks_collection

def seed():
    if users_collection.count_documents({}) == 0:
        users_collection.insert_many([
            {"name": "HR User", "email": "hr@example.com", "password": "1234", "role": "hr"},
            {"name": "Mentor User", "email": "mentor@example.com", "password": "1234", "role": "mentor"},
            {"name": "Intern User", "email": "intern@example.com", "password": "1234", "role": "intern"},
              {"name": "PSEB User", "email": "pseb@example.com", "password": "1234", "role": "PSEB"}
        ])
    print("Database seeded successfully")
