import matplotlib.pyplot as plt
from collections import Counter

def  promedio(num: list):
    return sum(num) / len(num)

#---------------------------------

def mediana(datos):
    if len(datos) == 0:
        return 0
    
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    
    if n % 2 == 1:
        return datos_ordenados[n // 2]

    else:
        medio1 = datos_ordenados[n // 2 - 1]
        medio2 = datos_ordenados[n // 2]
        return (medio1 + medio2) / 2
    
#---------------------------------

def porciento(parte, total):
    return parte/total

#---------------------------------

def productos_mypimes(mypimes):
    
    m_productos = []

    for i in mypimes:
        for elementos in i["productos"]:
            if elementos is not None:
                m_productos.append(elementos)
            
    return m_productos

#---------------------------------

def productos_yerro(yerro):
    
    y_productos = []
    
    for j in yerro:
        for elementoss in j["productos"]:
            if elementoss is not None:
                y_productos.append(elementoss)
    
    return y_productos

#---------------------------------

def union(productos_mypimes, productos_yerro):
    
    union_productos = productos_mypimes + productos_yerro
    
    return union_productos

#---------------------------------

def yerro_bebida(yerro_m):
    
    bebidas = []

    for tienda in yerro_m:
        if tienda["bebida"] is not None:
            for bebida in tienda["bebida"]:
                bebidas.append(bebida)
            
    return bebidas

#---------------------------------

def bebidas_porciento(yerro_bebida):
    
    bebidas = {
        "nacional": 0,
        "internacional": 0
    }
    for bebida in yerro_bebida:
        if bebida["nacional"]:
            bebidas["nacional"] += 1
        else:
            bebidas["internacional"] += 1
    
    plt.figure(figsize=(7, 7))
    plt.pie(bebidas.values(), 
            labels=["Nacionales", "Internacionales"], 
            colors=["#08CB00", "#00CAFF"],
            autopct="%1.1f%%"
            )
    plt.title("Bebidas en MYPIMES")
    plt.show() 

#---------------------------------

def marcas(productos): 
    marcas_granos = []

    for elementos in productos:
        if elementos.get("tipo") == "granos":
            if elementos.get("marca") is not None:
                marcas_granos.append(elementos.get("marca"))

    contador_marcas = Counter(marcas_granos)
    nombres_marcas = list(contador_marcas.keys())
    frecuencias = list(contador_marcas.values())
    
    plt.barh(nombres_marcas, frecuencias)
    plt.xlabel("Frecuencia")
    plt.ylabel("Marca")
    plt.title("Frecuencia de marcas de granos")
    plt.tight_layout()
    plt.show()
    
#---------------------------------
    
def pmm(tipos, promedios, maximos, minimos):
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = list(range(len(tipos)))
    ancho = 0.25

    x_promedios = []
    x_maximos = []
    x_minimos = []
    
    for i in x:
        x_promedios.append(i - ancho)
        x_maximos.append(i)
        x_minimos.append(i + ancho)
    
    ax.bar(x_promedios, promedios, width=ancho, label="Promedio", color="#060771")
    ax.bar(x_maximos, maximos, width=ancho, label="Máximo", color="#FFE08F")
    ax.bar(x_minimos, minimos, width=ancho, label="Mínimo", color="#F87B1B")
    
    ax.set_title("Promedio, Máximo y Mínimo de precios por tipo de producto")
    ax.set_xlabel("Tipo de producto")
    ax.set_ylabel("Precio (CUP)")
    ax.set_xticks(x)
    ax.set_xticklabels(tipos)
    ax.legend()
    plt.show()
       
#---------------------------------

def analizar_nacional_vs_importado(productos):
    
    nacionales = []
    importados = []
    
    for tienda in productos:
            if "nacional" in tienda:
                if tienda["nacional"] == True:
                    nacionales.append(tienda["precio_cup"])
                else:
                    importados.append(tienda["precio_cup"])
    
    promedio_nacional = promedio(nacionales)
    promedio_importado = promedio(importados)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # barras
    categorias = ["Nacional", "Importado"]
    promedios = [promedio_nacional, promedio_importado]
    colores_barras = ["#3498db", "#e67e22"]
    
    ax1.bar(categorias, promedios, color=colores_barras, width=0.5)
    ax1.set_ylabel("Precio Promedio (CUP)")
    ax1.set_title("Precio Promedio: Nacional vs Importado")
    ax1.grid(axis="y", alpha=0.3)
    
    for i, v in enumerate(promedios):
        ax1.text(i, v + 20, f"{v:.0f} CUP", ha="center")
    
    # pastel
    cantidades = [len(nacionales), len(importados)]
    ax2.pie(cantidades, labels=categorias, autopct="%1.1f%%", colors=colores_barras, startangle=90)
    ax2.set_title("Distribución de Productos en el Mercado")
    
    plt.tight_layout()
    plt.show()
    
    return promedio_nacional, promedio_importado
#---------------------------------

def cbasica(canasta_basica):
    cb_productos = []
    cb_nombre_productos = []
    for i in canasta_basica["productos"]:
        cb_nombre_productos.append(i["nombre"])
        cb_productos.append(i["precio_cup"])
    return cb_nombre_productos, cb_productos

#---------------------------------

def canasta_b(canasta):
    cb_productos = []
    for i in canasta["productos"]:
        cb_productos.append(i)
    return cb_productos