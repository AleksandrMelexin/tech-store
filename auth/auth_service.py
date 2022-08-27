from users.users_service import UsersService

class AuthService:
    def __init__(self):
        self.users_service = UsersService()

    
    def login(self, email, password):
        user = self.users_service.getUserByEmail(email)
        if not user:
            return False
        if password != user.password:
            return False
        return user

    def registration(self, email, password):
        user = self.users_service.getUserByEmail(email)
        if user:
            return False
        if not self.users_service.createUser(email, password):
            return False
        return True


    """ def create_brand(self, category_title):
        category = self.Category(category_title = category_title)
        try:
            db.session.add(category)
            db.session.commit()
            return True
        except BaseException as err:
            print(err)
            return False """