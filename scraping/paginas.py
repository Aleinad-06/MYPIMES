# import cloudscraper
import requests
from bs4 import BeautifulSoup
import json

url = "https://celebrenstore.com/mercadito"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0"}

# scraper = cloudscraper.create_scraper()
respuesta = requests.get(url, headers = header)


if respuesta.status_code == 200:
    print(respuesta.text)
    # buscador = BeautifulSoup(respuesta.text, "html.parser")
    # atributos_precio = {"class": " text-sm text-texto-texto text-left font-['Inter-Black',_sans-serif] font-black"}
    # atributos_nombre = {"class" : "text-lg text-ellipsis overflow-hidden font-black text-texto-texto text-left font-['Inter-Black',_sans-serif]"}
    # elementos_p = buscador.find_all("h5", attrs = atributos_precio)
    # elementos_n = buscador.find_all("h3", attrs = atributos_nombre)

    
    # productos = []
    # for i in range(len(elementos_n)):
    #     productos.append(
    #         {
    #             "nombre": elementos_n[i].text,
    #             "precio": int(elementos_p[i].text.split(" ")[0].replace(",", "")),
    #         }
    #     )
    # with open(f"{"celebrenstore"}.json", "w", encoding="utf-8") as archivo:
    #     json.dump(productos, archivo, ensure_ascii=False, indent=4)
        