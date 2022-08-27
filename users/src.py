from flask import render_template
from users.users_service import UsersService

def users_registry(app):
    users_service = UsersService()

    @app.route('/users')
    def get_users_page():
        return render_template('index.html')
           
    return app