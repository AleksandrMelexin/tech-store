from main import db

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    devices = db.relationship('Device', backref='brand')
    def __repr__(self):
        return self.brand_title
        