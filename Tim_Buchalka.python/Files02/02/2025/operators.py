a = 12 ;import os;os.system('cls')
b = 3
 
print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0
print(a // b) # 4 integer division, rounded down towards minus infinity
print(a % b)  # 0 modulo: the remainder after integer division

print()
# PEMDAS-(Parentheses(), Exponents**, Multiplication*, Division/, Addition+, Subtraction-)-
print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a) / b)





