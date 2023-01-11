subor=open('skok_do_dialky.txt')
krajiny = {}
maxdlzka=0
vitazi=[]
for riadok in subor:
    dlzka=0
    udaje=riadok.split()
    krajiny[udaje[1]] = krajiny.get(udaje[1], 0) + 1

    for i in range(5):
        dlzka=max(dlzka, int(udaje[i+2]))
    if dlzka > maxdlzka:
        maxdlzka = dlzka
        vitazi = [udaje[0]]
    elif dlzka == maxdlzka:
        vitazi.append(udaje[0])
print("Zoznam krajin: ")
for krajina in krajiny:
    print(krajina, end=', ')
print()
print("Pocty sportovcov: ")
for dvojica in krajiny.items():



    print(dvojica[0], ':', dvojica[1])
print("Najdlhsi skok:", maxdlzka)
for vitaz in vitazi:
    print(vitazi)