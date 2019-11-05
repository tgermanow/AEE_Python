annettu_rivi = []

# Lottogridi
hi = 40
lo = 1


def pyyda_ja_validoi_numero() -> (bool, int):
    try:
        luku = int(input("Anna numero:"))

        if not (hi >= luku >= lo):
            print("Numeron tulee olla valilta {} ja {}".format(lo, hi))
        elif luku  in annettu_rivi:
            print("Samaa numeroa ei voi valita toista kertaa")
        else:
            return True, luku

    except ValueError as e:
        print("Anna kokonaisluku")

    return False, 0


while len(annettu_rivi) < 7:
    (valid, luku) = pyyda_ja_validoi_numero()

    if valid:
        annettu_rivi.append(luku)

print("Annettu rivi {}".format(annettu_rivi))

# Formatoidaan tehtävänannon mukaisesti myös str
annettu_rivi_str = ",".join(map(str, annettu_rivi))