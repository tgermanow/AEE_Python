"""
Kysyy lukuja kunnes käyttäjä antaa luvun -1
• Tallentaa annetut luvut listaan
• Käy läpi listan ja laskee sen keskiarvon

"""

annetut_luvut = []
n = 0

while n != -1:
    n = float(input("Anna luku:"))
    if n != -1:
        annetut_luvut.append(n)

print("Keskiarvo:", sum(annetut_luvut)/len(annetut_luvut))
