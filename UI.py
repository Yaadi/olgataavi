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
        global Integr
        Försteri_raadius=0.105*pow(Kapparuut*Kvantsaagis*pow(n,-4)*J, 1/6)
        siltRadius = ttk.Label(root, text="Försteri raadius on (Å): ")
        siltRadius.grid(column=0, padx=20, pady=10, row=109)
        text = Text(root, height=1, width=15)
        text.grid(column=1, row=109, sticky=E)
        text.insert(INSERT, round(Försteri_raadius,6))

root.title("Fluorestsentsspektrid")
root.geometry("1000x300")

# Doonormolekuli kvantsaagise küsimine
siltQ = ttk.Label(root, text="Doonori kvantsaagis")
siltQ.grid(column=0, padx=20, pady=10, row=2)
textQ = ttk.Entry(root)
textQ.grid(column=1, row = 2, sticky = E)

# Aktseptori neeldumiskoefitsiendi küsimine
siltE = ttk.Label(root, text="Aktseptori neeldumiskoefitsient")
siltE.grid(column=3, padx=20, pady=10, row=2)
textE = ttk.Entry(root)
textE.grid(column=4, row = 2, sticky = E)

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
    global J
    if (checkFile()):
        J = calculation(DonorFile, AkseptorFile, textE.get())
        siltIntegr = ttk.Label(root, text="Kattumisintegraal: ")
        siltIntegr.grid(column=0, padx=20, pady=10, row=101)
        textI = Text(root, height=1, width=15)
        textI.grid(column=1, row=101, sticky=E)
        textI.insert(INSERT, J)
        
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
generateButton.grid(column=2, row=100, sticky=(N, S, W, E))

generateButton = ttk.Button(root, text="Graafik", command=joonista)
generateButton.grid(column=2, row=99, sticky=(N, S, W, E))

generateButton = ttk.Button(root, text="Integreerimine", command=integr)
generateButton.grid(column=2, row=98, sticky=(N, S, W, E))

root.mainloop()
