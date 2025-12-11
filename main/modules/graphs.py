import matplotlib.pyplot as plt
from collections import Counter

def  promedio(num: list):
    return sum(num) / len(num)

def porciento(parte, total):
    return parte/total

# def porcentaje(productos):
    
#     marcas_nac = [] 
#     marcas_int = []

#     for marcas in productos:
#         if marcas.get("nacional") == True:
#             marcas_nac.append(marcas.get("marca"))
#         else:
#             marcas_int.append(marcas.get("marca"))

#     contador_nac = len(marcas_nac)
#     contador_int = len(marcas_int)

#     valores = [contador_nac, contador_int]
#     labels = ["Nacionales", "Internacionales"]

#     fig, ax = plt.subplots()
#     ax.pie(valores, labels=labels, autopct='%1.1f%%', colors=["#E45A92", "#5D2F77"])
#     ax.set_title("Marcas nacionales vs internacionales")
#     plt.show()
    
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
    
def presentacion(producto):
    
    prodct_lb = []
    prodct_kg = []
    prodct_g = []
    
    for gramaje in producto:
        
        if gramaje["nombre"] == "frijol":
            
            if gramaje.get("presentacion") == "lb":
                prodct_lb.append(gramaje.get("precio_cup"))
            
            elif gramaje.get("presentacion") == "kg":
                prodct_kg.append(gramaje.get("precio_cup"))
               
            elif gramaje.get("presentacion") == "g":
                prodct_g.append(gramaje.get("precio_cup"))
                
    return prodct_lb, prodct_kg, prodct_g
 
 
 
def calcular_inflacion_real(productos_mypimes, productos_canasta):
    
    for mypimes in productos_mypimes:
        
        if mypimes["tipo"] == "granos" and mypimes["nombre"] == "frijol" and mypimes["presentacion"] == "kg":
            precio_frijol_mypimes = mypimes["precio_cup"]
            
        if mypimes["tipo"] == "granos" and mypimes["nombre"] == "arroz" and mypimes["presentacion"] == "kg":
            precio_arroz_mypimes = mypimes["precio_cup"]
            
        if mypimes["tipo"] == "aceites":
            precio_aceite_mypimes = mypimes["precio_cup"]
            
           
    for canasta in productos_canasta:
        
        if canasta["nombre"] == "frijol nacional":
            precio_frijol_oficial = canasta["precio_cup"]
             
        if canasta["nombre"] == "arroz nacional":
            precio_arroz_oficial = canasta["precio_cup"]
        
        if canasta["nombre"] == "aceite vegetal soya":
            precio_aceite_oficial = canasta["precio_cup"]
        
    
    
    productos_comunes = [
        
        ("Frijolo", precio_frijol_oficial, precio_frijol_mypimes),
        ("Arroz", precio_arroz_oficial, precio_arroz_mypimes),
        ("Aceite", precio_aceite_oficial, precio_aceite_mypimes)
    ]
    
    fig, ax = plt.subplots(figsize=(12, 6))

    nombres = []
    oficial = []
    real = []

    for nombre, precio_oficial, precio_real in productos_comunes:
        nombres.append(nombre)
        oficial.append(precio_oficial)
        real.append(precio_real)

    posiciones = list(range(len(nombres)))
    ancho = 0.35
    multiplicador = 0

    precios_datos = {
        'Precio Oficial (CUP)': oficial,
        'Precio Real Mercado (CUP)': real
    }

    colores = ["#047204", "#570900"]
    indice_color = 0

    for etiqueta, valores in precios_datos.items():
        desplazamiento = ancho * multiplicador
        posiciones_barras = []
        for i in posiciones:
            posiciones_barras.append(i + desplazamiento)
        
        ax.bar(posiciones_barras, valores, ancho, label=etiqueta, color=colores[indice_color])
        multiplicador += 1
        indice_color += 1

    posiciones_etiquetas = []
    for i in posiciones:
        posiciones_etiquetas.append(i + ancho / 2)
        
    ax.set_ylabel('Precio (CUP)')
    ax.set_title('Brecha de Precios: Oficial vs Mercado Real')
    ax.set_xticks(posiciones_etiquetas)
    ax.set_xticklabels(nombres)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.show()
    