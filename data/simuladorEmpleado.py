# Construir una funcion generadora de N empleados que permita crear MOCKS o datos semilla
import random
import pandas as pd
from datetime import datetime, timedelta


def generar_empleados(numeroEmpleados):

    # Simular una lista de nombres
    # Leer un excel y cargar esta lista con la info del excel
    # Consumir API
    
    nombres = [
        "Carlos", "Laura", "Andrés", "Valentina", "Miguel",
        "Sofía", "Javier", "Daniela", "Felipe", "Natalia",
        "Sebastián", "Camila", "Ricardo", "Paola", "Luis",
    ]

    # Simular una lista de apellidos
    apellidos = [
        "Méndez", "Gómez", "Torres", "Ruiz", "Herrera",
        "Vargas", "Castillo", "Moreno", "Jiménez", "Romero",
        "Díaz", "Reyes", "Cruz", "Salazar", "Peña",
    ]

    # Simular rangos de salario base (en pesos colombianos)
    salariosBase = [
        1300000,   # SMMLV 2026
        1500000,
        1800000,
        2200000,
        2800000,
        3500000,
        4500000,
        6000000,
    ]

    # Simular la fecha de ingreso a la compañia
    fechaInicio = datetime(2018, 1, 1)

    # Generar los N empleados que se están pidiendo
    empleados = []
    for i in range(numeroEmpleados):
        nombre   = random.choice(nombres)
        apellido = random.choice(apellidos)
        fechaIngreso = fechaInicio + timedelta(days=random.randint(0, 2555))  # hasta 7 años
        empleados.append(
            {
                "id":            i + 1,
                "nombre":        f"{nombre} {apellido}",
                "documento":     random.randint(1000000, 99999999),
                "salarioBase":   random.choice(salariosBase),
                "fechaIngreso":  fechaIngreso,
            }
        )
    return empleados