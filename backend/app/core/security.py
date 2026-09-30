from datetime import datetime, timedelta, timezone
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from .config import settings
security = HTTPBearer(auto_error=False)
def token_for(email: str, role: str):
    return jwt.encode({'sub': email, 'role': role, 'exp': datetime.now(timezone.utc)+timedelta(hours=12)}, settings.jwt_secret, algorithm='HS256')
def current_user(creds: HTTPAuthorizationCredentials = Depends(security)):
    if not creds: raise HTTPException(401, 'Authentication required')
    try: return jwt.decode(creds.credentials, settings.jwt_secret, algorithms=['HS256'])
    except jwt.PyJWTError: raise HTTPException(401, 'Invalid or expired token')
def require(*roles):
    def check(user=Depends(current_user)):
        if user['role'] not in roles: raise HTTPException(403, 'Insufficient role')
        return user
    return check
