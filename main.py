#from crypt import methods
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.src import base_regestry
from devices.src import devices_registry
from categories.src import categories_registry
from brands.src import brands_registry
from users.src import users_registry
from auth.src import auth_registry

users_registry(app)

auth_registry(app)

base_regestry(app)

devices_registry(app)

categories_registry(app)

brands_registry(app)




if __name__ == '__main__':
    app.run(debug=True)