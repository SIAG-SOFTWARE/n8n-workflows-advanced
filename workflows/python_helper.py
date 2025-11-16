import requests
from bs4 import BeautifulSoup

def scrape(url: str):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    return [a.text for a in soup.select("a")[:10]]

if __name__ == "__main__":
    print(scrape("https://example.com"))
