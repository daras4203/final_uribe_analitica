import pandas as pd 
import requests 
from data.simuladorEmpleados import generar_empleados

#1. Si voy a comenzar una rutina de analitica con PANDAS lo primero
#que debo hacer es crear un dataframe de los datos

#Como crear un data frame desde una fuente de datos simulados en el mismo python
lista=generar_ventas(10)
print(lista)
datosOrdenado=pd.DataFrame(lista) #Normlamente OJO se le entraga una LISTA

#1.Identificar/inspeccionar/asociar la informacion de base de los datos

#2.limpiar/evaluar la calidad de los datos


#como crear un data frame desde un archivo de Excel

#como crear un data frame desde un archivo csv

#como crear un data frame desde un consumo de un API(JSON)
