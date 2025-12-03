from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from auth.jwt_handler import decode_access_token as decodeJWT

class AuthTokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        excluded_routes = [
            "/auth/login",
            "/auth/register",
            "/docs",
            "/openapi.json"
        ]
        
        if request.url.path in excluded_routes:
            return await call_next(request)

        token = request.headers.get("Authorization")

        if not token:
            return Response("Missing Authorization Token", status_code=401)

        token = token.replace("Bearer ", "")

        try:
            decodeJWT(token)  # validate token
        except:
            return Response("Invalid or Expired Token", status_code=401)

        return await call_next(request)
