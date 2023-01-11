subor=open("mena_zamestnancov.txt")
mena=subor.readlines()
subor.close()
for i in range(len(mena)):
    mena[i] = mena[i].strip()
pocet=len(mena) // 2
print("Pocet mien:",pocet)
krstne=mena[:pocet]
priezviska=mena[pocet:]
dlzka=0
for s in priezviska:
    dlzka= max(dlzka, len(s))
print("Najdlhsie priezvisko je", dlzka)
dlzka=0
for s in krstne:
    dlzka=max(dlzka,len(s))
print("Najdlhsie meno je", dlzka)
vystup=open('vystup.txt', 'w')
for i in range(pocet):
    vystup.write(krstne[i] + (' ' * (dlzka - len(krstne[i]) + 1))
                 + priezviska[i]+'\n')
vystup.close()