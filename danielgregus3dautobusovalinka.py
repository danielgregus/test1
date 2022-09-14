import tkinter       #kniznica
canvas = tkinter.Canvas(width=500, height=400, bg='white')     #platno
canvas.pack()    
canvas.focus_set()
subor = open('vytazenost_autobusovej_linky.txt','r',encoding='utf-8')  #otvorenie suboru
kapacita = 0  
zastavka = []
pocet = 0
y = 20
for riadok in subor:
    if kapacita == 0:
        kapacita = int(riadok) #zmeni hodnotu na cele cislo
    else:
        casti = riadok.split() #rozdeli vstupny retazec
        pocet += int(casti[0]) #nastupujuci riadok
        pocet -= int(casti[1]) #vystupujuci riadok
        zastavka.append(pocet) #prida pocet
        canvas.create_text(10, y, text=' '.join(casti[2:]))     #text, join pretoze zastavka moze obsahovat viacej slov
        y += 20




        
def stlacenie(event):
    global y   #globalna premenna
    if len(zastavka) > 0:  
        canvas.create_rectangle(125, y + 10, 225, y + 20)
        aktpocet = zastavka.pop(0) #odstrani prvy prvok a vrati jeho hodnotu
        if aktpocet > kapacita:   
            farba = 'red'
        else:
            farba = 'green'
        canvas.create_rectangle(100, y + 10, 100 + 100 * aktpocet / kapacita,     #obdlznik
                                y + 20, fill=farba)
        y += 20



subor.close() #zavrie subor
y=20
canvas.bind('<Key>', stlacenie)  #stlacenie lubovolnej klavesy


