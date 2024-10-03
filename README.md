# LinuxProject
## IW 3 - Projet Multi Webapp

### Sommaire
1. [Introduction](#introduction)
2. [Technologies Utilisées](#technologies-utilisées)
3. [Étapes de Développement](#étapes-de-développement)
4. [Installation et Configuration](#installation-et-configuration)
5. [Utilisation](#utilisation)
6. [Étapes et Difficultés Rencontrées](#étapes-et-difficultés-rencontrées)
7. [Conclusion](#conclusion)

### Introduction
Ce projet consiste en une application web multiservice développée avec plusieurs technologies modernes. L'application permet la gestion d'articles via une API Flask, l'utilisation de WebSockets pour les notifications en temps réel, et un reverse proxy Nginx pour gérer les requêtes. L'objectif est de démontrer l'intégration de ces technologies pour créer une application réactive et performante.

### Technologies Utilisées
- **Flask** : Framework web pour le développement de l'API.
- **Flask-SQLAlchemy** : ORM pour la gestion de la base de données SQLite.
- **Flask-Migrate** : Outil pour gérer les migrations de base de données.
- **Flask-CORS** : Pour gérer les politiques de partage de ressources entre origines.
- **Go** : Pour le service WebSocket.
- **Nginx** : Serveur web et reverse proxy.
- **Docker** : Pour la conteneurisation des services.
- **HTML/CSS/JavaScript** : Pour le développement de l'interface utilisateur.

### Étapes de Développement
1. **Création de l'API Flask** : Initialisation de Flask, configuration de la base de données, et développement des endpoints pour la gestion des articles.
2. **Développement du WebSocket en Go** : Mise en place d'un serveur WebSocket pour les notifications en temps réel.
3. **Configuration du Reverse Proxy avec Nginx** : Rédaction de la configuration Nginx pour gérer les requêtes vers l'API et le WebSocket.
4. **Développement de l'Interface Web** : Création d'une interface simple pour afficher et gérer les articles.
5. **Dockerisation des Services** : Création de Dockerfiles et utilisation de Docker Compose pour orchestrer les services.
6. **Tests et Débogage** : Vérification des fonctionnalités et résolution des problèmes rencontrés.

### Installation et Configuration
1. Clonez le dépôt :
   ```bash
   git clone git@github.com:DeDinnich/LinuxProject.git
   cd LinuxProject