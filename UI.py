from tkinter import *
from tkinter import ttk


root = Tk()
paariNr = 0

def FosterRadius():
    siltRadius = ttk.Label(root, text="Försteri raadius on:")
    siltRadius.grid(column=0, padx=20, pady=10, row=99)
    text = Text(root, height=1, width=15)
    text.grid(column=1, row=99, sticky=E)
    text.insert(INSERT, "TODO")

def lisaPaari():
    global paariNr
    global reaNr
    paariNr += 1
    #Lainepikkuse küsimine
    siltLainePikkus = ttk.Label(root, text="Lainepikkus:")
    siltLainePikkus.grid(column=0, padx=20, pady=10, row=reaNr )
    textLainePikkus = ttk.Entry(root)
    textLainePikkus.grid(column=1, row = reaNr, sticky = E)

    #Suhtelise intensiivsuse küsimine
    siltSuhtelineIntensiivsus = ttk.Label(root, text="Suhtleine intensiivsus:")
    siltSuhtelineIntensiivsus.grid(column=0, padx=20, pady=10, row=reaNr + 1 )
    textSuhtelineIntensiivsus = ttk.Entry(root)
    textSuhtelineIntensiivsus.grid(column=1, row = reaNr + 1, sticky = E)
    reaNr += 2

root.title("Fluorestsents Spektrid")
root.geometry("350x800")

#Maksimaalse küsimine
siltMax = ttk.Label(root, text="Maksimaalne ??????")
siltMax.grid(column=0, padx=20, pady=10, row=1)
textMax = ttk.Entry(root)
textMax.grid(column=1, row = 1, sticky = E)

reaNr = 2
lisaPaari()


paariButton = ttk.Button(root, text="Lisa paari", command=lisaPaari)
paariButton.grid(column=1, row=97, sticky=(N, S, W, E))

generateButton = ttk.Button(root, text="Arvuta Försteri raadius!", command=FosterRadius)
generateButton.grid(column=1, row=98, sticky=(N, S, W, E))

root.mainloop()
