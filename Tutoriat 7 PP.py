"""Tutoriatul 7 - Testele de laborator 2/3"""

#Ex 2

# f = open('date2.txt', 'r')
#
# d = {}
#
# for line in f:
#     line = line.strip().split(", ")
#     cod, categorie = line[0].split()
#     subcategorie = line[1]
#     nume = line[2]
#     pret = line[3]
#     if len(line) == 5:
#         observatii = line[4]
#     else:
#         observatii = ""
#
#     if categorie not in d:
#         d[categorie] = {}
#     if subcategorie not in d[categorie]:
#         d[categorie][subcategorie] = []
#
#     # produs = {
#     #     "cod": cod,
#     #     "nume": nume,
#     #     "pret": pret,
#     #     "observatii": observatii
#     # }
#
#     produs = [cod, nume, pret, observatii]
#
#     d[categorie][subcategorie].append(produs)
#
# f.close()
#
# for categorie in d:
#     for subcategorie in d[categorie]:
#         matric = d[categorie][subcategorie]
#
#         produs_minim = matric[0]
#         minim = matric[0][2] #v[0] = minim
#
#         for produs in matric:   # v[i] din v ul meu
#             if produs[2] < minim:
#                 minim = produs[2]
#                 produs_minim = produs
#
#         print("categoria: ", categorie)
#         print("subcategoria: ", subcategorie)
#         print("nume: ", produs_minim[1])
#         print("pret: ", produs_minim[2])
#         print("observatii: ", produs_minim[3])
#
# def creare_fisiere (*subcategorii, dictionar):
#     for sub in subcategorii:
#         f = open(sub + ".txt", "w")
#
#         for categorie in dictionar:
#             if sub in dictionar[categorie]:
#                 for prod in dictionar[categorie][sub]:
#                     f.write(prod[0] + " " + prod[1] + " " + str(prod[2]) + " " + prod[3] + "\n")
#         f.close()
#
# print(creare_fisiere("lactate","bricolaj", "mezeluri", dictionar = d))
#
# import re
#
# def marca(nume_fisier):
#     return re.findall(r"\b[A-Z][a-z0-9]*\b", open(nume_fisier).read())
#
#
# print(marca("lactate.txt"))


# Testul 3 ex 1

a = input().split()
b = input().split()

a = list(map(int, a))
b = list(map(int, b))

T1 = tuple(a)
T2 = tuple(b)

c = []
for element in T1:
    if element > 0 and element in T2 and element not in c:
        c.append(element)

c = sorted(c, key=lambda x: -x)
print(c)

T = tuple([x for x in T1 if x > 0])
print(T)

lista_perechi = list(zip(T1, T2))
print(lista_perechi)

