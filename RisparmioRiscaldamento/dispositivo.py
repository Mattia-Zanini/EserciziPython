class Dispositivo:
    def __init__(self, rendimento, nomeDisp):
        self.rendimento = rendimento
        self.utilizzo = None
        self.prezzoDispositivo = None
        self.nome = nomeDisp

    def CalcUtilizzo(self, consumo, potereCalorifero):
        self.utilizzo = (consumo / (potereCalorifero*self.rendimento))

    def CalcCosto(self, smc_annui, prezzo, tasse):
        self.costo = round(((self.utilizzo + smc_annui)*prezzo)+tasse, 2)

    def GetUtilizzo(self):
        return self.utilizzo

    def GetCosto(self):
        return self.costo

    def GetRendimento(self):
        return self.rendimento

    def GetPrezzoDispositivo(self):
        return self.prezzoDispositivo

    def GetNome(self):
        return self.nome
