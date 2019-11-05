"""
TARKISTAA ONKO merkki VOKAALI JA
TULOSTAA ”Ostit vokaalin!” TAI ”Ei vokaali”
• TOIMII PIENILLÄ JA ISOILLA KIRJAIMILLA
• VOKAALIT == ”aeiouyåäö”

"""


def ostan_vokaalin(merkki):
    vokaalit = 'aeiouyäöå'
    vokaalit += vokaalit.upper()

    if merkki in vokaalit:
        print( "Ostit vokaalin")
    else:
        print( "Ei vokaali")


ostan_vokaalin("a")
ostan_vokaalin("A")
ostan_vokaalin("x")
ostan_vokaalin("J")

