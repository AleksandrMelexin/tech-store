from main import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    category_title = db.Column(db.String(100), nullable = False)
    def __repr__(self):
        return self.category_title
        
