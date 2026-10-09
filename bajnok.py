eredmenyek = input("1. feladat: Eredménysor: ")


gyozelem = 0
dontetlen = 0
vereseg = 0
for betu in eredmenyek:             
    if betu == "G":
        gyozelem = gyozelem + 1
    elif betu == "D":
        dontetlen = dontetlen + 1
    elif betu == "V":
        vereseg = vereseg + 1
print(f"2. feladat: Győzelem: {gyozelem}, döntetlen: {dontetlen}, vereség: {vereseg}")
pont = gyozelem * 3 + dontetlen * 1
print(f"3. feladat: A csapat {pont} pontot szerzett.")
if vereseg == 0:
    print("4. feladat: Veretlen maradt.")
else:
    print("4. feladat: Volt vereség.")
