"Lab 2 - Programarea Algoritmilor"

# Ex #1:
#
# n = input("Introduceti un numar: ")
# n = int(n)
# copan = n
# rev = 0
# while copan != 0:
#     rev = rev * 10 + copan % 10
#     copan = copan // 10
# if rev == n:
#     print(f"Numarul {n} este palindrom.")
# else:
#     print(f"Numarul {n} nu este palindrom. Inversul lui este: {rev}")
#
# # Ex #2:
#
# [l1, l2] = input("Introduceti marimile: ").split()
# l1 = int(l1)
# l2 = int(l2)
# surface_area = l1 * l2
# while l1 != 0 and l2 != 0:
#     if l1>l2:
#         l1 -= l2
#     else:
#         l2 -= l1
#
# print(f"Numarul de placi este: {surface_area // l1**2}, iar dimensiune maxima a placii este {l1}")

# Ex #3

# [a,b] = input().split()
# a = int(a)
# b = int(b)
# f1 = 0
# f2 = 1
# f3 = 0
# num = 0
# while f1+f2 <= b:
#     if a <= f1 <= b:
#         num = f1
#         break
#     if a <= f2 <= b:
#         num = f2
#         break
#     f3 = f1 + f2
#     f1 = f2
#     f2 = f3
#     if a <= f3 <=b:
#         num = f3
#         break
# if num < a or num >b:
#     print("Nu exista")
# else:
#     print(num)

# Ex #4

#. . .

# Ex #5:

