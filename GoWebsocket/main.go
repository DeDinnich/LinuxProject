package main

import (
	"github.com/gorilla/websocket"
	"log"
	"net/http"
)

// Variable pour l'upgrader WebSocket
var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		return true
	},
}

// Clients WebSocket connectés
var clients = make(map[*websocket.Conn]bool)

// Handler pour les connexions WebSocket
func handleWebSocket(w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Println(err)
		return
	}
	defer conn.Close()
	clients[conn] = true

	for {
		_, message, err := conn.ReadMessage()
		if err != nil {
			log.Println("Erreur WebSocket:", err)
			delete(clients, conn)
			break
		}
		log.Printf("Message reçu : %s", message)
	}
}

// Fonction pour notifier tous les clients WebSocket
func notifyClients() {
	for client := range clients {
		err := client.WriteMessage(websocket.TextMessage, []byte("Nouveau message reçu"))
		if err != nil {
			log.Println("Erreur lors de l'envoi du message :", err)
			client.Close()
			delete(clients, client)
		}
	}
}

// Endpoint HTTP pour recevoir les notifications de Flask
func notifyHandler(w http.ResponseWriter, r *http.Request) {
	log.Println("Notification reçue de Flask")
	notifyClients() // Notifie tous les clients WebSocket
}

func main() {
	http.HandleFunc("/ws/", handleWebSocket)     // Endpoint pour WebSocket
	http.HandleFunc("/notify", notifyHandler)    // Endpoint pour les notifications Flask
	log.Fatal(http.ListenAndServe(":8080", nil)) // Lancer le serveur sur le port 8080
}
