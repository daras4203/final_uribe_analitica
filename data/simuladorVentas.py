#Construir una funcion generadora de N ventas que permita crear MOCKS o datos semilla para la rutina de analisis
import pandas as pd # pyright: ignore[reportMissingModuleSource]
from datetime import datetime, timedelta


def generar_ventas(numeroVentas):

    #Simular una lista de productos
    #Leer un excel y cargar esta lista con la info del excel
    #Consumir API
    productos=[
        {"nombre":"Camisa Polo de Hombre Slim Fit Manga Corta con Textura Bordado de Pato en Algodón","precio":150000,"descuento":False},
        {"nombre":"Camisa Polo de Hombre Classic Fit Cuello Nerú Manga Corta Textura Piqué Jacquard en Algodón","precio":135000,"descuento":False},
        {"nombre":"Camisa Polo de Hombre Slim Fit Cuello Nerú Manga Corta Sesgos en Contraste en Mezcla de Algodón","precio":128000,"descuento":True},
        {"nombre":"Camisa Polo de Hombre Classic Fit Manga Larga Varsity con Cierre Efecto Desgaste en Algodón","precio":162000,"descuento":False},
        {"nombre":"Camiseta Polo M/C","precio":98000,"descuento":False},
        {"nombre":"Jean de Hombre Skinny Fit Tiro Medio Lavado Oscuro Clásico con Raspones en Mezcla de Algodón","precio":195000,"descuento":True},
        {"nombre":"Jean de Hombre Rider Skinny Fit Tiro Bajo Lavado Medio Rotos Detalles en Costuras en Mezcla de Algodón","precio":210000,"descuento":False},
        {"nombre":"Chaqueta de Hombre Bomber Acolchada Rombos y Gráficos Bordados en Mezcla de Algodón y Poliéster","precio":380000,"descuento":True},
        {"nombre":"Chaqueta de Hombre Doble Faz Cuello Alto Windbreaker Bolsillo Canguro en Mezcla de Algodón y Poliéster","precio":420000,"descuento":False},
        {"nombre":"Chaqueta Tipo Trucker en Denim para Hombre","precio":820000,"descuento":False},
    ]

    #Simular una lista de tallas
    tallas=["XS","S","M","L","XL","XXL","XXXL"]
    
    
    #simular vendedor asociado
    vendedores=[]
    
    #Simula la fecha
    fechaInicio=datetime(2026,1,2)

    
    #generar la N ventas que se me estan pidiendo
    ventas=[]
    for i in range(numeroVentas):
        producto=random.choice(productos) # pyright: ignore[reportUndefinedVariable]
        cantidad=random.randint(1,5) # pyright: ignore[reportUndefinedVariable]
        fecha=fechaInicio+timedelta(days=random.randint(0,60)) # pyright: ignore[reportUndefinedVariable]
        ventas.append(
            {
                "producto":producto,
                "precioUnitario":producto["precio"],
                "talla":random.choice(tallas), # pyright: ignore[reportUndefinedVariable]
                "catidad":cantidad,
                "vendedor":random.choice(vendedores), # pyright: ignore[reportUndefinedVariable]
                "fecha":fecha,
                "total":cantidad*producto["precio"] 
            }
            
        )
        return ventas



        #Seleccionar producto aleatorio





   