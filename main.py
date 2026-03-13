import pandas as pd 
from data.simuladorVentas import generar_ventas          
from utils.generarcsv import generar_archivo_csv
from utils.generarjson import generar_archivo_json 


#1. Si voy a comenzar una rutina de analitica con PANDAS lo primero
#que debo hacer es crear un dataframe de los datos

#Como crear un data frame desde una fuente de datos simulados en el mismo python
lista = generar_ventas(200)
print(lista)
datosOrdenados = pd.DataFrame(lista) #Normlamente OJO se le entraga una LISTA


generar_archivo_csv(lista,"data/ventas_susias.csv") 
generar_archivo_json(lista,"data/ventas_susias.json") 




#B TEXTOS
# -ESPACIOS
#-MAYUSCULAS/MINUSCULAS
#FORMATOS INCONSISTENTES

#C. VALORES NULOS

#D. VALORES DUPLICADOS

#E. VERIFICAR TIPO DE DATOS

#F. SE VERIFICAN LAS REGLAS DE NEGOCIO



dataFrameCopia=datosOrdenados.copy()

dataFrameCopia.columns=dataFrameCopia.columns.str.strip()
columnas_texto=["producto","talla","vendedor"]
for columna in columnas_texto:
    dataFrameCopia[columna]=dataFrameCopia[columna].astype(str).str.strip()

dataFrameCopia["producto"]=dataFrameCopia["producto"].str.title()
dataFrameCopia["vendedor"]=dataFrameCopia["vendedor"].str.title()
dataFrameCopia["talla"]=dataFrameCopia["talla"].str.upper()

dataFrameCopia.replace([""," ","none","nan"],pd.NA,inplace=True)

dataFrameCopia["precioUnitario"]=pd.to_numeric(dataFrameCopia["precioUnitario"],errors="coerce")
dataFrameCopia["cantidad"]=pd.to_numeric(dataFrameCopia["cantidad"],errors="coerce")
dataFrameCopia["total"]=pd.to_numeric(dataFrameCopia["total"],errors="coerce")

dataFrameCopia["fecha"]=pd.to_datetime(dataFrameCopia["fecha"],errors="coerce",dayfirst=True)

dataFrameCopia=dataFrameCopia.drop_duplicates()

dataFrameCopia=dataFrameCopia.dropna(subset=["producto","precioUnitario","cantidad","total","fecha"])

#rutina para limpiar segun reglas de negocio
dataFrameCopia=dataFrameCopia[dataFrameCopia["cantidad"]>0]
dataFrameCopia=dataFrameCopia[dataFrameCopia["precioUnitario"]>5000]


tallasValidas=["XS","S","M","L","XL","XXL","XXXL"]
dataFrameCopia=dataFrameCopia[dataFrameCopia["talla"].isin(tallasValidas)]

dataFrameCopia["total"]=dataFrameCopia["precioUnitario"]*dataFrameCopia["cantidad"]

