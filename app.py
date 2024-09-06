from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key = 'your_secret_key'

db = SQLAlchemy(app)




# Configurez Flask-Migrate
migrate = Migrate(app, db)


# Importez vos modèles ici
from Model import *
from routes import *
print("importation reussie")

# with app.app_context():
#     pass
    # db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5001)




