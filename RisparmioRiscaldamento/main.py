from typing import Final
from caldaia import Caldaia

# prezzi al metro cubo
GAS_OLD: Final[float] = 0.5
# GAS: Final[float] = 1.05
GAS: Final[float] = 1.049988

# prezzi a kWh
ENERGIA_OLD: Final[float] = 0.3
ENERGIA: Final[float] = 0.276

# tasse, prezzo annuo
QVD: Final[int] = 70
ONERI_SISTEMA: Final[int] = 47
SPESE_TRASPORTO: Final[int] = 8*12

KWH_ANNUI: Final[int] = 2700
SMC_ANNUI: Final[int] = 1300
POTERE_CALORIFERO: Final[float] = 10.7

cald = Caldaia(0.9)
cald.CalcUtilizzo(KWH_ANNUI, POTERE_CALORIFERO)
cald.CalcCosto(SMC_ANNUI, GAS, QVD + ONERI_SISTEMA + SPESE_TRASPORTO)
print(f"Rendimento: 0.9\nCosto: {cald.GetCosto()}€")

cald = Caldaia(1)
cald.CalcUtilizzo(KWH_ANNUI, POTERE_CALORIFERO)
cald.CalcCosto(SMC_ANNUI, GAS, QVD + ONERI_SISTEMA + SPESE_TRASPORTO)
print(f"Rendimento: 1\nCosto: {cald.GetCosto()}€")
