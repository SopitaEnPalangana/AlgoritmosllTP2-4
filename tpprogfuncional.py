print("-----------------------------------------------------------------------")
print("Ejercicios del TP2.4 - Programación Funcional en Pyhton - Algoritmos II")
print("-----------------------------------------------------------------------")
#6.1 Obtener el cuadrado de todos los elementos en la lista.
print("Cuadrado de una lista")

lista_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"La lista inicial es: {lista_base}")
print()

#codigo version larga
def cuadrado(elemento=0):
    return elemento * elemento

lista_cuadrados = list( map(cuadrado, lista_base) )

print("Resultado de codigo más largo: ")
print(f"La lista mapeada con cuadrados ahora es: {lista_cuadrados}")
print()
#codigo version shorter

cuadrado = lambda elemento : elemento * elemento
lista_cuadradoss = list( map( cuadrado , lista_base) )
print("Resultado de código más corto:")
print(f"La lista mapeada con cuadrados ahora es: {lista_cuadradoss}")
print()
print("-----------------------------------------------------------------------")
#6.2 Obtengamos la cantidad de elementos mayores a 5 en una tupla.
print("Cantidad de elementos mayores a 5")

tupla_base = (5, 2 ,6 ,7, 8, 10, 77, 55, 2, 1, 30, 4, 2 ,3)
print(f"La tupla inicial es: {tupla_base}")
print()

#codigo version larga
def mayor_a_5(numero):
    return numero > 5

tupla_filtrada = tuple(filter(mayor_a_5, tupla_base))
contador = 0
for numero in tupla_filtrada:
   contador = contador + 1

print("Resultado de código más largo:")
print(f"Los elementos mayores a 5 en la tupla son {contador}: {tupla_filtrada}")
print()

#Y el código puede ser más corto:
tupla_filtradaa = tuple(filter( lambda num: num > 5, tupla_base))
contadora = 0
for num in tupla_filtradaa:
    contadora = contadora + 1

print("Resultado de código más corto:")
print(f"Los elementos mayores a 5 en la tupla son {contadora}: {tupla_filtradaa}")
print()
print("-----------------------------------------------------------------------")
#6.3 Obtengamos la cantidad de elementos mayores a 5 en una tupla, usando Reduce
print()
lista_a = [5, 2 ,6 ,7, 8, 10, 77, 55, 2, 1, 30, 4, 2 ,3]
print(f"La lista inicial es: {lista_a}")
print()

from functools import reduce

def acumulador(contad, elemento):
    if elemento > 5:
        return contad + 1
    else:
        return contad

cantidad = reduce(acumulador, lista_a, 0)
print(f"Los elementos mayores a 5 en la lista son {cantidad}")
print()