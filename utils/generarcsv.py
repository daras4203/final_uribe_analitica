import pandas as pd
import os

def generar_archivo_csv(listaVentas, nombreArchivo):
    # Crear un DataFrame a partir de la lista de datos
    df = pd.DataFrame(listaVentas)

    # Guardar el DataFrame como un archivo CSV
    df.to_csv(nombreArchivo, index=False)

    print(f"Archivo '{nombreArchivo}' generado exitosamente.")