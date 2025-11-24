from fastapi import FastAPI
from routes import user_routes, task_routes, mentor_routes
from middleware.cors import add_cors
from middleware.error_handler import add_exception_handlers
from seeder.seed import seed
from routes import hr_routes
from routes import pseb_routes


app = FastAPI(title="Internship Task Tracker API")


add_cors(app)
add_exception_handlers(app)


app.include_router(user_routes.router)
app.include_router(task_routes.router)
app.include_router(mentor_routes.router)
app.include_router(hr_routes.router)
app.include_router(pseb_routes.router)


seed()
