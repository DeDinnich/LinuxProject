from app import app, db

# Créer le contexte de l'application
with app.app_context():
    # Créer les tables dans la base de données
    db.create_all()
