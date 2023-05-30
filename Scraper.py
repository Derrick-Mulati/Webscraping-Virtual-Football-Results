from bs4 import BeautifulSoup
import requests









try:

    source = requests.get('https://www.betika.com/en-ke/virtuals/table/6')
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')
    print(soup)
 
except Exception as e:
    print(e)