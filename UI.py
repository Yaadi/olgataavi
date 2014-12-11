# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from draw import run
from integr import calculation
from tkinter import ttk
from math import pi

root = Tk()
DonorFile = ""
AkseptorFile = ""

#DoonoriPaariNr=0
#AktseptoripaariNr=0

def FosterRadius():
    try:
        Kvantsaagis = float(textQ.get())
        if (Kvantsaagis <= 1):
            error = False
        else:
            error = True
    except:
        error = True
    if (error):
        messagebox.showwarning("WARNING", "Doonori kvantsaagise väärtus saab olla 0 ja 1 vahel")
    else:
        # Konstandid
        Kapparuut=2/3  # Doonori ja aktseptori üleminekudipoolide orientatsioon
        N=6.0221*1e23  # Avogadro
        n=1.35  # Keskkonna murdumisnäitaja
        # Försteri raadiuse arvutamine
        Försteri_raadius=(9000*2.30258*Kapparuut*Kvantsaagis)/(128*pow(pi,5)*N*pow(n,4))
        siltRadius = ttk.Label(root, text="Försteri raadius on: ")
        siltRadius.grid(column=0, padx=20, pady=10, row=101)
        text = Text(root, height=1, width=15)
        text.grid(column=1, row=101, sticky=E)
        text.insert(INSERT, Försteri_raadius)



# def lisaDoonoriPaari():
#     global DoonoriPaariNr
#     global DoonoriReaNr
#     DoonoriPaariNr += 1
#     #Lainepikkuse küsimine
#     siltLainepikkus = ttk.Label(root, text="Doonori lainepikkus:")
#     siltLainepikkus.grid(column=0, padx=20, pady=10, row=DoonoriReaNr )
#     textLainepikkus = ttk.Entry(root)
#     textLainepikkus.grid(column=1, row = DoonoriReaNr, sticky = E)
#
#     #Suhtelise intensiivsuse küsimine
#     siltSuhtelineIntensiivsus = ttk.Label(root, text="Suhteline intensiivsus:")
#     siltSuhtelineIntensiivsus.grid(column=0, padx=20, pady=10, row=DoonoriReaNr + 1 )
#     textSuhtelineIntensiivsus = ttk.Entry(root)
#     textSuhtelineIntensiivsus.grid(column=1, row = DoonoriReaNr + 1, sticky = E)
#     DoonoriReaNr += 2
    
# def lisaAktseptoriPaari():
#     global AktseptoripaariNr
#     global AktseptoriReaNr
#     AktseptoripaariNr += 1
#     #Lainepikkuse küsimine
#     siltLainePikkus = ttk.Label(root, text="Aktseptori lainepikkus:")
#     siltLainePikkus.grid(column=3, padx=20, pady=10, row=AktseptoriReaNr )
#     textLainePikkus = ttk.Entry(root)
#     textLainePikkus.grid(column=4, row = AktseptoriReaNr, sticky = E)
#
#     #Suhtelise intensiivsuse küsimine
#     siltSuhtelineIntensiivsus = ttk.Label(root, text="Suhteline intensiivsus:")
#     siltSuhtelineIntensiivsus.grid(column=3, padx=20, pady=10, row=AktseptoriReaNr + 1 )
#     textSuhtelineIntensiivsus = ttk.Entry(root)
#     textSuhtelineIntensiivsus.grid(column=4, row = AktseptoriReaNr + 1, sticky = E)
#     AktseptoriReaNr += 2

root.title("Fluorestsentsspektrid")
root.geometry("1000x300")

# Doonori maksimaalse emissiooni lainepikkuse küsimine
#siltDMax = ttk.Label(root, text="Doonori emissioonimaksimum")
#siltDMax.grid(column=0, padx=20, pady=10, row=1)
#textDMax = ttk.Entry(root)
#textDMax.grid(column=1, row = 1, sticky = E)

