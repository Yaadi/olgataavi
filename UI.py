from tkinter import *
from tkinter import ttk
from math import pi
from pylab import *

root = Tk()
DoonoriPaariNr=0
AktseptoripaariNr=0
D_andmed=open("Alexa555.txt")
A_andmed=open("Alexa647.txt")
D_lainepikkus=[]
D_intensiivsus=[]
A_lainepikkus=[]
A_intensiivsus=[]

for rida in D_andmed:
    tükid=rida.strip().split(",")
    D_lainepikkus.append(float(tükid[0]))
    D_intensiivsus.append(float(tükid[1]))
for rida in A_andmed:
    tükid=rida.strip().split(",")
    A_lainepikkus.append(float(tükid[0]))
    A_intensiivsus.append(float(tükid[1]))
A_andmed.close()
D_andmed.close()

X_D=np.linspace(D_lainepikkus[0], D_lainepikkus[-1],num=len(D_lainepikkus))
Y_D=D_intensiivsus
plot(X_D,Y_D)
X_A=np.linspace(A_lainepikkus[0], A_lainepikkus[-1],num=len(A_lainepikkus))
Y_A=A_intensiivsus
plot(X_A,Y_A)
show()


def FosterRadius():
    # Konstandid
    Kapparuut=2/3  # Doonori ja aktseptori üleminekudipoolide orientatsioon
    N=6.0221*1e23  # Avogadro
    n=1.35  # Keskkonna murdumisnäitaja
    # Försteri raadiuse arvutamine
    Försteri_raadius=(9000*2.30258*Kapparuut*int(textQ.get()))/(128*pow(pi,5)*N*pow(n,4))
    
    siltRadius = ttk.Label(root, text="Försteri raadius on: ")
    siltRadius.grid(column=0, padx=20, pady=10, row=99)
    text = Text(root, height=1, width=15)
    text.grid(column=1, row=99, sticky=E)
    text.insert(INSERT, Försteri_raadius)

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
    global AktseptoriReaNr
    AktseptoripaariNr += 1
    #Lainepikkuse küsimine
    siltLainePikkus = ttk.Label(root, text="Aktseptori lainepikkus:")
    siltLainePikkus.grid(column=3, padx=20, pady=10, row=AktseptoriReaNr )
    textLainePikkus = ttk.Entry(root)
    textLainePikkus.grid(column=4, row = AktseptoriReaNr, sticky = E)

    #Suhtelise intensiivsuse küsimine
    siltSuhtelineIntensiivsus = ttk.Label(root, text="Suhteline intensiivsus:")
    siltSuhtelineIntensiivsus.grid(column=3, padx=20, pady=10, row=AktseptoriReaNr + 1 )
    textSuhtelineIntensiivsus = ttk.Entry(root)
    textSuhtelineIntensiivsus.grid(column=4, row = AktseptoriReaNr + 1, sticky = E)
    AktseptoriReaNr += 2
root.title("Fluorestsentsspektrid")
root.geometry("800x800")

# Doonori maksimaalse emissiooni lainepikkuse küsimine
siltDMax = ttk.Label(root, text="Doonori emissioonimaksimum")
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

AktseptoriReaNr = 7
lisaAktseptoriPaari()

DoonoriPaariButton = ttk.Button(root, text="Lisa doonoripaari", command=lisaDoonoriPaari)
DoonoriPaariButton.grid(column=1, row=97, sticky=(N, S, W, E))

AktseptoriPaariButton = ttk.Button(root, text="Lisa aktseptoripaari", command=lisaAktseptoriPaari)
AktseptoriPaariButton.grid(column=4, row=97, sticky=(N, S, W, E))

generateButton = ttk.Button(root, text="Arvuta Försteri raadius!", command=FosterRadius)
generateButton.grid(column=1, row=98, sticky=(N, S, W, E))

root.mainloop()
