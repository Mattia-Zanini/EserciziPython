from typing import Final
from enum import Enum  # for enum34, or the stdlib version
from caldaia import Caldaia
from stufa import Stufa
from pompaCalore import Pompa
from bolletta import Bolletta

# prezzi al metro cubo
GAS_OLD: Final[float] = 0.5
GAS: Final[float] = 1.049988

# prezzi a kWh
ENERGIA_OLD: Final[float] = 0.3
ENERGIA: Final[float] = 0.276

# tasse, prezzo annuo
QVD: Final[int] = 70
ONERI_SISTEMA: Final[int] = 47
SPESE_TRASPORTO: Final[int] = 8*12

POTERE_CALORIFERO: Final[float] = 10.7

bollette = []
riscaldamento = Enum(
    'Dispositivi', 'caldaia_eco caldaia stufa pompa_eco pompa')


# Confronta i nomi dei vari dispositivi e ritorna 0 per il dispositivo selezionato, altrimenti ritorna il costo del dispositivo
def CostoInstallazione(disp, dispScelto):
    if riscaldamento(dispScelto).name == disp.GetNome():
        return 0
    return disp.GetPrezzoDispositivo()


def SceltaDispositivo():  # Chiede all'utente quale dispositivo tra quelli elencati utilizza
    print("\n\nQuale dispositivo possiedi?:\n" + "1)Caldaia economica\n" + "2)Caldaia a condensazione\n" +
          "3)Stufa\n" + "4)Pompa di calore economica\n" + "5)Pompa di calore di buon livello\n")
    while True:
        val = InputCorretto()
        if (val == 1 or val == 2 or val == 3 or val == 4 or val == 5 or val == 6):
            break
    return val


# Confronta tutte le bollette calcolate e ritorna quella più economica
def DispositivoConveniente(b):
    min = b[0]
    for i in range(0, len(b)):
        if min.GetCostoDecennale() > b[i].GetCostoDecennale():
            min = b[i]
    return min


def InputCorretto():  # Controlla che l'utente inserisca bene i dati (int)
    while True:
        try:
            val = int(input())
            break
        except:
            print("(solo valori interi)")
    return val


def FormattaNome(name):  # Formatta il nome del dispositivo per far capire meglio all'utente qual è il risultato ottenuto
    match name:
        case "caldaia_eco":
            return "Caldaia economica"
        case "caldaia":
            return "Caldaia a condensazione"
        case "stufa":
            return "Stufa"
        case "pompa_eco":
            return "Pompa di calore economica"
        case "pompa":
            return "Pompa di calore di buon livello"


print("Quanti kWh annui consumi?")
kWhAnnui = InputCorretto()
print("Quanti smc annui consumi?")
smcAnnui = InputCorretto()

# Creazione dei diversi oggetti Dispositivo
caldaia_eco = Caldaia(0.9, riscaldamento.caldaia_eco.name)
caldaia_eco.CalcUtilizzo(kWhAnnui, POTERE_CALORIFERO)
caldaia_eco.CalcCosto(smcAnnui, GAS, QVD + ONERI_SISTEMA + SPESE_TRASPORTO)
print(
    f"Caldaia Eco\nRendimento: {caldaia_eco.GetRendimento()}\nCosto: {caldaia_eco.GetCosto()}€")

caldaia = Caldaia(1, riscaldamento.caldaia.name)
caldaia.CalcUtilizzo(kWhAnnui, POTERE_CALORIFERO)
caldaia.CalcCosto(smcAnnui, GAS, QVD + ONERI_SISTEMA + SPESE_TRASPORTO)
print(
    f"\nCaldaia\nRendimento: {caldaia.GetRendimento()}\nCosto: {caldaia.GetCosto()}€")

stufa = Stufa(1, riscaldamento.stufa.name)
stufa.CalcUtilizzo(smcAnnui, POTERE_CALORIFERO)
stufa.CalcCosto(kWhAnnui, ENERGIA, QVD + ONERI_SISTEMA + SPESE_TRASPORTO)
print(f"\nStufa\nCosto: {stufa.GetCosto()}€\n")

pompa = Pompa(3.6, riscaldamento.pompa.name)
pompa.CalcUtilizzo(smcAnnui, POTERE_CALORIFERO)
pompa.CalcCosto(kWhAnnui, ENERGIA, QVD + ONERI_SISTEMA + SPESE_TRASPORTO)
print(
    f"Pompa di calore ultra\nRendimento: {pompa.GetRendimento()}\nCosto: {pompa.GetCosto()}€\n")

pompa_eco = Pompa(2.8, riscaldamento.pompa_eco.name)
pompa_eco.CalcUtilizzo(smcAnnui, POTERE_CALORIFERO)
pompa_eco.CalcCosto(kWhAnnui, ENERGIA, QVD + ONERI_SISTEMA + SPESE_TRASPORTO)
print(
    f"Pompa di calore eco\nRendimento: {pompa_eco.GetRendimento()}\nCosto: {pompa_eco.GetCosto()}€")

# Si chiede all'utente quale dispositivo possiede
dispositivo = SceltaDispositivo()

# Creazione dei diversi oggetti Bolletta
bollette.append(Bolletta(riscaldamento.caldaia.name,
                caldaia.GetCosto(), CostoInstallazione(caldaia, dispositivo)))
bollette.append(
    Bolletta(riscaldamento.caldaia_eco.name, caldaia_eco.GetCosto(), CostoInstallazione(caldaia_eco, dispositivo)))
bollette.append(Bolletta(riscaldamento.stufa.name,
                stufa.GetCosto(), CostoInstallazione(stufa, dispositivo)))
bollette.append(Bolletta(riscaldamento.pompa.name,
                         pompa.GetCosto(), CostoInstallazione(pompa, dispositivo)))
bollette.append(Bolletta(riscaldamento.pompa_eco.name,
                         pompa_eco.GetCosto(), CostoInstallazione(pompa_eco, dispositivo)))

# Si ottiene qual è il dispositivo più conveniente tramite la sua bolletta
dispConveniente = DispositivoConveniente(bollette)
print(
    f"Questo è il dispositivo meno costoso: {FormattaNome(dispConveniente.GetNomeDispositivo())}\ncon {dispConveniente.GetCostoDecennale()}€ in 10 anni più eventuale installazione")
print("\n===============================================================")
