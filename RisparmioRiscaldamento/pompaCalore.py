from dispositivo import Dispositivo


class Pompa(Dispositivo):
    def __init__(self, rendimento):
        super().__init__(rendimento)
        self.prezzo = 3000 if rendimento == 3.6 else 1000

    def CalcUtilizzo(self, consumo, potereCalorifero):
        self.utilizzo = ((consumo * potereCalorifero) / self.rendimento)

    def CalcCosto(self, kwh_annui, prezzo, tasse):
        self.costo = round(((self.utilizzo + kwh_annui)
                           * prezzo)+tasse+self.prezzo, 2)
