from flask import render_template
from users.users_service import UsersService
from auth.auth_middleware import auth_middleware
def users_registry(app):
    users_service = UsersService()

    @app.route('/users')
    @auth_middleware()
    def get_users_page():
        return render_template('index.html')
           
    return app