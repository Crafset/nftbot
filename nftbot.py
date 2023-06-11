import requests

def get_top_cryptos():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        "start": "1",
        "limit": "50",
        "sort": "market_cap",
        "convert": "USD",
        "aux": "num_market_pairs,tags"
    }
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "19cdf6d6-4d5c-4c12-afec-4591e7542d35"
    }
    
    response = requests.get(url, params=parameters, headers=headers)
    data = response.json()

    if "data" in data:
        return data["data"]
    else:
        return None

def filter_cryptos(cryptos):
    filtered_cryptos = []
    
    for crypto in cryptos:
        if crypto["quote"]["USD"]["market_cap"] < 100000000:
            if len(crypto["platform"]) > 0:
                filtered_cryptos.append(crypto)
    
    return filtered_cryptos

def get_cryptos_with_large_wallets(cryptos):
    cryptos_with_large_wallets = []
    
    for crypto in cryptos:
        if crypto["tags"] and "wallet" in crypto["tags"]:
            if crypto["num_market_pairs"] > 1:
                cryptos_with_large_wallets.append(crypto)
    
    return cryptos_with_large_wallets

# Récupération des cryptomonnaies du top 50
cryptos = get_top_cryptos()

if cryptos:
    # Filtrage des cryptomonnaies selon les critères spécifiés
    filtered_cryptos = filter_cryptos(cryptos)

    # Récupération des cryptomonnaies avec plusieurs gros wallets associés
    cryptos_with_large_wallets = get_cryptos_with_large_wallets(filtered_cryptos)

    # Affichage des résultats
    for crypto in cryptos_with_large_wallets:
        print("Nom : ", crypto["name"])
        print("Wallet : ", crypto["platform"]["token_address"])
        print("--------------------------------------")
else:
    print("Erreur lors de la récupération des données.")
