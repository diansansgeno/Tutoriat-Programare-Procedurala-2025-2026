"""Tutoriat 3 PP
- liste
- functii
- fisiere
- dictionare
"""

# Ex1:

# n = input()
# n = int(n)
# #
# l = []
# # # a + b
# for i in range(n):
#     x = input()
#     x = int(x)
#     l.append(x)
# # set = set(l)
# # s1 = sorted(set)
# # print(s1)
# # #c
# # neg_list = [x for x in l if x < 0]
# # print(neg_list)
# # #d
# #
# T = tuple(filter(lambda x: (99 < abs(x) <= 999), l))
# print(T)

# Ex2:
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
                d[profil][clasa] = []
            d[profil][clasa].extend((cnp, nume, prenume, clasa, medie))
    return d

print(citeste_date())



