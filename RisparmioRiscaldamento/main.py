from typing import Final
from caldaia import Caldaia
from stufa import Stufa
from pompaCalore import Pompa

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

caldaia_eco = Caldaia(0.9)
caldaia_eco.CalcUtilizzo(KWH_ANNUI, POTERE_CALORIFERO)
caldaia_eco.CalcCosto(SMC_ANNUI, GAS, QVD + ONERI_SISTEMA + SPESE_TRASPORTO)
print(
    f"Caldaia Eco\nRendimento: {caldaia_eco.GetRendimento()}\nCosto: {caldaia_eco.GetCosto()}€")

caldaia = Caldaia(1)
caldaia.CalcUtilizzo(KWH_ANNUI, POTERE_CALORIFERO)
caldaia.CalcCosto(SMC_ANNUI, GAS, QVD + ONERI_SISTEMA + SPESE_TRASPORTO)
print(
    f"\nCaldaia\nRendimento: {caldaia.GetRendimento()}\nCosto: {caldaia.GetCosto()}€")

stufa = Stufa(1)
stufa.CalcUtilizzo(SMC_ANNUI, POTERE_CALORIFERO)
stufa.CalcCosto(KWH_ANNUI, ENERGIA, QVD + ONERI_SISTEMA + SPESE_TRASPORTO)
print(f"\nStufa\nCosto: {stufa.GetCosto()}€\n")

pompa = Pompa(3.6)
pompa.CalcUtilizzo(SMC_ANNUI, POTERE_CALORIFERO)
pompa.CalcCosto(KWH_ANNUI, ENERGIA, QVD + ONERI_SISTEMA + SPESE_TRASPORTO)
print(
    f"Pompa di calore ultra\nRendimento: {pompa.GetRendimento()}\nCosto: {pompa.GetCosto()}€\n")

pompa_eco = Pompa(2.8)
pompa_eco.CalcUtilizzo(SMC_ANNUI, POTERE_CALORIFERO)
pompa_eco.CalcCosto(KWH_ANNUI, ENERGIA, QVD + ONERI_SISTEMA + SPESE_TRASPORTO)
print(
    f"Pompa di calore eco\nRendimento: {pompa_eco.GetRendimento()}\nCosto: {pompa_eco.GetCosto()}€")
