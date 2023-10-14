number_1 = input("Ingresa el primer número ")
number_2 = input("Ingresa el segundo número ")

number_1 = int(number_1)
number_2 = int(number_2)

sum = number_1 + number_2
les = number_1 - number_2
mul = number_1 * number_2
div = number_1 / number_2

message = f"""
Para los números {number_1} y {number_2}:
La suma es {sum}.
La resta es {les}.
La multiplicación es {mul}.
La divición es {div}.
"""

print(message)

# Conversion of data
# x = input("Cualquier dato")

# int()
# str()
# float()
# bool() 
print(bool(""))
print(bool("0"))
print(bool(None))
print(bool(" "))
print(bool(0))

# Logical Comparators
print("Logical Comparators")
print(1 < 2)
print(1 > 2)
print(1 <= 2)
print(1 >= 2)
print(1 == 2)
print(1 != 2)

# Consitionals
age = 62
if age > 54 :
    print("\nTienes un descuento")
elif age > 17 :
    print("\nPuede ver la pelicula")
else :
    print("\nNo puedes ver la pelicula")
print("Listo...")

# Ternary Conditions
message_2 = "Es mayor " if age > 17 else "Es menor "
print(message_2)