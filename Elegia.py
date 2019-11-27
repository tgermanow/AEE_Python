from collections import Counter

filename = 'elegia.txt'

sanat = Counter()
rivit = 0
merkit = 0

with open(filename, encoding='utf-8') as elegia:
    sanat = Counter(elegia.read().split())


with open(filename, encoding='utf-8') as elegia:
    for r in elegia:
        rivit = rivit + 1
        for c in r:
            merkit += 1


print("{} sanaa runossa.".format(sum(sanat.values())) )
print("{} riviä runossa.".format(rivit+1 ))
print("{} merkkiä runossa.".format(merkit+1 ))

vokaalilla_alkavat = Counter()


for key, value in sanat.items():
    if key.lower().startswith(("a","e","i","o","y","ä","ö") ):
        vokaalilla_alkavat.update({key: value})

print(vokaalilla_alkavat)



