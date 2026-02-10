import os

# obtener el directorio actual
"""cwd = os.getcwd()
print("Directorio de trabajo actual: ", cwd)"""

# lisrtar archivos.txt

txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
print("Archivos txt: ", txt_files)

# renombrar un archivo
os.rename("caperucita.txt", "cuento.txt")
print("Archivo renombrado a cuento.txt")

txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
print("Archivos txt: ", txt_files)
