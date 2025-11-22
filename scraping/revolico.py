import cloudscraper
from bs4 import BeautifulSoup
import json
# "https://www.revolico.com/profile/aPt77ECWFm052agGiAlMZPXs"
while True:
    url = input("Ingrese la URL de Revolico a scrapear (o 'salir' para terminar): ")
    if url.lower() == "salir":
        break
    
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0"}

    scraper = cloudscraper.create_scraper()
    respuesta = scraper.get(url, headers = header)

    if respuesta.status_code == 200:
        buscador = BeautifulSoup(respuesta.text, "html.parser")
        nombre = {"class": "styles__UserName-sc-c410e852-2 jbhVnP"}
        atributos_precio = {"class" : "AdCard__StyledPrice-sc-bb98bc10-3 PwhuM"}
        atributos_nombre = {"class": "AdCard__StyledTitle-sc-bb98bc10-4 dzmgvy"}
        nombre_lugar = buscador.find("h2", attrs = nombre)
        elementos_p = buscador.find_all("p", attrs = atributos_precio)
        elementos_n = buscador.find_all("p", attrs = atributos_nombre)

        
        productos = []
        for i in range(len(elementos_n)):
            productos.append(
                {
                    "nombre": elementos_n[i].text,
                    "precio": int(elementos_p[i].text.split(" ")[0].replace(",", "")),
                }
            )
        with open(f"{nombre_lugar.text}.json", "w", encoding="utf-8") as archivo:
            json.dump(productos, archivo, ensure_ascii=False, indent=4)
            