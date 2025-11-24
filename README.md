# Internship Task Tracker API

A FastAPI-based Internship Task Tracker system with MongoDB, JWT authentication, CRUD operations, middleware, CORS, and database seeding.
This project allows **interns, mentors, and HR** to manage internship tasks efficiently. The frontend is not included.

---

## **Features**

* JWT-based authentication with role-based access (`intern`, `mentor`, `hr`)
* CRUD operations for tasks
* Mentor feedback on intern tasks
* Middleware for CORS and error handling
* Database seeding with default users
* Positive and negative flow handling
* Debug-friendly structure
* Fully modular: controllers, services, routes, models, middleware

---

## **Project Structure**

```
internship_task_tracker/
│── app/
│   ├── main.py
│   ├── config/
│   │   └── db.py
│   ├── auth/
│   │   ├── jwt_handler.py
│   │   └── jwt_bearer.py
│   ├── middleware/
│   │   ├── cors.py
│   │   └── error_handler.py
│   ├── models/
│   │   ├── user_model.py
│   │   └── task_model.py
│   ├── schemas/
│   │   ├── user_schema.py
│   │   └── task_schema.py
│   ├── controllers/
│   │   ├── user_controller.py
│   │   ├── task_controller.py
│   │   └── mentor_controller.py
│   ├── routes/
│   │   ├── user_routes.py
│   │   ├── task_routes.py
│   │   └── mentor_routes.py
│   ├── services/
│   │   ├── user_service.py
│   │   └── task_service.py
│   └── seeder/
│       └── seed.py
└── requirements.txt
```

---

## **Installation**

1. Clone the repository:

```bash
git clone <repository_url>
cd internship_task_tracker
```

2. Create a virtual environment:

```bash
python -m venv Project2
Project2\Scripts\activate  # Windows
# OR
source Project2/bin/activate  # Linux/macOS
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
uvicorn app.main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

---

## **Usage**

### Auth Routes

* **POST /auth/signup** — Register a new user
* **POST /auth/login** — Login and get JWT token
* **GET /auth/me** — Get current user info

### Task Routes (Intern)

* **POST /tasks/create** — Create a new task
* **GET /tasks/my** — Get my tasks
* **PUT /tasks/update/{task_id}** — Update a task
* **DELETE /tasks/delete/{task_id}** — Delete a task

### Mentor Routes

* **GET /mentor/tasks** — Get all intern tasks
* **POST /mentor/tasks/{task_id}/feedback** — Add feedback to a task

---

## **Environment Variables**

Optional: Create a `.env` file for custom settings:

```
MONGO_URI=mongodb://localhost:27017
SECRET_KEY=your_jwt_secret
```

---

## **Database Seeding**

Default users are created on first run:

| Name        | Email                                           | Password | Role   |
| ----------- | ----------------------------------------------- | -------- | ------ |
| HR User     | [hr@example.com](mailto:hr@example.com)         | 1234     | hr     |
| Mentor User | [mentor@example.com](mailto:mentor@example.com) | 1234     | mentor |
| Intern User | [intern@example.com](mailto:intern@example.com) | 1234     | intern |

---

## **Dependencies**

* fastapi
* uvicorn
* pymongo
* python-jose
* python-multipart
* email-validator
* passlib[bcrypt]
* python-dotenv

---

## **Contributing**

1. Fork the repository
2. Create a branch for your feature: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature"`
4. Push to branch: `git push origin feature-name`
5. Create a pull request

---

## **License**

MIT License © 2025
