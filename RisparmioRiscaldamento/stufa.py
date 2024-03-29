from dispositivo import Dispositivo


class Stufa(Dispositivo):
    def __init__(self, rendimento, nomeDisp):
        super().__init__(rendimento, nomeDisp)
        self.prezzoDispositivo = 400

    def CalcUtilizzo(self, consumo, potereCalorifero):
        self.utilizzo = ((consumo * potereCalorifero) / self.rendimento)

    def CalcCosto(self, kwh_annui, prezzo, tasse):
        self.costo = round((self.utilizzo + kwh_annui)*prezzo+tasse, 2)
