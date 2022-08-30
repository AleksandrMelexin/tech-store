from flask import render_template, request, redirect, make_response, url_for
from auth.auth_service import AuthService
from utils.response_util import Response

def auth_registry(app):
    auth_service = AuthService()

    @app.get('/login')
    def get_login_page():
        if request.cookies.get("email"):
            return redirect('/')
        return render_template('sign_in.html')

    @app.post('/login')
    def login():
        
        request_data = {"email": request.form['email'], "password": request.form['password']}
        user = auth_service.login(request_data)
        if not user:
            return "Ошибка"
        return Response("").cookies("email", user.email).redirect("/")

    @app.get('/registration')
    def get_registration_page():
        if request.cookies.get("email"):
            return redirect('/')
        return render_template('sign_in.html')

    @app.post('/registration')
    def registration():
        
        request_data = {"email": request.form['email'], "password": request.form['password']}
        if not auth_service.registration(request_data):
            return "Ошибка"
        return Response("").cookies("email", user.email).redirect("/")

    @app.get("/logout")
    def logout():
        return Response("").delete_cookies("email").redirect("/login")
           
    return app