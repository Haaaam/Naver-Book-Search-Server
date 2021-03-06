from Bookbot import db

class MovieRank(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200),nullable=False)

class ItemBuy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    lprice=db.Column(db.String(200),nullable=False)
    address=db.Column(db.String(200),nullable=False)
    buy_date=db.Column(db.DateTime(),nullable=False)