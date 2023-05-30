import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

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
            h3_and_links.append((h3_text, None))

        for link in links:
            link_text = link.get("href", "").strip()
            parsed_url = urlparse(link_text)
            if parsed_url.netloc == "airdrops.io":
                h3_and_links.append((None, link_text))
            else:
                h3_and_links.append((None, None))

    return h3_and_links


if __name__ == "__main__":
    url = "https://airdrops.io"  # Remplacez par l'URL du site web souhaité
    h3_and_links = get_h3_and_links(url)

    if h3_and_links:
        print("Balises h3 et liens dans la classe 'inside-article' :")
        for h3, link in h3_and_links:
            if h3:
                print("Name :", h3, "Lien :",link)
            if link:
                print("Lien :", link)
    else:
        print("Aucune balise h3 ou lien trouvés dans la classe 'inside-article' sur la page.")
