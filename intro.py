""" Python Introduction """
print("Hola César!!!")
print("Hola Rincón  " * 4)

# Variables
name_course = "Ultimate Python"
name1 = "Cesar rincon"
print(name_course, name1)
alumns = 5000
points = 9.9
publish = True

# Strings
course_name = "Ultimate Python"
couse_decription = """
Ultimate Python,
Este curso me permite aprender
todos los elementos necesarios
para poder trabajar con Python
"""
print(name_course, couse_decription)
print( len(course_name) )
print(couse_decription[3])
print(couse_decription[3:15])
print(couse_decription[:])

# Format String
name = "Cesar"
lastname = "Rincon"
full_name = f"{name} {lastname}"
print(full_name)

# String Methods
animal = " Perrito feliz  "
print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.title())
print(animal.strip())
print(animal.find("rrI"))
print(animal.replace("rr", "m"))
print("rrito" in animal)
print("rrito" not in animal)

# Scape Secuences
name_simple = 'Cesar "Cesrra"'
name_backS = "Cesar \"Cesrra\""
print(name_simple)
print(name_backS)
jum = "Cesar \n Rincon"
print(jum)

# Numbers
number = 2 # integer
decimal = 2.1 # float
imagnate = 2 + 2j # 2 + 2i

number = number + 2
number += 2

print(1 / 3)
print(1 // 3)
print(1 ** 3)

# Functions to Numbers
print(round(1.3))
print(round(1.3))
print(abs(-85)) # absolute vaue

import math

print(math.ceil(1.1))
print(math.floor(1.9999))
print(math.isnan(1.9999))
print(math.pow(10, 3))
print(math.sqrt(9))