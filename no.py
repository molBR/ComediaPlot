class No:
    valorX = None
    valorY = None
    proximo = None
    anterior = None
    
    def __init__(self,valorX,valorY):
        self.valorX = valorX
        self.valorY = valorY

    def getValorX(self):
        return self.valorX
    def getValorY(self):
        return self.valorY
    def getProximo(self):
        return self.proximo
    def getAnterior(self):
        return self.anterior
    
    def setValorX(self,valorX):
        self.valorX = valorX
    def setValorY(self,valorY):
        self.valorY = valorY
    def setProximo(self,proximo):
        self.proximo = proximo
    def setAnterior(self,anterior):
        self.anterior = anterior
