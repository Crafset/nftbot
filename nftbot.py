import requests
from bs4 import BeautifulSoup
import time

while True:
    url = "https://campfire.exchange/minting"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    nft_projects = soup.select(".nft-project-card")

    for project in nft_projects:
        name = project.select_one(".nft-project-card-title").text
        url = project.select_one("a")["href"]
        discord_link = project.select_one(".discord-link")
        twitter_link = project.select_one(".twitter-link")

        if discord_link and twitter_link:
            discord_url = discord_link["href"]
            twitter_url = twitter_link["href"]
            print(f"Project name: {name}\nProject URL: {url}\nDiscord URL: {discord_url}\nTwitter URL: {twitter_url}\n")

    time.sleep(60) # Attendre 60 secondes avant de continuer
