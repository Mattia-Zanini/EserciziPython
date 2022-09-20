class Pompa:
    def __init__(self, rendimento):
        self.rendimento = rendimento
        self.utilizzo = None
        self.costo = None
        self.prezzo = 3000 if rendimento == 3.6 else 1000

    def CalcUtilizzo(self, consumo, potereCalorifero):
        self.utilizzo = ((consumo * potereCalorifero) / self.rendimento)

    def CalcCosto(self, kwh_annui, prezzo, tasse):
        self.costo = round(((self.utilizzo + kwh_annui)
                           * prezzo)+tasse+self.prezzo, 2)

    def GetUtilizzo(self):
        return self.utilizzo

    def GetCosto(self):
        return self.costo

    def GetRendimento(self):
        return self.rendimento
