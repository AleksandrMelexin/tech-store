from categories.categories_model import Category
from main import db

class CategoriesService:
    def __init__(self):
        self.Category = Category

    
    def get_all_categories(self):
        categories = self.Category.query.order_by.all()
        return categories

    def create_brand(self, category_title):
        category = self.Category(category_title = category_title)
        try:
            db.session.add(category)
            db.session.commit()
            return True
        except BaseException as err:
            print(err)
            return False