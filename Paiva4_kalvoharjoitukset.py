import csv


def lue_csv(filename):

    kunnat = []
    asukkaat = []
    kasvu = []
    tyollisyys = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader, None) # Skip the header

        for r in csv_reader:
            kunnat.append(r[0])
            asukkaat.append(int(r[1]))
            kasvu.append(float(r[2]))
            tyollisyys.append(float(r[3]))

    return kunnat, asukkaat, kasvu, tyollisyys



aineisto = 'Kuntien avainluvut.csv'
kunnat, asukkaat, kasvu, tyollisyys = lue_csv(aineisto)


