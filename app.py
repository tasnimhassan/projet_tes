from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
app.secret_key = 'your_secret_key'

db = SQLAlchemy(app)

from routes import *

with app.app_context():
    db.create_all()



    
if __name__ == '__main':
    app.run(debug=True)

