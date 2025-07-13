print("-----------------------------------------------------------------------")
print("Ejercicios del TP2.4 - Excepciones en Pyhton - Algoritmos II")
print("-----------------------------------------------------------------------")
print()
#8.1 Crear un programa que abra un fichero en modo lectura y escritura, si no existe lo creará, y añadir la frase “Estoy aprendiendo Python”
print("Crea/Abre archivo y escribe texto.")
print()
archivo = open("aprendiendo.txt", "a+")

# Nos aseguramos de estar al final del archivo
archivo.seek(0, 2)  # 2 = final del archivo

# Escribimos la frase
archivo.write("Estoy aprendiendo Python\n")

# Cerramos
archivo.close()

print("-----------------------------------------------------------------------")
print()
#8.2 Crear un programa que abra el fichero editado anteriormente y muestre el estado del fichero, el modo en el que fue abierto, el nombre y 
# la codificación de caracteres del mismo.
print("Abre el archivo, muestra el estado y otros datos")

archivo = open("aprendiendo.txt", "r")

print("Nombre del archivo:", archivo.name)
print("Modo de apertura:", archivo.mode)
print("¿Está cerrado?", archivo.closed)
print("Codificación:", archivo.encoding)

archivo.close()
print("¿Está cerrado ahora?", archivo.closed)

print("-----------------------------------------------------------------------")
print()
#8.3 Realizar un programa que realice los ejercicios 1 y 2 utilizando la estructura with.
print("Lo mismo de antes pero con with structure")
# Escribir en el archivo (crear si no existe)
with open("aprendiendo.txt", "a+", encoding="utf-8") as archivo:
    archivo.write("Estoy aprendiendo Python con with\n")

# Mostrar el estado del archivo
with open("aprendiendo.txt", "r", encoding="utf-8") as archivo:
    print("Nombre del archivo:", archivo.name)
    print("Modo de apertura:", archivo.mode)
    print("¿Está cerrado?", archivo.closed)  # Debe ser False dentro del with
    print("Codificación:", archivo.encoding)

# Fuera del with, ya se cerró solo
print("¿Está cerrado fuera del with?", archivo.closed)