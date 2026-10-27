"""Tutoriatul 6 - curs 8"""

"""
Recap test lab
"""

#Ex 1 ::
# #a
# n = int(input("dati un numar: "))
# v = []
# for i in range(n):
#     x = int(input())
#     v.append(x)
# print(v)
#
# #v_2 = [int(input()) for i in range(n)]
# #print(v_2)
# #b
#
# v_sorted = sorted(v)
# v_nou = []
# for i in range(n):
#     if v_sorted[i] not in v_nou:
#         v_nou.append(v_sorted[i])
# print(v_nou)
# #c
# neg = [x for x in v if x < 0]
# print(neg)
# #d
#
# T = tuple(filter(lambda x: 99 < x <= 999, v))
# print(T)


#Ex 2 ::

#a
def citeste_date():
    d = {}
    with open('date.txt') as f:
        for line in f:
            cnp, nume, prenume, clasa, medie, profil = line.strip().split(maxsplit = 5)
            medie = float(medie)
            if profil not in d:
                d[profil] = {}
            if clasa not in d[profil]:
                d[profil][clasa] = []
            d[profil][clasa].extend((cnp, nume, prenume, clasa, medie))
    return d
dic = citeste_date()
print(dic)
for profil in dic.keys():
    for clasa in dic[profil].keys():
        media_clasei = 0
        n=len(dic[profil][clasa])
        for i in range(4,n,5):
            media_clasei+=dic[profil][clasa][i]
        #
        # for media in dic[profil][clasa].items():
        #     media_clasei += media
        #     elevi += 1
    print(dic[profil][clasa])
    print(profil, clasa, media_clasei/(n//5))