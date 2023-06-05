import requests
import json
import time

# Remplacez les valeurs suivantes par vos propres informations
BITGET_API_KEY = "YOUR_BITGET_API_KEY"
BITGET_API_SECRET = "YOUR_BITGET_API_SECRET"
DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

def send_discord_embed(name, rewards, farming_period):
    data = {
        "embeds": [
            {
                "title": name,
                "description": f"Total des récompenses : {rewards}\nPériode de farming : {farming_period}"
            }
        ]
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(data), headers=headers)
    if response.status_code != 204:
        print("Erreur lors de l'envoi du message Discord :", response.text)

def check_new_launchpools():
    url = "https://api.bitget.com/api/v1/launchpools"
    response = requests.get(url)
    if response.status_code == 200:
        launchpools = response.json()["data"]
        # Vérifiez si un nouveau launchpool a été ajouté
        # Vous pouvez mettre en place une logique personnalisée ici selon votre besoin
        # Dans cet exemple, nous vérifions simplement si le nombre total de launchpools a augmenté
        num_launchpools = len(launchpools)
        if num_launchpools > check_new_launchpools.last_num_launchpools:
            new_launchpool = launchpools[num_launchpools - 1]  # Récupère le dernier launchpool ajouté
            name = new_launchpool["name"]
            rewards = new_launchpool["totalRewards"]
            farming_period = new_launchpool["farmingPeriod"]
            send_discord_embed(name, rewards, farming_period)
        check_new_launchpools.last_num_launchpools = num_launchpools
    else:
        print("Erreur lors de la requête Bitget :", response.text)

# Initialisez la variable statique pour garder une trace du nombre de launchpools
check_new_launchpools.last_num_launchpools = 0

# Exécutez la vérification toutes les 10 secondes (modifiable selon vos besoins)
while True:
    check_new_launchpools()
    time.sleep(10)
