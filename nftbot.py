import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from colorama import Fore, Style

def get_h3_and_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    inside_article_tags = soup.find_all(class_="inside-article")
    h3_and_links = []

    for tag in inside_article_tags:
        h3_tags = tag.find_all("h3")
        links = tag.find_all("a")

        for h3 in h3_tags:
            h3_text = h3.text.strip()
            h3_link = None

            for link in links:
                link_text = link.get("href", "").strip()
                if link_text.startswith("https://airdrops.io/"):
                    h3_link = link_text
                    break

            h3_and_links.append((h3_text, h3_link))

    return h3_and_links


if __name__ == "__main__":
    url = "https://airdrops.io"  # Remplacez par l'URL du site web souhaité
    h3_and_links = get_h3_and_links(url)

    if h3_and_links:
        print("Balises h3 et liens dans la classe 'inside-article' :")
        now = datetime.now()
        one_week_ago = now - timedelta(days=7)
        for h3, link in h3_and_links:
            if link is not None:
                try:
                    link_date = datetime.strptime(link.split("/")[-1], "%Y-%m-%d")
                    if link_date >= one_week_ago:
                        print(Fore.GREEN + "Name :", h3, "/ Lien :", link + Style.RESET_ALL)  # Vert pour les nouvelles balises h3
                    else:
                        print(Fore.YELLOW + "Name :", h3, "/ Lien :", link + Style.RESET_ALL)  # Orange pour les balises h3 anciennes
                except ValueError:
                    print("Name :", h3, "/ Lien :", link)
            else:
                print("Name :", h3, "/ Lien : None")
    else:
        print("Aucune balise h3 ou lien trouvés dans la classe 'inside-article' sur la page.")
