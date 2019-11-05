"""
Kysyy luvun, tulostaa luvun ja sen lukusumman ja tulon
"""


def lukusumma(num):
    summa = 0
    for x in list(range(1, n+1)):
        summa += x

    return summa


def lukutulo(num):
    tulo = 1
    for x in list(range(1, n+1)):
        tulo *= x

    return tulo


n = int(input("Luku: "))

print("Luku:", n)
print("Lukusumma:", lukusumma(n) )
print("Lukutulo:", lukutulo(n) )
