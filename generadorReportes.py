import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from transformaciones import (
    datosOrdenados,
    ventas_mayores_500,
    ventas_300_tallaM,
    ventas_vendedores_Messi_Ronaldo,
    ventas_febrero,
    ventas_leo_messi,
    ventas_agrupadas,
    ventas_talla
)

# ===============================
# CREAR CARPETAS DE REPORTES
# ===============================
CARPETA_REPORTES = "reportes"
CARPETA_GRAFICAS = os.path.join(CARPETA_REPORTES, "graficas")

os.makedirs(CARPETA_GRAFICAS, exist_ok=True)


# ===============================
# FUNCION PARA CONVERTIR DATAFRAME A HTML
# ===============================
def dataFrame_convertir_html(dataFrame):

    if isinstance(dataFrame, pd.Series):
        dataFrame = dataFrame.reset_index()

    return dataFrame.to_html(
        classes="table table-striped table-hover table-bordered table-sm",
        border=0
    )


# ===============================
# GRAFICA 1: VENTAS POR VENDEDOR
# ===============================
plt.figure(figsize=(10,5))

ventas_agrupadas.sort_values(ascending=False).plot(
    kind="bar",
    color="#264D25"
)

plt.title("Total de ventas por vendedor")
plt.xlabel("Vendedor")
plt.ylabel("Total vendido en pesos")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(os.path.join(CARPETA_GRAFICAS, "ventas_por_vendedor.png"))
plt.close()


# ===============================
# GRAFICA 2: VENTAS POR TALLA
# ===============================
plt.figure(figsize=(10,5))

ventas_talla.sort_values(ascending=False).plot(
    kind="bar",
    color="#39254D"
)

plt.title("Total de ventas por talla")
plt.xlabel("Talla")
plt.ylabel("Total vendido en pesos")

plt.tight_layout()

plt.savefig(os.path.join(CARPETA_GRAFICAS, "ventas_por_talla.png"))
plt.close()


# ===============================
# GRAFICA 3: VENTAS POR MES
# ===============================
df = pd.DataFrame(datosOrdenados)

df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
df["mes"] = df["fecha"].dt.month

ventas_mes = df.groupby("mes")["total"].sum()

plt.figure(figsize=(10,5))

ventas_mes.plot(
    kind="bar",
    color="#4AB5D5"
)

plt.title("Total de ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Total vendido")

plt.tight_layout()

plt.savefig(os.path.join(CARPETA_GRAFICAS,"ventas_por_mes.png"))
plt.close()


# ===============================
# GRAFICA 4: TORTA POR VENDEDOR
# ===============================
colores_torta = [
    "#264D25",
    "#39254D",
    "#5C8A2B",
    "#7B0E15",
    "#4AB5D5",
    "#C13B89",
    "#C9E24C",
    "#B2672E",
    "#43F10E",
    "#EEAF80"
]

explode = [0.07] * len(ventas_agrupadas)

plt.figure(figsize=(10,5))

ax = ventas_agrupadas.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    colors=colores_torta,
    explode=explode,
    wedgeprops={"edgecolor":"black"},
    pctdistance=0.75
)

# Rotar etiquetas 45 grados
for label in ax.texts:
    label.set_rotation(45)

plt.title("Participación porcentual de cada vendedor")

plt.tight_layout()

plt.savefig(os.path.join(CARPETA_GRAFICAS,"tortas_vendedor.png"))
plt.close()


# ===============================
# CREACION DEL REPORTE HTML
# ===============================
documento_html = f"""
<!DOCTYPE html>
<html lang="es">

<head>
<meta charset="UTF-8">
<title>Reporte de Analítica</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

</head>

<body>

<div class="container mt-5">

<h1>Reporte de Analítica de Ventas</h1>
<hr>

<p>
Este reporte presenta el análisis de ventas de la tienda Chevignon Sandiego
utilizando herramientas de análisis de datos con Python y Pandas.
</p>

<div class="card p-4 shadow mb-5">

<h3>Total vendido por vendedor</h3>

{dataFrame_convertir_html(ventas_agrupadas)}

<img src="graficas/ventas_por_vendedor.png" class="img-fluid mt-3">

<img src="graficas/tortas_vendedor.png" class="img-fluid mt-3">

</div>

<div class="card p-4 shadow mb-5">

<h3>Ventas por talla</h3>

<img src="graficas/ventas_por_talla.png" class="img-fluid">

</div>

<div class="card p-4 shadow mb-5">

<h3>Ventas por mes</h3>

<img src="graficas/ventas_por_mes.png" class="img-fluid">

</div>

</div>

</body>
</html>
"""


# ===============================
# GUARDAR REPORTE
# ===============================
RUTA_REPORTE = os.path.join(CARPETA_REPORTES,"reporte.html")

with open(RUTA_REPORTE, "w", encoding="utf-8") as archivo:
    archivo.write(documento_html)