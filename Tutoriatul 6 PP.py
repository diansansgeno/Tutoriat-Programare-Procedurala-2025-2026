"""
====== Tutoriatul 6 ======

- tehnici de programare
- recapitulare test lab

"""

"""Testul 2"""

#Ex 1 ::
# a = input().split()
# b = input().split()
#
# a = list(map(int, a))
# b = list(map(int, b))
#
# c = []
#
# for x in a:
#     if x in b and x not in c:
#         c.append(x)
#
# c = sorted(c, key=lambda x: -x)      #lambda x:-x   ---> filtru pentru nr luate invers/descrescator
#
# print(c)
#
# t = tuple([x for x in c if x > 0])
# print(t)
#
# d = list(map(lambda x:  int(str(x)[:2]), t))
# print(d)

#Ex 2 ::

f = open('date2.txt', 'r')

d = {}

for line in f:
    line = line.strip().split(", ")
    cod, categorie = line[0].split()
    subcategorie = line[1]
    nume = line[2]
    pret = line[3]
    if len(line) == 5:
        observatii = line[4]
    else:
        observatii = ""

    if categorie not in d:
        d[categorie] = {}
    if subcategorie not in d[categorie]:
        d[categorie][subcategorie] = []

    produs = {
        "cod": cod,
        "nume": nume,
        "pret": pret,
        "observatii": observatii
    }

    d[categorie][subcategorie].append(produs)
f.close()

#print(d)

# for categorie in d:
#     preturi = []
#     for subcategory in d[categorie]:
#         for produs in d[categorie][subcategory]:
#             pret, moneda = produs["pret"].split()
#             pret = float(pret)
#             preturi.append(pret)
#         minim = min(preturi)
#         print(categorie, subcategory, minim)
#abandonam chat

for categ in d:
    for subcat in d[categ]:
        ##in episodul urmator
