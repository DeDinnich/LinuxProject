import requests

try:
    response = requests.post('http://localhost:8080/notify')
    print(f'Statut de la réponse : {response.status_code}')
    print(f'Contenu de la réponse : {response.text}')
except Exception as e:
    print(f'Erreur lors de l\'envoi de la notification : {e}')

