#Ex 1
# print("dati niste numere: ")
# [a,b] = input().split()
# a = int(a)
# b = int(b)
# print (a+b, a*b)
# print (a+b, a*b, sep = ",")
# print (a+b, a*b, sep = "\n")
# sumo = a+b
# prod = a*b
# print(f"Suma cifrelor este {sumo}, iar produsul numerelor este {prod}")

#Ex 2
# [a,b,c] = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# ok = 1
# if not(0 <= a <= 23):
#     ok = 0
# if not(0 <= b <= 59):
#     ok = 0
# if not(0 <= c <= 59):
#     ok = 0
# if  ok == 1:
#     print("Numerele date reprezinta ore, minute si respectiv secunde.")
#     if (10<=a<=23) and (10<=b<=59) and (10<=c<=59):
#         print(f"{a}:{b}:{c}")
#     else:
#         if (10<=a<=23) and (10<=b<=59) and (0<=c<=9):
#             print(f"{a}:{b}:0{c}")
#         else:
#             if 10<=a<=23 and 0<=b<=9 and 0<=c<=9:
#                 print(f"{a}:0{b}:0{c}")
#             else:
#                 if 10<=a<=23 and 0<=b<=9 and 10<=c<=59:
#                     print(f"{a}:0{b}:{c}")
#                 else:
#                     if 0<=a<=9 and 10<=b<=59 and 10<=c<=59:
#                         print(f"0{a}:{b}:{c}")
#                     else:
#                         if 0<=a<=9 and 10<=b<=59 and 0<=c<=9:
#                             print(f"0{a}:{b}:0{c}")
#                         else:
#                             if 0<=a<=9 and 0<=b<=9 and 10<=c<=59:
#                                 print(f"0{a}:0{b}:{c}")
#                             else:
#                                 if 0<=a<=9:
#                                     print(f"0{a}:0{b}:0{c}")
# else:
#     if ok == 0:
#         print("Numerele nu represinta ore, minute, secunde.")


#Ex 3

# [z,l,a] = input().split()
# a = int(a)
# z = int(z)
# l = int(l)
#
# ok = 1
# if not(0<= a):
#     ok = 0
# if not(1 <= l <= 12):
#     ok = 0
# if not(1 <= z <= 31):
#     ok = 0
# if ok == 1:
#     if l == 2 and z > 29:
#         ok = 0
#     else:
#         if (z == 29 and l == 2 and ((a % 4 == 0 and a % 100 != 0) or a % 400 == 0)) or (l == 2 and z == 28):
#             l = +1
#             z = 1
#         else:
#             if z == 29 and l == 2 and (a % 4 != 0):
#                 ok = 0
#             else:
#                 if (l == 1 or l == 3 or l == 5 or l == 7 or l == 8 or l == 10) and z == 31:
#                     z = 1
#                     l += 1
#                 else:
#                     if l == 12 and z == 31:
#                         a += 1
#                         l += 1
#                         z = 1
#                     else:
#                         if (l == 2 or l == 4 or l == 6 or l == 9 or l == 11) and z == 30:
#                             l += 1
#                             z = 1
#                         else:
#                             z += 1
# print("Data zilei urmatoare in format an/luna/zi ese: ")
# if 1 <= z <= 9 and 1 <= l <= 9:
#     print(f"{a}/0{l}/0{z}")
# else:
#     if 1 <= l <= 9:
#         print(f"{a}/0{l}/{z}")
#     else:
#         if 1 <= z <= 9:
#             print(f"{a}/{l}/0{z}")
#         else:
#             print(f"{a}/{l}/{z}")
# if ok == 0:
#     print ("Numerele nu reprezinta o zi, o luna sau un an.")


#Ex 4
#
# [x,op,y] = input().split()
# x = int(x)
# y = int(y)
# if not(op == '+' or op == '-' or op == '*' or op == '/'):
#     print("Operatorul este gresit")
# else :
#     if op == '+':
#         rez = x + y
#     else:
#         if op == '-' and y > x:
#             rez = y - x
#         else:
#             if op == '-' and y < x:
#                 rez = x - y
#             else:
#                 if op == '*':
#                     rez = x * y
#                 else:
#                     if op == '/':
#                         rez = x / y
# print (f"Rezultatul lui {x}{op}{y} este: ")
# print("{:.4}".format(rez))

#Ex 5

# [a, b, x, y, char1, char2] = input().split()
# a = int(a)
# b = int(b)
# x = float(x)
# y = float(y)
# char1 = str(char1)
# char2 = str(char2)
#
# print(a, b, x, y, char1, char2)
# print(a, x, char1, b, y, char2)
# print(a, b, x, y, char1, char2, sep ="\n")
# print(a, b)
# print(x, y)
# print(char1, char2)

#Ex 6

