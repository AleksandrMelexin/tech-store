from main import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    devices = db.relationship('Device', backref='category')
    def __repr__(self):
        return self.category_title
        
