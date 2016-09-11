from no import No
from array import *
class ListaEncadeada:
    raiz = None
    def __init__ (self, No):
        self.raiz = No


    def insereNo(self,No):
        aux = self.raiz
        while(aux.proximo!=None):
            aux = aux.getProximo()
        aux.setProximo(No)

    def imprimeNo(self):
        aux = self.raiz
        while(aux!=None):
            print "\nX:"
            print aux.getValorX()
            print "Y:"
            print aux.getValorY()
            aux = aux.getProximo()
        print "Fim"

    def SendVectorX(self):
        aux= self.raiz
        cont = 0
        arrayX = array("f")
        while(aux!=None):
            arrayX.insert(cont,aux.getValorX())
            cont = cont+1
            aux = aux.getProximo()
        return arrayX
            
    def SendVectorY(self):
        aux= self.raiz
        cont = 0
        arrayY = array("f")
        while(aux!=None):
            arrayY.insert(cont,aux.getValorY())
            cont = cont+1
            aux = aux.getProximo()
        return arrayY

            
            
