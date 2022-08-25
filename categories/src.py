from flask import render_template, redirect, request
from categories.categories_service import CategoriesService

def categories_registry(app):
    categories_service = CategoriesService()

    @app.route('/categories')
    def device(id):
        return render_template('index.html')
           
    return app