from bs4 import BeautifulSoup
import requests




try:
    source = requests.get('https://www.betpawa.co.ke/virtual-sports?virtualTab=results')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    out = soup.find('div', class_="l-container")

    print(out)








except Exception as e:
    print(e)
