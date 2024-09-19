from sqlalchemy import column ,Integer,String
from flask_sqlalchemy import SQLAlchemy



db= SQLAlchemy()

class Panier(db.Model):
    __tablename__ = 'panier'
    id =db.Column(db.Integer, primary_key=True)
    produit_id = db.Column(db.String, nullable=False)
    quantite = db.Column(db.String, nullable=False)

    def __init__(self, produit_id, quantite):
        self.produit_id =produit_id
        self.quantite =quantite





class Paiment(db.Model):
    __tablename__ = 'paiment'
    
    id =db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    card_name = db.Column(db.String(100), nullable=False)
    card_number = db.Column(db.String(16), primary_key=True)
    expiry_date = db.Column(db.String(7), nullable=False)
    cvv = db.Column(db.String(4), nullable=False)
    address = db.Column(db.String(255), nullable=False)
   

    def __init__(self, first_name, last_name, card_name, card_number, expiry_date, cvv, address):
        self.first_name =first_name
        self.last_name = last_name
        self.card_name = card_name
        self.card_number = card_number 
        self.expiry_date = expiry_date  
        self.cvv = cvv  
        self.address = address        






 


class Contact(db.Model):
    __tablename__ = 'contact'
    
    id =db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(20), nullable=False)
    full_name= db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message= db.Column(db.Text, nullable=False)

    def __init__(self, phone_number, full_name, email, message):
        self.phone_number =phone_number
        self.full_name = full_name
        self.email = email
        self.message = message

class User(db.Model):
    __tablename__ = 'User'
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), nullable=False)
    password=db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<User{self.id}>'
    


      


   




