from brands.brand_model import Brand
from main import db

class BrandsService:
    def __init__(self):
        self.Brand = Brand

    
    def get_all_brands(self):
        brands = self.Brand.query.order_by.all()
        return brands

    def create_brand(self, brand_title):
        brand = self.Brand(brand_title = brand_title)
        try:
            db.session.add(brand)
            db.session.commit()
            return True
        except BaseException as err:
            print(err)
            return False