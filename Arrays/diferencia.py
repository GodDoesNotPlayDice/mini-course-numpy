from numpy import *
lista = [1,3,5]
matriz = array([2,4,6])

print(lista)
print(matriz)
# Diferencia Lista: [1, 3, 5]  Matriz: [2 4 6], una lista es una coleccion de datos en cambio una matriz es una estructura de datos.

# Listas: No se pueden manejar operaciones aritmeticas de forma directa, de lo contrario en los arrays si es posible manejar directamente operaciones aritmeticas.

matriz = matriz + array([8]) # Se meten de manera individual a cada elemento. (Es porque cada uno esta en un espacio de memoria) [10 12 14]
print(matriz)
a = [1,2,3]
b = [4,5,6]
print(a+b) # lo unico que se hace es sumar ambas listas [1, 2, 3, 4, 5, 6]

a = array([1,2,3])
b = array([4,5,6]) 
print(a+b) # En este caso es distinto ya que aca sumamos 1+4 2+5 3+6 cada valor de forma independiente en su posicion ([5 7 9])

# listas: Secuencia corta (no sea muy grande)
# Array: Generar muchos elementos dentro de un array
# Porque las listas tenemos problemas de memoria pero el array tiene mejor rendimiento de la memoria, ademas de que en las listas tenemos problemas de espacios de memoria no ordenado en caso de los arrays si estan ordenandos.