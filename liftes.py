utasok=[72,85,64,91,58,103,77,69,88,95,60,81]
teherbiras=int(input("A lift teherbírása (kg): "))
osszeg = 0
for tomeg in utasok:
    osszeg = osszeg + tomeg
if osszeg <= teherbiras:
    print(f"3. feladat: Az összes tömeg {osszeg} kg. Mindenki elfér.")
else:
    print(f"3. feladat: Az összes tömeg {osszeg} kg. Nem fér el mindenki.")
talalt_index = -1      
i = 0
while i < len(utasok) and talalt_index == -1:
    if utasok[i] > 100:
        talalt_index = i          
    i = i + 1
if talalt_index != -1:
    print(f"4. feladat: Az első 100 kg feletti utas: {talalt_index + 1}. ({utasok[talalt_index]} kg)")
else:
    print("4. feladat: Nincs 100 kg feletti utas.")
