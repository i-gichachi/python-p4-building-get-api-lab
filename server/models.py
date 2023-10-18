from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    serialize_rules = ('-baked_goods.bakery',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.String)

    baked_goods = db.relationship('BakedGood', backref='bakery')

    def to_dict(self, nested=False):
        data = super().to_dict()
        if nested:
            data['baked_goods'] = [bg.to_dict(nested=False) for bg in self.baked_goods]
        data['created_at'] = self.created_at  
        return data



class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    serialize_rules = ('-bakery.baked_goods',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.func.now()) 

    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))

    def to_dict(self, nested=False):
        data = super().to_dict()
        if nested:
            data['bakery'] = self.bakery.to_dict(nested=False)
        data['created_at'] = self.created_at  
        return data