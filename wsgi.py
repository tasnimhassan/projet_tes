from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Créez une instance de l'application Flask
app = Flask(__name__)

# Configurez votre URI de base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Créez une instance de SQLAlchemy
db = SQLAlchemy(app)

# Créez une instance de Flask-Migrate
migrate = Migrate(app, db)

# Importez vos modèles et routes après la configuration
# Cela garantit que les modèles et routes sont importés après la configuration de l'application
from Model import *  # Assurez-vous que ce fichier contient vos modèles
from routes import *  # Assurez-vous que ce fichier contient vos routes

# Exécutez l'application si ce fichier est exécuté directement
if __name__ == '__main__':
    app.run(debug=True, port=5001)
