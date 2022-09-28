import tkinter
canvas = tkinter.Canvas(width=500, height=200)
canvas.pack()
farby = ['green', 'red', 'blue', 'orange']  #farby
farby2 = 'zcmo'   #skratka zelena cervena modra tekvicova
x, y, vel = 15, 50, 100



def kocke():
    for i in range(len(farby)):
        canvas.create_rectangle(x+i*vel, y, x+i*vel+vel-2, y+vel-2,  #farebne kocky
                                fill=farby[i])
def klik(sur):
    if y < sur.y < y + vel:
        poradie = (sur.x - x) // vel 
        if 0 <= poradie < len(farby):
            entry = entry1.get()   
            if entry != '':
                subor = open('vyber_jedla.txt', 'a')
                subor.write(entry+' '+farby2[poradie]+'\n')  #pise do suboru 
                subor.close()
canvas.create_text(210, 30, text='VÝBER JEDLA', font='Arial 30', fill='red')
subor = open('vyber_jedla.txt', 'w')
subor.close()


canvas.bind('<Button-1>', klik)
label1 = tkinter.Label(text='kód študenta:')  #text nad entry
label1.pack()
entry1 = tkinter.Entry()  #na pisanie textu
entry1.pack()
kocke()  #def
