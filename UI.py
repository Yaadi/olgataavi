from tkinter import *
from tkinter import ttk
from math import pi

root = Tk()
DoonoriPaariNr=0
AktseptoripaariNr=0


def FosterRadius():
    siltRadius = ttk.Label(root, text="Försteri raadius on:")
    siltRadius.grid(column=0, padx=20, pady=10, row=99)
    text = Text(root, height=1, width=15)
    text.grid(column=1, row=99, sticky=E)
    text.insert(INSERT, "TODO")

def lisaDoonoriPaari():
    global DoonoriPaariNr
    global DoonoriReaNr
    DoonoriPaariNr += 1
    #Lainepikkuse küsimine
    siltLainepikkus = ttk.Label(root, text="Doonori lainepikkus:")
    siltLainepikkus.grid(column=0, padx=20, pady=10, row=DoonoriReaNr )
    textLainepikkus = ttk.Entry(root)
    textLainepikkus.grid(column=1, row = DoonoriReaNr, sticky = E)

    #Suhtelise intensiivsuse küsimine
    siltSuhtelineIntensiivsus = ttk.Label(root, text="Suhteline intensiivsus:")
    siltSuhtelineIntensiivsus.grid(column=0, padx=20, pady=10, row=DoonoriReaNr + 1 )
    textSuhtelineIntensiivsus = ttk.Entry(root)
    textSuhtelineIntensiivsus.grid(column=1, row = DoonoriReaNr + 1, sticky = E)
    DoonoriReaNr += 2
    
def lisaAktseptoriPaari():
    global AktseptoripaariNr
    global AkseptoriReaNr
    AktseptoripaariNr += 1
    #Lainepikkuse küsimine
    siltLainePikkus = ttk.Label(root, text="Aktseptori lainepikkus:")
    siltLainePikkus.grid(column=3, padx=20, pady=10, row=AkseptoriReaNr )
    textLainePikkus = ttk.Entry(root)
    textLainePikkus.grid(column=4, row = AkseptoriReaNr, sticky = E)

    #Suhtelise intensiivsuse küsimine
    siltSuhtelineIntensiivsus = ttk.Label(root, text="Suhteline intensiivsus:")
    siltSuhtelineIntensiivsus.grid(column=3, padx=20, pady=10, row=AkseptoriReaNr + 1 )
    textSuhtelineIntensiivsus = ttk.Entry(root)
    textSuhtelineIntensiivsus.grid(column=4, row = AkseptoriReaNr + 1, sticky = E)
    AkseptoriReaNr += 2
root.title("Fluorestsentsspektrid")
root.geometry("800x800")

# Doonori maksimaalse neelduvuse lainepikkuse küsimine
siltDMax = ttk.Label(root, text="Doonori neeldumismaksimum")
siltDMax.grid(column=0, padx=20, pady=10, row=1)
textDMax = ttk.Entry(root)
textDMax.grid(column=1, row = 1, sticky = E)

# Doonormolekuli kvantsaagise küsimine
siltQ = ttk.Label(root, text="Doonori kvantsaagis")
siltQ.grid(column=0, padx=20, pady=10, row=2)
textQ = ttk.Entry(root)
textQ.grid(column=1, row = 2, sticky = E)

# Aktseptori maksimaalse neelduvuse lainepikkuse küsimine
siltAMax = ttk.Label(root, text="Aktseptori neeldumismaksimum")
siltAMax.grid(column=3, padx=20, pady=10, row=1)
textAMax = ttk.Entry(root)
textAMax.grid(column=4, row = 1, sticky = E)

# Aktseptori neeldumiskoefitsiendi küsimine
siltQ = ttk.Label(root, text="Aktseptori neeldumiskoefitsient")
siltQ.grid(column=3, padx=20, pady=10, row=2)
textQ = ttk.Entry(root)
textQ.grid(column=4, row = 2, sticky = E)

DoonoriReaNr = 7
lisaDoonoriPaari()

AkseptoriReaNr = 7
lisaAktseptoriPaari()

DoonoriPaariButton = ttk.Button(root, text="Lisa doonoripaari", command=lisaDoonoriPaari)
DoonoriPaariButton.grid(column=1, row=97, sticky=(N, S, W, E))

AkseptoriPaariButton = ttk.Button(root, text="Lisa akseptoripaari", command=lisaAktseptoriPaari)
AkseptoriPaariButton.grid(column=4, row=97, sticky=(N, S, W, E))

generateButton = ttk.Button(root, text="Arvuta Försteri raadius!", command=FosterRadius)
generateButton.grid(column=1, row=98, sticky=(N, S, W, E))

# Konstandid
Kapparuut=2/3  # Doonori ja aktseptori üleminekudipoolide orientatsioon
N=6.0221*1e23  # Avogadro
n=1.35  # Keskkonna murdumisnäitaja

root.mainloop()
