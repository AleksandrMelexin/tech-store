from flask import render_template
from categories.categories_service import CategoriesService

def categories_registry(app):
    categories_service = CategoriesService()

    @app.route('/categories')
    def get_categories_page():
        return render_template('index.html')
           
    return app