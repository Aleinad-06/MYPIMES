import requests
from bs4 import BeautifulSoup
import json

while True:
    
    url = "https://elyerromenu.com/b/don-rilio/seller/bazar-ym/category/carnes-y-embutidos-388a"

    if url.lower() == "salir":
        break
    
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0" }
    
    respuesta = requests.get(url, headers = header)
    
    if respuesta.status_code == 200:
        buscador = BeautifulSoup(respuesta.text, "html.parser")
        nombre = {
            "class": "line-clamp-1 text-gray-500 text-xs leading-1 w-full pr-4"
        }

        atributos_nombre = {
            "line-clamp-2 text-main-500 font-semibold text-base leading-tight"
        }
        atributos_presentacion = {
            "class": "line-clamp-2 text-gray-500 text-xs"
        }
        
        atributos_precio = {
            "class": "text-main-500 font-semibold"
        }
        
        nombre_lugar = buscador.find("div", attrs = nombre)
        producto = buscador.find_all("div", attrs = atributos_nombre)
        presentacion = buscador.find_all("div", attrs = atributos_presentacion)
        precio = buscador.find_all("span", attrs = atributos_precio)
        
        productoos = []
        
        for i in range(len(producto)):
            productoos.append(
                {
                    "nombre": producto[i].text ,
                    "presentacion": presentacion[i].text,
                    "precio": float(precio[i].text.split(" ")[0].replace(",", "")) 
                }
            )
        
        contador = 0
        with open(f"{nombre_lugar.text}_{contador}.json", "w", encoding="utf-8") as archivo:
            json.dump(productoos, archivo, ensure_ascii=False, indent=4)
        
        contador += 1