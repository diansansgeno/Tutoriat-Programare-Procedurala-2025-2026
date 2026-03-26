"""Tutoriat 8 PP - rezolvari teste 3/4"""

#recap ex 1, test 3

# a = input().split()
# b = input().split()
#
# a = list(map(int, a))
# b = list(map(int, b))
#
# T1 = tuple(a)
# T2 = tuple(b)
#
# c = []
# for element in T1:
#     if element > 0 and element in T2 and element not in c:
#         c.append(element)
#
# c = sorted(c, key=lambda x: -x)
# print(c)
#
# T = tuple([x for x in T1 if x > 0])
# print(T)
#
# lista_perechi = list(zip(T1, T2))
# print(lista_perechi)

"""
Deci, cand ne cere sa citim 2 siruri de numere, le citim clasic cu input().split(), apoi ca sa le memoram
corespunzator in memorie --> list(map(int, a)) adica, o lista, mapatape fiecare element al sirului a citit sa fie
un numar intreg.

tuple() --> ca sa convertim lista in tuple

sorted(lista, key) sorteaza lista lista dupa cheia key de sortare (crescator, descrescator, dupa uc, etc). Key 
va fi exprimat ca o functie locala de tip lambda --> lambda x: -x, de exemplu.

list(zip(tuplu 1, tuplu 2)) --> imperecheaza elementele tuplurilor tuplu 1 si tuplu 2 astfel: primul1-primul2,
aldouilea1 - aldoilea2 etc. Va avea nr de perechi cate elemente are tuplut cu nr minim de elemente. 
"""

#Ex 2 testul 3
f = open('date3.txt', 'r')
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
        observatii = 0

    if categorie not in d:
        d[categorie] = {}

    if subcategorie not in d[categorie]:
        d[categorie][subcategorie] = []

    produs = [cod, nume, pret, observatii]

    d[categorie][subcategorie].append(produs)
f.close()

print(d)

for categorie in d:
    for subcategory in d[categorie]:
        matric = d[categorie][subcategory]

        produs_minim = matric[0]
        for i in range(len(d[categorie][subcategory])):
            if matric[i][3] != 0:
                pret, moneda = matric[i][2].split()
                pret = float(pret)
                discount = matric[i][3].split("%")
                discount = float(discount[0])
                pret = pret - discount * pret / 100
                matric[i][2] = pret
                print(matric[i][2])
            else:
                pret, moneda = matric[i][2].split()
                pret = float(pret)
                matric[i][2] = pret

        pret_minim = matric[0][2]
        #pret_minim = float(pret_minim)
        print(matric)
        for produs in matric:
            pret = matric[i][2]

            print(matric[i][2])
            if pret < pret_minim:
                pret_minim = produs[2]
                produs_minim = produs

        print("categoria:", categorie)
        print("subcategorie", subcategory)
        print("numele:", produs_minim[1])
        print("pret", pret_minim)
        print("discount", produs_minim[3])


