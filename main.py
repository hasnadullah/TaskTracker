from fastapi import FastAPI
from routes import user_routes, task_routes, mentor_routes
from middleware.cors import add_cors
from middleware.error_handler import add_exception_handlers
from seeder.seed import seed

app = FastAPI(title="Internship Task Tracker API")

# Middleware
add_cors(app)
add_exception_handlers(app)

# Include Routes
app.include_router(user_routes.router)
app.include_router(task_routes.router)
app.include_router(mentor_routes.router)

# Seed DB
seed()
