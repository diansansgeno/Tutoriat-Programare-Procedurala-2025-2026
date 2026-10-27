"""
Tutoriatul 4 Programare Procedurala

--> functii
--> stringuri
--> dictionare si extra

"""

#Ex1
#completare exercitiu
def citeste_date():
    d = {}
    with open('date1.txt') as f:
        # f = open ("date1.txt", "r") .....
        # f.close()
        for linie in f:
            cnp, nume, prenume, clasa, medie, profil = linie.strip().split(maxsplit=5)
            medie = float(medie)
            if profil not in d:
                d[profil] = {}

            if clasa not in d[profil]:
                d[profil][clasa] = {}
            if cnp not in d[profil][clasa]:
                d[profil][clasa][cnp]=[]




            d[profil][clasa][cnp].extend((cnp, nume, prenume, clasa, medie))

    return d

d = citeste_date()
print(d)

# b:
media = 0
copil = 0
for profil in d.keys():
    for clasa in d[profil]:
        for cnp in d[profil][clasa]:
            media = media + (float(d[profil][clasa][cnp][4]))
            copil +=1
        media_tot = media/copil
        print(f"Media clasei {clasa} este {media_tot:.2f}")

# c:
def creare_fisier(d, cls):
    with open(f"{cls}B.txt", "w") as g:
        for profil in d.keys():
            for clasa in d[profil]:
            #if clasu is clasa:
                for cnp in d[profil][clasa]:
                    if clasa==cls:
                        g.write(f"{d[profil][clasa][cnp][0]} {d[profil][clasa][cnp][1]} {d[profil][clasa][cnp][2]} {d[profil][clasa][cnp][3]} {d[profil][clasa][cnp][4]}\n")
                        print(cnp)
creare_fisier(d, 10)

"""A NU SE MAI FACE NIMIC CA E DRQ INTRUCHIPAT"""
