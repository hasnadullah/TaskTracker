import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        start_time = time.time()
        method = request.method
        path = request.url.path
        client_ip = request.client.host

        print(f"[LOG] Incoming request: {method} {path} from {client_ip}")

        response = await call_next(request)

        duration = time.time() - start_time
        print(f"[LOG] Completed {method} {path} in {duration:.2f}s with {response.status_code}")

        return response
