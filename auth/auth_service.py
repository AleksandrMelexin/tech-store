from users.users_service import UsersService

class AuthService:
    def __init__(self):
        self.users_service = UsersService()

    
    def login(self, data):
        user = self.users_service.getUserByEmail(data["email"])
        if not user:
            return False
        if data["password"] != user.password:
            return False
        return user

    def registration(self, data):
        user = self.users_service.getUserByEmail(data["email"])
        if user:
            return False
        if not self.users_service.createUser(data["email"], data["password"]):
            return False
        return True
