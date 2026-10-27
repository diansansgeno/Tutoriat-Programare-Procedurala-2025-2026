"""
Tutoriat 2 PP (27/10/2025)
Siruri de numere, liste, tupluri, siruri de caractere
"""

#Ex 1
#
# n = input("Numar, domnule boss:: ")
# n = int(n)
# max = 0
# par = 0
# x_par = 0
# #ls = []
# for i in range (n):
#     x = input()
#     x = int(x)
#     #ls.append(x)
#     if max <= x:
#         max = x
#     if par == 0 and x % 2 == 0:
#         par = 1
#         x_par = x
# if x_par == max:
#     print("Acela;i numar. Diferenta este 0!")
# else:
#     print(max - x_par)

#Ex 2
# [a, b, c] = input("Dati cele 3 numere naturale:: ").split()
# ls = []
# a = int(a)
# ls.append(a)
# b = int(b)
# ls.append(b)
# c = int(c)
# ls.append(c)
# ls_sorted = sorted(ls)
# print(ls_sorted, ls_sorted[::-1])
# print(ls_sorted[2] + 1)

#Ex 3
# [a,b] = input().split()
# a = int(a)
# b = int(b)
# fibo1 = 1
# fibo2 = 1
# fibo3 = 2
# fib = 0
# ok = 0
# while fibo3 <= b:
#     if a <= fibo1 <= b:
#         ok =1
#         fib = fibo1
#         break
#     if a<= fibo2 <= b:
#         ok = 1
#         fib = fibo2
#         break
#     if a<=fibo3 <=b:
#         ok = 1
#         fib = fibo3
#         break
#     else:
#         fibo1 = fibo2
#         fibo2 = fibo3
#         fibo3 = fibo1 + fibo2
# if ok == 1:
#     print(f"Numarul fibonaccci din interval este: {fib}")
# else:
#     print(f"Nu exista un astfe de numar in interval.")
#     print(f"Intervalul {a,b} este prea restrans.")

#Ex 7 (modificat)
"""
in loc de un sir de caractere va fi un list dat"""

ls = [1, 6, 3, 5, 0, 24, 2, 0, 43, 8, 19, 123]
