from flask import redirect
from functools import wraps
from flask import request

def auth_middleware():
    def _auth_middleware(f):
        @wraps(f)
        def __auth_middleware(*args, **kwargs):
            if not request.cookies.get("email"):
                return redirect("/login")
            return f(*args, **kwargs)
        return __auth_middleware
    return _auth_middleware