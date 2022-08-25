from main import db

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    brand_title = db.Column(db.String(100), nullable = False)
    def __repr__(self):
        return self.brand_title
        