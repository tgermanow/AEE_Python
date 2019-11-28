import os
import csv

print("Working dir", os.getcwd())


with open("materiaalit/Kuntien avainluvut.csv") as f:
    _reader = csv.reader(f, delimiter=";")
    _otsikko = next(_reader)
    print("Otsikko:", _otsikko)
    print("Otsikko uudetaan: ", 
    for rivi in f:
        print(rivi)

