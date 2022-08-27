from users.users_model import User
from main import db

class UsersService:
    def __init__(self):
        self.User = User

    
    def getAllUsers(self):
        users = self.User.query.all()
        return users

    def getUserByEmail(self, email):
        try:
            user = self.User.query.filter(User.email == email).one()
            return user
        except:
            return False

    def createUser(self, email, password):
        user = self.User(email = email, password = password)
        try:
            db.session.add(user)
            db.session.commit()
            return True
        except BaseException as err:
            print(err)
            return False
    """ def create_brand(self, category_title):
        category = self.Category(category_title = category_title)
        try:
            db.session.add(category)
            db.session.commit()
            return True
        except BaseException as err:
            print(err)
            return False """