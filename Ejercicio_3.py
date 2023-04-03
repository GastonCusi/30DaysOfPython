#data types de tipo numérico
entero = 10

flotante = 10.5

complejo = 10+5j

#data type de tipo string
nombre = "Gastón"

#data type de tipo booleano
true = True

#data type de tipo lista
lista = ["Gastón", 1.94, 32]

#data type de tipo tuple
tupla = ("Gastón", "Argentino", "Humano")

#data type de tipo set
set = {3.14, 254, 365}

#data type de tipo dictionary
dictionary = {
    'Nombre' : 'Gastón',
    'Nacionalidad' : 'Argentina',
    'Edad' : 32
}

#importando el modulo math
import math

#define las coordenadas de los dos puntos
x1 = 2
y1 = 3
x2 = 10
y2 = 8

#calcular la distancia usando la formula de la distancia euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#imprimir el resultado de la distancia entre dos puntos
print("La distancia euclidiana entre los puntos(2, 3) y (10, 8) es: " + distancia)