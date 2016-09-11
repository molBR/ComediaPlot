from listaencadeada import ListaEncadeada
from no import No
import numbers
import numpy as np
import matplotlib.pyplot as plt
from grafico import ImprimeVector



cond = 0
n = No(0,0)
l = ListaEncadeada(n)
num =0
while(cond==0):
    x = input("Digite o valor de x\n")
    y = input("Digite o valor de y\n")
    if(x == 0 & y==0):
        cond=1
    else:
        n = No(x,y)
        l.insereNo(n)
ImprimeVector(l.SendVectorX(),l.SendVectorY())
