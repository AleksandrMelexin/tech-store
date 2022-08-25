from main import db

class Device(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    def __repr__(self):
        return self.device_title




