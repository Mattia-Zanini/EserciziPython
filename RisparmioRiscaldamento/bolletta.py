class Bolletta:
    def __init__(self, nome, c, inst=0):
        self.nomeDispositivo = nome
        self.costo = c
        self.costoDecennale = self.CalcCostoDecennale(inst)

    # Questo metodo viene richiamato quando viene usato l'operatore di uguaglianza
    def __eq__(self, other):
        return self.costo == other.GetCosto()

    def CalcCostoDecennale(self, costoInstallazione):
        return round(self.costo*10 + costoInstallazione, 2)

    def GetCosto(self):
        return self.costo

    def GetCostoDecennale(self):
        return self.costoDecennale

    def GetNomeDispositivo(self):
        return self.nomeDispositivo
