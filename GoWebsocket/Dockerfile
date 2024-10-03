# Utiliser l'image officielle de Go
FROM golang:1.19-alpine

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers source
COPY main.go ./
COPY go.mod ./

# Installer les dépendances
RUN go mod tidy

# Compiler l'application
RUN go build -o websocket-server .

# Exposer le port pour le serveur
EXPOSE 8080

# Commande pour exécuter l'application
CMD ["./websocket-server"]
