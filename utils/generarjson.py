import pandas as pd
import os



def generar_archivo_json(listaVentas, nombreArchivo):
    # Crear un DataFrame a partir de la lista de datos
    df = pd.DataFrame(listaVentas)

    # Guardar el DataFrame como un archivo JSON
    df.to_json(nombreArchivo, orient='records', indent=4)

    print(f"Archivo '{nombreArchivo}' generado exitosamente.")

    

