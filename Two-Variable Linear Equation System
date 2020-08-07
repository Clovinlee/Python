print("""
FORMAT :
a + b = x
c + d = z
""")
a = int(input("Number A : "))
default_a = a
b = int(input("Number B : "))
default_b = b
x = int(input("Number X : "))
c = int(input("Number C : "))
default_c = c
d = int(input("Number D : "))
default_d = d
z = int(input("Number Z : "))
multiplier1 = 1
multiplier2 = 1
while a != c :
    if a > c :
        c = default_c
        multiplier2 += 1
        c = default_c * multiplier2
    elif c > a :
        a = default_a
        multiplier1 += 1
        a = default_a * multiplier1

if multiplier1 > multiplier2 :
    print("Mul1>Mul2")
    final_b = (default_b * multiplier1) - (default_d * multiplier2)
    final_x = (x * multiplier1) - (z * multiplier2)
    final_x = final_x / final_b #Price per B
    final_a = (x - (default_b * final_x)) / default_a
    print("Price A or C : ", final_a)
    print("Price B or D : ", final_x)
elif multiplier2 > multiplier1 :
    print("Mul2>Mul1")
    final_d = (default_d * multiplier2) - (default_b * multiplier1)
    final_z = (z * multiplier2) - (x * multiplier1)
    final_z = final_z / final_d #Price per D
    final_c = (z - (default_d * final_z)) / default_c
    print("Price A or C : ", final_c)
    print("Price B or D : ", final_z)
