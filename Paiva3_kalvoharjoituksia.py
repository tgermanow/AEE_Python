def find(_lista, _etsittava_arvo):
    try:
        return _lista.index(_etsittava_arvo)
    except ValueError as e:
        return -1

def count_even(_lista):
    _summa = 0
    cnt_even = len([x for x in _lista if x % 2 == 0])
    return cnt_even

def reverse_list(_lista):
    return list(reversed(_lista))

    return _lista.reverse()



lista = list(range(1, 10))
print ("Originaali lista {0}".format(lista) )

# H1. find
r = find(lista, 12)
print(r)

# H2. even count
cnt = count_even(lista)
print("Even count {0}".format(cnt))

# h3. reverse list
reversed_list = reverse_list(lista)
print("Kaannetty lista {0}".format(reversed_list))

# Rivinvaihtojen poisto lopusta == rstrip()
testiteksti =   "paljon \nrivin \n vaihtoja  \npaljon  \nrivin  \nvaihtoja\n\n\n\n\n\n\n\n"

print(testiteksti)
print("------")
print(testiteksti.rstrip())


