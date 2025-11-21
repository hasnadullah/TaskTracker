from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from .jwt_handler import decode_access_token

class JWTBearer(HTTPBearer):
    def __init__(self, roles: list = []):
        super(JWTBearer, self).__init__()
        self.roles = roles

    async def __call__(self, request: Request):
        credentials = await super(JWTBearer, self).__call__(request)
        token = credentials.credentials
        payload = decode_access_token(token)
        if payload is None:
            raise HTTPException(status_code=403, detail="Invalid token")
        if self.roles and payload.get("role") not in self.roles:
            raise HTTPException(status_code=403, detail="Not authorized for this role")
        return payload
