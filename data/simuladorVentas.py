#Construir una funcion generadora de N ventas que permita crear MOCKS o datos semilla para la rutina de analisis
import random
import pandas as pd
from datetime import datetime, timedelta


def generar_ventas(numeroVentas):

    # Lista de productos simulados
    productos = [
        {"nombre": "Camisa Polo de Hombre Slim Fit Manga Corta con Textura Bordado de Pato en Algodón", "precio": 150000, "descuento": False},
        {"nombre": "Camisa Polo de Hombre Classic Fit Cuello Nerú Manga Corta Textura Piqué Jacquard en Algodón", "precio": 135000, "descuento": False},
        {"nombre": "Camisa Polo de Hombre Slim Fit Cuello Nerú Manga Corta Sesgos en Contraste en Mezcla de Algodón", "precio": 128000, "descuento": True},
        {"nombre": "Camisa Polo de Hombre Classic Fit Manga Larga Varsity con Cierre Efecto Desgaste en Algodón", "precio": 162000, "descuento": False},
        {"nombre": "Camiseta Polo M/C", "precio": 98000, "descuento": False},
        {"nombre": "Jean de Hombre Skinny Fit Tiro Medio Lavado Oscuro Clásico con Raspones en Mezcla de Algodón", "precio": 195000, "descuento": True},
        {"nombre": "Jean de Hombre Rider Skinny Fit Tiro Bajo Lavado Medio Rotos Detalles en Costuras en Mezcla de Algodón", "precio": 210000, "descuento": False},
        {"nombre": "Chaqueta de Hombre Bomber Acolchada Rombos y Gráficos Bordados en Mezcla de Algodón y Poliéster", "precio": 380000, "descuento": True},
        {"nombre": "Chaqueta de Hombre Doble Faz Cuello Alto Windbreaker Bolsillo Canguro en Mezcla de Algodón y Poliéster", "precio": 420000, "descuento": False},
        {"nombre": "Chaqueta Tipo Trucker en Denim para Hombre", "precio": 820000, "descuento": False},
    ]

    # Lista de tallas
    tallas = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]

    # Lista de vendedores
    vendedores = [
        "Leo Messi",
        "Cristiano Ronaldo",
        "Neymar Jr",
        "Kylian Mbappé",
        "Kevin De Bruyne",
        "Mohamed Salah",
        "Virgil van Dijk",
        "Sadio Mané",
        "Eden Hazard"
    ]

    # Fecha inicial para las ventas
    fechaInicio = datetime(2026, 1, 2)

    ventas = []

    # Generar ventas simuladas
    for i in range(numeroVentas):

        producto = random.choice(productos)
        cantidad = random.randint(1, 5)
        fecha = fechaInicio + timedelta(days=random.randint(0, 60))

        ventas.append({
            "producto": producto["nombre"],
            "precioUnitario": producto["precio"],
            "talla": random.choice(tallas),
            "cantidad": cantidad,
            "vendedor": random.choice(vendedores),
            "fecha": fecha,
            "total": cantidad * producto["precio"]
        })

    return ventas