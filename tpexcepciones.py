print("-----------------------------------------------------------------------")
print("Ejercicios del TP2.4 - Excepciones en Pyhton - Algoritmos II")
print("-----------------------------------------------------------------------")
print()
#7.1 Crear una Función que divida hasta cero, ej: dividir(27,0), verificar: ZeroDivisionError:
print("Dividir entre 0: ZeroDivisionError")
print()

def dividir(num,div):
  return num/div

print("dividir 27/0")
try:
    res = dividir(27,0)
    print(res)
except ZeroDivisionError:
    print("No se puede dividir entre cero")

print("-----------------------------------------------------------------------")
#7.2 llamar a la función mas_10() con cualquier número, además: add_10("cinco") verificar TypeError:
print("Funcion para sumar 10.")
print()

def mas_10(valor):
    return valor + 10

print("Sumar a 5: ")
try:
    print(mas_10(5))
except TypeError:
    print("Error: el tipo de dato no es correcto")

print("Sumar a cinco: ")
try:
    print(mas_10("cinco"))
except TypeError:
    print("Error: el tipo de dato no es correcto")

print("-----------------------------------------------------------------------")
#7.3 Crear una Lista e Iterar mas allá del limite del Index, verifica: IndexError:
print("Iterar más allá del límite.")
print()

mi_lista = [10, 20, 30]

for i in range(4):
    try:
        print(f"Elemento en posición {i+1}: {mi_lista[i]}")
    except IndexError:
        print(f"¡Error! No existe el índice {i+1} (IndexError)")

print("-----------------------------------------------------------------------")
#7.3 Crear un Diciconario en Python y buscar una clave Inexistente, verificar keyError:
print("Buscar una clave erronea en un diccionario")
print()

persona = {
    "nombre": "Filomena",
    "edad": 25
}

print(f"Ciudad de {persona['nombre']}?")
try:
    print(f"La ciudad de {persona["nombre"]} es:", persona["ciudad"])
except KeyError:
    print("¡Error! La clave 'ciudad' no existe en el diccionario (KeyError)")
