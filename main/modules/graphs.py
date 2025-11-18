import matplotlib.pyplot as plt
from collections import Counter

def  promedio(num: list):
    return sum(num) / len(num)

def porciento(parte, total):
    return parte/total

def porcentaje(productos):
    
    marcas_nac = [] 
    marcas_int = []

    for marcas in productos:
        if marcas.get("nacional") == True:
            marcas_nac.append(marcas.get("marca"))
        else:
            marcas_int.append(marcas.get("marca"))

    contador_nac = len(marcas_nac)
    contador_int = len(marcas_int)

    valores = [contador_nac, contador_int]
    labels = ["Nacionales", "Internacionales"]

    fig, ax = plt.subplots()
    ax.pie(valores, labels=labels, autopct='%1.1f%%', colors=["#E45A92", "#5D2F77"])
    ax.set_title("Marcas nacionales vs internacionales")

    plt.show()
import matplotlib.pyplot as plt
import numpy as np
def pmm(tipos, promedios, maximos, minimos):
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(tipos))
    ancho = 0.25

    ax.bar(x - ancho, promedios, width=ancho, label="Promedio", color="#060771")
    ax.bar(x, maximos, width=ancho, label="Máximo", color="#FFE08F")
    ax.bar(x + ancho, minimos, width=ancho, label="Mínimo", color="#F87B1B")

    ax.set_title("Promedio, Máximo y Mínimo de precios por tipo de producto")
    ax.set_xlabel("Tipo de producto")
    ax.set_ylabel("Precio (CUP)")
    ax.set_xticks(x)
    ax.set_xticklabels(tipos)
    ax.legend()
    plt.show()