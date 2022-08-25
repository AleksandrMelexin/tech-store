from main import db
from categories.categories_model import Category

class CategoriesService:
    def __init__(self):
        self.Category = Category

    
    def get_all_categoriess(self):
        categories = self.Category.query.order_by.all()
        return categories

    def create_brand(self, category_title):
        category = self.Item(category_title = category_title)
        try:
            db.session.add(category)
            db.session.commit()
            return True
        except BaseException as err:
            print(err)
            return False