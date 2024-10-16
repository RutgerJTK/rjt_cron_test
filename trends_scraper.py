import requests
from bs4 import BeautifulSoup

def get_trends():
    print("Getting trends...")
    url = "https://trends.google.com/trends/explore?date=today%205-y&q=AI&hl=nl"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all paragraph texts
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print(p.text)


get_trends()