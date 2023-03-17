from datetime import date
print("Hello World")

sum = 1+2
print(sum)

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

print(type(planets_in_solar_system))

#OPERADORES
left_side = 10
right_side = 5
left_side / right_side # 2

# Operadores de asignacion 

print(" = ")
print("+= : x += 2")
#x incrementado en 2. Si contenía 2 antes, ahora tiene un valor de 4.")

print("=+ : x -= 2")
#x reducido en 2. Si contenía 2 antes, ahora tiene un valor de 0

print(" / : x /= 2")
#x dividido por 2. Si contenía 2 antes, ahora tiene un valor de 1.

print(" / : x *= 2")
#x multiplicado por 2. Si contenía 2 antes, ahora tiene un valor de 4.

date.today()
print(date.today())
print("La fecha de hoy es : " , str(date.today()))


import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg

#sys.argv es una matriz o estructura de datos que contiene muchos elementos. La primera posición,
#que se indica como 0 en la matriz, contiene el nombre del programa. La segunda posición, 1, contiene el primer argumento.
#Supongamos que el programa backup.py contiene el código de ejemplo y lo ejecuta de la siguiente manera:
