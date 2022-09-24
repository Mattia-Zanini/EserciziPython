from dispositivo import Dispositivo


class Caldaia(Dispositivo):
    def __init__(self, rendimento, nomeDisp):
        super().__init__(rendimento, nomeDisp)
        self.prezzoDispositivo = 2000 if rendimento == 1 else 1800
