from flask import render_template, redirect, request
from brands.brand_service import BrandsService

def brands_registry(app):
    brands_service = BrandsService()

    @app.route('/brands')
    def get_brands_page():
        return render_template('index.html')
           
    return app