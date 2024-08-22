from flask import Flask, request, jsonify, redirect, url_for, render_template,flash,session



from Model import Panier
from Model import Paiment
from Model import Contact



from app import *
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)
with app.app_context():
    db.create_all()






    




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produit')
def produit():
    return render_template('produit.html')    


@app.route('/panier', methods=['GET', 'POST'])
def panier():
    if request.method == 'POST':
        produit_id = request.form['robe']
        quantite= request.form['nombre']

         # Création d'un nouvel objet objet
        nouveau_panier = Panier(produit_id=produit_id , quantite=quantite)

        # Ajouter et sauvegarder dans la base de données
        db.session.add(nouveau_panier)
        db.session.commit()

        return redirect(url_for('panier'))
    
    return render_template('panier.html')


        





@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        phone_number = request.form['identifiant']
        full_name= request.form['nom']
        email = request.form['email']
        message= request.form['avis']

        # Création d'un nouvel objet Contact
        nouveau_contact = Contact(phone_number=phone_number, full_name=full_name, email=email, message=message)

        # Ajouter et sauvegarder dans la base de données
        db.session.add(nouveau_contact)
        db.session.commit()

        return redirect(url_for('contact'))
    
    return render_template('contact.html')




@app.route('/paiment', methods=['GET', 'POST'])
def paiment():
    if request.method == "POST":
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        card_name = request.form['card-name']
        card_number = request.form['card-number']
        expiry_date = request.form['expiry-date']
        cvv = request.form['cvv']
        address = request.form['address']

        # Création d'un nouvel objet paiment
        nouveau_paiment =Paiment(first_name=first_name, last_name=last_name, card_name=card_name, card_number=card_number, expiry_date=expiry_date, cvv=cvv, address=address)

        # Ajouter et sauvegarder dans la base de données
        db.session.add(nouveau_paiment)
        db.session.commit()

        return redirect(url_for('paiment'))
    
    return render_template('paiment.html')    



if __name__ == '__main__':
    app.run(debug=True)




