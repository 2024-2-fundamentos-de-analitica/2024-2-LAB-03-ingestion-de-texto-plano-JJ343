"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    
  import pandas as pd
  import re

  # Leer el archivo
  with open('files/input/clusters_report.txt' ,"r") as file:
    lines = file.readlines()
   
# Extract clusters from raw data
  clusters = []
  text=""
  for line in lines:
     text+=line
    

# Process the content directly without reading from a file

# Split the content into lines
# Process the content directly without reading from a file
  lines = text.strip().split("\n")[4:]

  palabras_clave = [palabra.strip() for palabra in text.split(',')]

# Formatear para que cada palabra clave quede en una nueva línea
  resultado = ",\n            ".join(palabras_clave)
  
# Data processing
  data = []
  for line in lines:
    if line.strip() == "":
        continue
    # Match the cluster information
    match = re.match(r'^\s*(\d+)\s+(\d+)\s+([\d,]+) %\s+(.+)', line)
    if match:
        cluster = int(match.group(1))
        cantidad_palabras_clave = int(match.group(2))
        porcentaje_palabras_clave = float(match.group(3).replace(',', '.'))
        palabras_clave = match.group(4).strip()
    else:
        # Append remaining keywords to the last row's keywords
        palabras_clave += " " + line.strip()
        data[-1][3] = palabras_clave
        continue
    data.append([cluster, cantidad_palabras_clave, porcentaje_palabras_clave, palabras_clave])

# Clean and format keywords
  for row in data:
    row[3] = re.sub(r'\s+', ' ', row[3].replace('\n', '').replace(',', ', ')).strip()

# Create the dataframe
  columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
  df = pd.DataFrame(data, columns=columns)
  
  df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(
    lambda x: ', '.join([palabra.strip() for palabra in x.split(',')])
  )

  print(df['principales_palabras_clave'].tolist()[0])
# Display the dataframe

  return df
  """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.

    
    """
pregunta_01()


  

