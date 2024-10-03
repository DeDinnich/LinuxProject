# Utiliser l'image officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requis
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY init_db.py init_db.py

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port de l'application
EXPOSE 5002

# Initialiser la base de données et exécuter l'application
CMD ["sh", "-c", "python init_db.py && python app.py"]
