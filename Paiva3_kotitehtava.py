'''
* Lue kuntatilasto csv kirjastolla listamuuttujiin: kunnat, asukkaat, kasvu, tyollisuus
** PK-seudun asukasluku; Espoo, Helsinki, Vantaa, Kauniainen
** Suurin ja pienin kunta
** Suurin ja pienen tyottamyysaste
'''

import csv


path_to_src_file = "materiaalit/Kuntien avainluvut.csv"

kunnat, asukkaat, kasvu, tyollisuus = [], [], [], []

def clear_lists():
    kunnat.clear()
    asukkaat.clear()
    kasvu.clear()
    tyollisuus.clear()

def parse_src_to_lists_dictreader(filename):
    clear_lists()
    with open(filename) as f:
        _reader = csv.DictReader(f, delimiter=";")
        for r in _reader:
            kunnat.append(r["Nimi"])
            asukkaat.append(float(r["Väkiluku 2017"]))
            kasvu.append(float(r["Väkiluvun muutos %"]))
            tyollisuus.append(float(r["Työllisyysaste %"]))

def parse_src_to_lists(filename):
    clear_lists()
    with open(filename) as f:
        _reader = csv.reader(f, delimiter=";")
        next(_reader)  # consuming the header row
        for r in _reader:
            kunnat.append(r[0])
            asukkaat.append(float(r[1]))
            kasvu.append(float(r[2]))
            tyollisuus.append(float(r[3]))

def get_pk_seudun_asukasluku():
    pk_kunnat = ["Helsinki", "Espoo", "Vantaa", "Kauniainen"]
    asukasluku = 0

    for kunta in pk_kunnat:
        index_of_kunta = kunnat.index(kunta)
        kunnan_asukasluku = asukkaat[index_of_kunta]
        asukasluku += kunnan_asukasluku
        #print("{0} asukasluku on {1}".format(kunta, kunnan_asukasluku) )

    return asukasluku

def get_suurin_kunta():
    index = asukkaat.index(max(asukkaat))
    return kunnat[index], max(asukkaat)

def get_pienin_kunta():
    index = asukkaat.index(min(asukkaat))
    return kunnat[index], min(asukkaat)

def get_suurin_tyollisyys():
    index = tyollisuus.index(max(tyollisuus))
    return kunnat[index], max(tyollisuus)

def get_pienin_tyollisyys():
    index = tyollisuus.index(min(tyollisuus))
    return kunnat[index], min(tyollisuus)



parse_src_to_lists(path_to_src_file)
parse_src_to_lists_dictreader(path_to_src_file)

print("PK-seudun asukasluku: ", get_pk_seudun_asukasluku() )
print("Suurin kunta on", get_suurin_kunta())
print("Pienin kunta on", get_pienin_kunta())
print("Suurin tyollisyys", get_suurin_tyollisyys())
print("Pienin tyollisyys", get_pienin_tyollisyys())