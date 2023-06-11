import requests

def get_top_cryptos():
    # Appel à l'API CoinMarketCap pour récupérer les informations sur le top 50 des cryptomonnaies
    url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=50&sortBy=market_cap&sortType=asc&convert=USD&cryptoType=all&tagType=all"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data["data"]["cryptoCurrencyList"]

    return None

def get_wallets(crypto_id):
    # Appel à l'API CoinMarketCap pour récupérer les informations sur les portefeuilles d'une cryptomonnaie
    url = f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/wallets/rankings/latest?id={crypto_id}&start=1&limit=100&score=market_cap"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data["data"]["cryptoCurrency"]["wallets"]

    return None

def print_wallets():
    top_cryptos = get_top_cryptos()

    if top_cryptos is not None:
        for crypto in top_cryptos:
            if crypto["marketCap"] < 100_000_000:
                crypto_id = crypto["id"]
                wallets = get_wallets(crypto_id)
                if wallets is not None:
                    print(f"--- {crypto['name']} Wallets ---")
                    for wallet in wallets:
                        print(wallet["address"])
                    print()

print_wallets()
