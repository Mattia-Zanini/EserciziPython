# Dizionari
from typing import ItemsView


itmes = {"latte":3, "riso":2, "tofu":5}
print(itmes)

itmes["latte"]# otteniamo il valore

itmes["cereali"] = 1# aggiunge la chiave "cereali" con valore 1
print(itmes)

itmes["yougurt"] = {"fragole":2, "bianco":3}# così inseriamo un dizionario dentro il dizionario items
print(itmes)

itmes["yougurt"]["fragole"]# --> 2
# per mostrare solo le chiavi del nostro dizionario
itmes.keys()

keys = list(itmes.keys())
print(keys[0])

values = list(itmes.values())# per ottenere solo i valori, ne lcaso di yougurt
                             # otterremo l'altro dizionario
                             
print(values)