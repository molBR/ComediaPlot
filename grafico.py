import numpy as np
import matplotlib.pyplot as plt


def ImprimeVector(arrayX,arrayY):
    t1 =(arrayX)
    t2 =(arrayY)
    plt.plot(t1,t2)
    plt.title("Tensao por corrente no diodo")
    plt.ylabel("Corrente")
    plt.show()
