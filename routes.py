
from flask import Flask, request, jsonify, redirect, url_for
from models import db, panier, paiment, contact 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

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



# from flask import Flask, request, redirect, url_for
# from models import db, PaymentInfo  

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)

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






# contact

# from flask import Flask, request, redirect, url_for
# from models import db, ContactInfo  

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)

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




# from flask import Flask
# from models import db
# from panier import panier_blueprint
# from paiement import paiement_blueprint
# from contact import contact_blueprint

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)

# app.register_blueprint(panier_blueprint)
# app.register_blueprint(paiement_blueprint)
# app.register_blueprint(contact_blueprint)

# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Blueprint, request, jsonify
# from models import db, Panier

# panier_blueprint = Blueprint('panier', __name__)

# @panier_blueprint.route('/panier', methods=['POST'])
# def ajouter_au_panier():
#     data = request.json
#     cart_items = data.get('cartItems', [])

#     if not cart_items:
#         return jsonify({'message': 'Le panier est vide'}), 400

#     try:
#         for item in cart_items:
#             produit_id = item['id']
#             quantite = item['quantity']

#             existing_item = Panier.query.filter_by(produit_id=produit_id).first()
#             if existing_item:
#                 existing_item.quantite += quantite
#             else:
#                 new_item = Panier(produit_id=produit_id, quantite=quantite)
#                 db.session.add(new_item)

#         db.session.commit()
#         return jsonify({'message': 'Panier mis à jour avec succès'}), 200

#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'message': 'Erreur lors de la mise à jour du panier', 'error': str(e)}), 500







# from flask import Blueprint, request, redirect, url_for
# from models import db, PaymentInfo

# paiement_blueprint = Blueprint('paiement', __name__)

# @paiement_blueprint.route('/payment', methods=['POST'])
# def payment():
#     first_name = request.form.get('first-name')
#     last_name = request.form.get('last-name')
#     card_name = request.form.get('card-name')
#     card_number = request.form.get('card-number')
#     expiry_date = request.form.get('expiry-date')
#     cvv = request.form.get('cvv')
#     address = request.form.get('address')

#     payment_info = PaymentInfo(
#         first_name=first_name,
#         last_name=last_name,
#         card_name=card_name,
#         card_number=card_number,
#         expiry_date=expiry_date,
#         cvv=cvv,
#         address=address
#     )

#     try:
#         db.session.add(payment_info)
#         db.session.commit()
#         return redirect(url_for('paiement.payment_success'))
#     except Exception as e:
#         db.session.rollback()
#         print(f"Erreur: {e}")
#         return redirect(url_for('paiement.payment_failure'))

# @paiement_blueprint.route('/payment-success')
# def payment_success():
#     return "Votre paiement a été enregistré avec succès !"

# @paiement_blueprint.route('/payment-failure')
# def payment_failure():
#     return "Une erreur est survenue lors de l'enregistrement du paiement."







# from flask import Blueprint, request, redirect, url_for
# from models import db, ContactInfo

# contact_blueprint = Blueprint('contact', __name__)

# @contact_blueprint.route('/contact', methods=['POST'])
# def contact():
#     phone_number = request.form.get('identifiant')
#     full_name = request.form.get('nom')
#     email = request.form.get('email')
#     message = request.form.get('avis')

#     contact_info = ContactInfo(
#         phone_number=phone_number,
#         full_name=full_name,
#         email=email,
#         message=message
#     )

#     try:
#         db.session.add(contact_info)
#         db.session.commit()
#         return redirect(url_for('contact.contact_success'))
#     except Exception as e:
#         db.session.rollback()
#         print(f"Erreur: {e}")
#         return redirect(url_for('contact.contact_failure'))

# @contact_blueprint.route('/contact-success')
# def contact_success():
#     return "Votre message a été envoyé avec succès !"

# @contact_blueprint.route('/contact-failure')
# def contact_failure():
#     return "Une erreur est survenue lors de l'envoi de votre message."
