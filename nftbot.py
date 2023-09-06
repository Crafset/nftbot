import requests

# Nom de la cryptomonnaie
crypto = "uniswap"

# Fonction pour obtenir la liste des exchanges avec les prix de la cryptomonnaie UNI
def get_exchange_prices(crypto):
    url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={crypto}"
    response = requests.get(url)
    data = response.json()
    return data

# Obtention de la liste des exchanges avec les prix de UNI
exchange_data = get_exchange_prices(crypto)

if len(exchange_data) > 0:
    # Recherche du prix le plus bas et le plus élevé
    lowest_price_exchange = min(exchange_data, key=lambda x: x["current_price"])
    highest_price_exchange = max(exchange_data, key=lambda x: x["current_price"])

    # Affichage des résultats
    print(f"Crypto: {crypto}")
    print(f"Prix le plus bas sur {lowest_price_exchange['name']}: {lowest_price_exchange['current_price']} USD")
    print(f"Prix le plus élevé sur {highest_price_exchange['name']}: {highest_price_exchange['current_price']} USD")
else:
    print(f"Impossible de trouver des données pour {crypto}")

