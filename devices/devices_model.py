from main import db

class Device(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    device_title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = False)
    category_id = db.Column(db.Integer, nullable = False)
    brand_id = db.Column(db.Integer, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    def __repr__(self):
        return self.device_title




