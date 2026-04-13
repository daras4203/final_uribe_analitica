# Construir una funcion generadora de N empleados que permita crear MOCKS o datos semilla

import random
from datetime import datetime, timedelta


def generar_empleados(numeroEmpleados):

    # Simular una lista de nombres
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
        1300000,
        1500000,
        1800000,
        2200000,
        2800000,
        3500000,
        4500000,
        6000000,
    ]

    # Fecha inicial de ingreso
    fechaInicio = datetime(2018, 1, 1)

    empleados = []

    for i in range(numeroEmpleados):

        # Generar nombre completo
        nombreCompleto = f"{random.choice(nombres)} {random.choice(apellidos)}"

        # Generar fecha aleatoria
        fechaIngreso = fechaInicio + timedelta(days=random.randint(0, 2555))

        # Generar salario (con algunos errores simulados)
        salario = random.choice(salariosBase + [None, -500000])

        empleado = {
            "id": i + 1,
            "nombreCompleto": nombreCompleto,
            "documento": random.randint(10000000, 99999999),
            "salarioBase": salario,
            "fechaIngreso": fechaIngreso.strftime("%Y-%m-%d")
        }

        empleados.append(empleado)

    return empleados