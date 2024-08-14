
from flask import Flask, request, jsonify, redirect, url_for, render_template
# from models import panier, paiment, contact 
from app import *
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)




@app.route('/')
def index():
    return render_template('index.html')

              
              
@app.route('/panier', methods=['GET','POST'])
def panier():
    data = request.json
    cart_items = data.get('cartItems', [])

    if not cart_items:
        return jsonify({'message': 'Le panier est vide'}), 400

    try:
        for item in cart_items:
            produit_id = item['id']
            quantite = item['quantity']

            existing_item = Panier.query.filter_by(produit_id=produit_id).first()
            if existing_item:
                existing_item.quantite += quantite
            else:
                new_item = Panier(produit_id=produit_id, quantite=quantite)
                db.session.add(new_item)

        db.session.commit()
        return jsonify({'message': 'Panier mis à jour avec succès'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Erreur lors de la mise à jour du panier', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)





@app.route('/paiment', methods=['GET','POST'])
def paiment():
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    card_name = request.form.get('card-name')
    card_number = request.form.get('card-number')
    expiry_date = request.form.get('expiry-date')
    cvv = request.form.get('cvv')
    address = request.form.get('address')

    # Créez une instance de PaymentInfo
    payment_info = Paiment(
        first_name=first_name,
        last_name=last_name,
        card_name=card_name,
        card_number=card_number,
        expiry_date=expiry_date,
        cvv=cvv,
        address=address
    )

    # Ajoutez et validez l'information de paiement
    try:
        db.session.add(payment_info)
        db.session.commit()
        return redirect(url_for('payment_success'))  # Redirigez vers une page de succès après l'ajout
    except Exception as e:
        db.session.rollback()
        print(f"Erreur: {e}")
        return redirect(url_for('payment_failure'))  # Redirigez vers une page d'échec en cas d'erreur

@app.route('/payment-success')
def payment_success():
    return "Votre paiement a été enregistré avec succès !"

@app.route('/payment-failure')
def payment_failure():
    return "Une erreur est survenue lors de l'enregistrement du paiement."








@app.route('/contact', methods=['GET','POST'])
def contact():
    phone_number = request.form.get('identifiant')
    full_name = request.form.get('nom')
    email = request.form.get('email')
    message = request.form.get('avis')

    # Créez une instance de ContactInfo
    contact_info = contact(
        phone_number=phone_number,
        full_name=full_name,
        email=email,
        message=message
    )

    # Ajoutez et validez l'information de contact
    try:
        db.session.add(contact_info)
        db.session.commit()
        return redirect(url_for('contact_success'))  # Redirigez vers une page de succès après l'ajout
    except Exception as e:
        db.session.rollback()
        print(f"Erreur: {e}")
        return redirect(url_for('contact_failure'))  # Redirigez vers une page d'échec en cas d'erreur

@app.route('/contact-success')
def contact_success():
    return "Votre message a été envoyé avec succès !"

@app.route('/contact-failure')
def contact_failure():
    return "Une erreur est survenue lors de l'envoi de votre message."





