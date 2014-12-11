from tkinter import *
from tkinter import ttk
from math import pi
from pylab import *

def run(donor_file, akseptor_file):
    #D_andmed=open("Alexa555.txt")
    #A_andmed=open("Alexa647.txt")
    D_andmed=open(donor_file)
    A_andmed=open(akseptor_file)
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