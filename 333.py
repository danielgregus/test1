import tkinter
canvas=tkinter.Canvas(width=1000, height=300)
canvas.pack()
def vykreslit():
    subor=open('zastavba_na_ulici.txt', 'r')
    limit=int(entry1.get())
    y=200
    x=10
    for riadok in subor:
        cislo=riadok.split()
        sirka=int(cislo[0])
        vyska=int(cislo[1])
        if vyska>0:
            canvas.create_rectangle(x,y-vyska,x+sirka,y,fill='gray')
        else:
            canvas.create_line(x,y,x+sirka,y,width=6, fill='green')
        x+=sirka
        vyska2=vyska
    subor.close()

entry1=tkinter.Entry()
entry1.pack()
entry1.insert(0, '60')
button1=tkinter.Button(text='vykresli ulicu', command=vykreslit)
button1.pack()
