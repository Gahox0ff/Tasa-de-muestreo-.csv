import pandas as pd  # Importar la biblioteca pandas para manejo de datos

# Cargar el archivo CSV
datos = pd.read_csv("T1.csv")  # Lee el archivo CSV y lo almacena en un DataFrame

# Calcular la tasa de muestreo
intervalo_muestreo = float(datos.iloc[0, 1])  # Extrae el valor del intervalo de muestreo (Ts) en segundos
tasa_muestreo = 1 / intervalo_muestreo  # Calcula la tasa de muestreo (fs = 1 / Ts)

# Mostrar resultado
print(f"Tasa de muestreo: {tasa_muestreo:.2f} Hz")  # Imprime la tasa de muestreo con dos decimales
