from sqlalchemy import column ,Integer,String
from flask_sqlalchemy import SQLAlchemy
from app import db

db= SQLAlchemy()

class panier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produit_id = db.Column(db.Integer, nullable=False)
    quantite = db.Column(db.Integer, nullable=False)




# paiement
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

class paiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    card_name = db.Column(db.String(100), nullable=False)
    card_number = db.Column(db.String(16), nullable=False)
    expiry_date = db.Column(db.String(7), nullable=False)
    cvv = db.Column(db.String(4), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<paiment{self.id}>'






# contact
#  from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

class contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(20), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<contact {self.id}>'       
        
   




