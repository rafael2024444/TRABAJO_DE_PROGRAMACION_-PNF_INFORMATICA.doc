# Paso 1: Crear y escribir en un archivo
nombre_archivo = 'ejemplo.txt'

# Abrir el archivo en modo escritura ('w'), esto creará el archivo si no existe
with open(nombre_archivo, 'w') as archivo:
    archivo.write('Hola, este es un ejemplo de manejo de archivos en Python.\n')
    archivo.write('Aquí agregamos una segunda línea de texto.\n')
    archivo.write('¡Hasta luego!\n')

# Paso 2: Leer desde el archivo
print("Contenido del archivo:")
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print(contenido)

# Paso 3: Agregar más datos al archivo
with open(nombre_archivo, 'a') as archivo: # abrir en modo añadir ('a')
    archivo.write('Esta línea se agrega al final del archivo.\n')

# Paso 4: Volver a leer el archivo para ver el contenido actualizado
print("Contenido actualizado del archivo:")
with open(nombre_archivo, 'r') as archivo:
    contenido_actualizado = archivo.read()
    print(contenido_actualizado)
