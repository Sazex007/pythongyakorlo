lepesek=[6500,8200,4300,10100,7600,12000,5400,9800,3900,11200]
osszeg=0

for lepes in lepesek:
    osszeg=osszeg+lepes
atlag=osszeg/len(lepesek)
print(f"2. feladat: Összesen {osszeg} lépés, átlag: {atlag}")

legtobb = lepesek[0]
legtobb_nap = 1                      
for i in range(1, len(lepesek)):
    if lepesek[i] > legtobb:
        legtobb = lepesek[i]
        legtobb_nap = i + 1         
print(f"3. feladat: A legtöbb lépés: {legtobb}, a {legtobb_nap}. napon.")
darab = 0
for lepes in lepesek:
    if lepes >= 10000:
        darab = darab + 1
print(f"4. feladat: {darab} napon volt legalább 10000 lépés.")
