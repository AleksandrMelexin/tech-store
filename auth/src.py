from flask import render_template, request, redirect, make_response, url_for
from auth.auth_service import AuthService

def auth_registry(app):
    auth_service = AuthService()

    @app.get('/login')
    def get_login_page():
        return render_template('sign_in.html')

    @app.post('/login')
    def login():
        email = request.form['email']
        password = request.form['password']
        user = auth_service.login(email, password)
        if not user:
            return "Ошибка"
        res = make_response()
        res.set_cookie("user", value=user.id)
        res.headers['location'] = url_for('index') 
        return res, 302

    @app.get('/registration')
    def get_registration_page():
        return render_template('sign_in.html')

    @app.post('/registration')
    def registration():
        email = request.form['email']
        password = request.form['password']
        if not auth_service.registration(email, password):
            return "Ошибка"
        return redirect('/')
           
    return app