# Doonormolekuli kvantsaagise küsimine
siltQ = ttk.Label(root, text="Doonori kvantsaagis")
siltQ.grid(column=0, padx=20, pady=10, row=2)
textQ = ttk.Entry(root)
textQ.grid(column=1, row = 2, sticky = E)

# Aktseptori maksimaalse neelduvuse lainepikkuse küsimine
#siltAMax = ttk.Label(root, text="Aktseptori neeldumismaksimum")
#siltAMax.grid(column=3, padx=20, pady=10, row=1)
#textAMax = ttk.Entry(root)
#textAMax.grid(column=4, row = 1, sticky = E)

# Aktseptori neeldumiskoefitsiendi küsimine
siltE = ttk.Label(root, text="Aktseptori neeldumiskoefitsient")
siltE.grid(column=3, padx=20, pady=10, row=2)
textE = ttk.Entry(root)
textE.grid(column=4, row = 2, sticky = E)

#DoonoriReaNr = 7
#lisaDoonoriPaari()

#AktseptoriReaNr = 7
#lisaAktseptoriPaari()

#DoonoriPaariButton = ttk.Button(root, text="Lisa doonoripaari", command=lisaDoonoriPaari)
#DoonoriPaariButton.grid(column=1, row=97, sticky=(N, S, W, E))

#AktseptoriPaariButton = ttk.Button(root, text="Lisa aktseptoripaari", command=lisaAktseptoriPaari)
#AktseptoriPaariButton.grid(column=4, row=97, sticky=(N, S, W, E))


def donorFile():
    global DonorFile
    Label(root, text="Doonormolekuli andmete fail")
    DonorFile = filedialog.askopenfilename(parent=root)
    splittedDonor = DonorFile.split("/")
    siltDonorFile = ttk.Label(root, text=splittedDonor[len(splittedDonor ) - 1])
    siltDonorFile.grid(column=1, padx=20, pady=10, row=52)



def akseptorFile():
    global AkseptorFile
    Label(root, text="Aktseptormolekuli andmete fail")
    AkseptorFile = filedialog.askopenfilename(parent=root)
    splittedAkseptor= AkseptorFile.split("/")
    siltAkseptorFile = ttk.Label(root, text=splittedAkseptor[len(splittedAkseptor ) - 1])
    siltAkseptorFile.grid(column=4, padx=20, pady=10, row=52)


def joonista():
    global DonorFile
    global AkseptorFile
    if (checkFile()):
        run(DonorFile, AkseptorFile)

def integr():
    global DonorFile
    global AkseptorFile
    if (checkFile()):
        result = calculation(DonorFile, AkseptorFile, textE.get())
        siltIntegr = ttk.Label(root, text="Kattumisintegraal: ")
        siltIntegr.grid(column=0, padx=20, pady=10, row=109)
        text = Text(root, height=1, width=15)
        text.grid(column=1, row=109, sticky=E)
        text.insert(INSERT, result)


def checkFile():
    global DonorFile
    global AkseptorFile
    if (len(DonorFile) > 3 or len(AkseptorFile) > 3):
        return True
    else:
        messagebox.showwarning("WARNING", "Doonori ja Aktseptori failid peavad olema valitud")
        return False

DoonoriPaariButton = ttk.Button(root, text="Lisa doonormolekuli andmed failist", command=donorFile)
DoonoriPaariButton.grid(column=1, row=51, sticky=(N, S, W, E))

AktseptoriPaariButton = ttk.Button(root, text="Lisa aktseptormolekuli andmed failist", command=akseptorFile)
AktseptoriPaariButton.grid(column=4, row=51, sticky=(N, S, W, E))

generateButton = ttk.Button(root, text="Arvuta Försteri raadius!", command=FosterRadius)
generateButton.grid(column=2, row=98, sticky=(N, S, W, E))

generateButton = ttk.Button(root, text="Graafik", command=joonista)
generateButton.grid(column=2, row=99, sticky=(N, S, W, E))

generateButton = ttk.Button(root, text="Integreerimine", command=integr)
generateButton.grid(column=2, row=100, sticky=(N, S, W, E))

root.mainloop()
