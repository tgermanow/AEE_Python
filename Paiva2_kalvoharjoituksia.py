import random
import string
import time

def listharjoitus():
    lista = ["kissa", "koira", "poni", "pupu"]

    print ("Listassa", len(lista), "alkiota")

    while len(lista) > 0:
        print (lista.pop())

    print ("Listassa", len(lista), "alkiota")

    lista = list(range(0, 100))
    print(lista)

merkkijono = "Pitka merkkijono is this"


def merkkijonoharjoitus():
    #for merkki in merkkijono:
    #    print(merkki)

    teksti = "ohjelmointi on kivaa"

    nurin = teksti[-1::-1]
    print(nurin)

    print (teksti)

def suoritus1(inputstr, value):
    if value in inputstr:
        return value.rindex("a")
    else:
        return -1

def suoritus2(inputstr, value):
    try:
        return inputstr.rindex(value)
    except Exception as e:
        return -1

def randomString(letters, stringLength=10):
    """Generate a random string of fixed length """
    #letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


all_chars = string.ascii_lowercase +  string.ascii_uppercase

all_chars_no_A = all_chars.replace("a", '')
all_chars_no_A = all_chars_no_A.replace("A", '')

print(all_chars_no_A)



start = time.time()
verylongstring = randomString(all_chars_no_A, 10**6)
end = time.time()
print("Elapsed on generator:", end - start)

value = 'a'

start = time.time()
suoritus1(verylongstring, value)
end = time.time()
print(end - start)

start = time.time()
suoritus2(verylongstring, value)
end = time.time()
print(end - start)
