import csv
import numpy as np
import matplotlib.pyplot as plt

a = np.array([1,2,3,5])
print(a.shape)
print(a.size)

lista = [[1,2,3], [5,6,7], [8,9,10]]
matriisi = np.array(lista)
print(matriisi.shape)
print(matriisi.size)

print(matriisi)
print("pienin alkio {}".format(np.min(matriisi) ))
print("mean alkio {}".format(np.mean(matriisi) ))
print("keskihajonta {}".format(np.std(matriisi) ))

print("linspace {}".format(np.linspace(2,1000,3) ) )

m2 = np.arange(100)
print (m2.reshape( (10,10) ))






def lue_csv(filename):

    kunnat = []
    asukkaat = []
    kasvu = []
    tyollisyys = []
    huoltosuhde = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader, None) # Skip the header

        for r in csv_reader:
            kunnat.append(r[0])
            asukkaat.append(int(r[1]))
            kasvu.append(float(r[2]))
            tyollisyys.append(float(r[3]))
            huoltosuhde.append(float(r[4]))

    return kunnat, asukkaat, kasvu, tyollisyys, huoltosuhde

aineisto = 'Kuntien avainluvut.csv'
kunnat, asukkaat, kasvu, tyollisyys, huoltosuhde = lue_csv(aineisto)

np_asukkaat = np.array(asukkaat)
print("Pienin asukasmäärä {}".format( np.min(np_asukkaat) ))
print("Suurin asukasmäärä {}".format( np.max(np_asukkaat) ))
print("Asukkaiden keskiarvo {}".format( np.mean(np_asukkaat) ))
print("Asukkaiden mediaani {}".format( np.median(np_asukkaat) ))


plt.figure()
plt.plot([1,3,5,6,8,9])
#plt.show()

np_asukkaat = np.array(asukkaat)
np_tyollisyys = np.array(tyollisyys)
np_huoltosuhde = np.array(huoltosuhde)

plt.plot(np_asukkaat, np_tyollisyys, np_huoltosuhde)
plt.show()

