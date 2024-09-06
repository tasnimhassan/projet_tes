from wsgi import db, app

# Crée les tables dans la base de données
with app.app_context():
    db.create_all()
