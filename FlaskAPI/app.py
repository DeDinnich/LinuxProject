import os
import requests
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS  # Importer CORS pour gérer les politiques de partage de ressources

# Initialisation de l'application Flask
app = Flask(__name__)

# Activer CORS pour toutes les routes
CORS(app)

# Configuration de la base de données SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de la base de données et des migrations
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modèle d'articles
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Identifiant unique de l'article
    title = db.Column(db.String(120), nullable=False)  # Titre de l'article, requis

# Endpoint pour récupérer tous les articles
@app.route('/api/articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()  # Récupérer tous les articles de la base de données
    articles_list = [{"id": article.id, "title": article.title} for article in articles]
    return jsonify(articles_list)  # Retourner la liste d'articles au format JSON

# Endpoint pour ajouter un nouvel article
@app.route('/api/articles', methods=['POST'])
def add_article():
    new_article_data = request.json  # Récupérer les données de l'article depuis la requête
    new_article = Article(title=new_article_data['title'])  # Créer un nouvel objet Article
    db.session.add(new_article)  # Ajouter l'article à la session
    db.session.commit()  # Enregistrer les changements dans la base de données
    
    # Notifie le serveur WebSocket après un ajout
    try:
        requests.post('http://go-websocket:8080/notify')  # Utiliser le nom du service ici
    except Exception as e:
        print(f"Erreur lors de l'envoi de la notification WebSocket: {e}")
    
    return jsonify({"id": new_article.id, "title": new_article.title}), 201  # Retourner l'article ajouté

# Exécution de l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)  # Lancer l'application sur le port 5002