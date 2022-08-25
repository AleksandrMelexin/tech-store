#from crypt import methods
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.src import base_regestry
from devices.src import devices_registry
from categories.src import categories_registry
from brands.src import brands_registry

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

base_regestry(app)

devices_registry(app)

categories_registry(app)

brands_registry(app)


if __name__ == '__main__':
    app.run(debug=True)