import requests
from bs4 import BeautifulSoup

anchieta = entrada 'https://anchieta.br'
r = requests.get(anchieta)
html_anchieta = r.text

soup = BeautifulSoup(html_anchieta)
for elem in soup.find_all('div', class_='elementor-widget-container'):
    print(elem.text)
