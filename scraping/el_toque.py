import requests
from bs4 import BeautifulSoup

url = "https://eltoque.com/"


respuesta = requests.get(url)
print(respuesta.json())