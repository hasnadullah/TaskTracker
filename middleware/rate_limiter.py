import time
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

RATE_LIMIT = 100  # number of requests allowed
WINDOW_SIZE = 60  # seconds

client_requests = {}

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        
        current_time = time.time()
        request_log = client_requests.get(client_ip, [])

        # purani requests clear karo
        request_log = [timestamp for timestamp in request_log if current_time - timestamp < WINDOW_SIZE]
        client_requests[client_ip] = request_log

        # agar limit exceed ho jaye
        if len(request_log) >= RATE_LIMIT:
            return Response(
                content="Too Many Requests. Try again later.",
                status_code=429
            )

        # new request ko log karo
        request_log.append(current_time)
        client_requests[client_ip] = request_log

        response = await call_next(request)
        return response
