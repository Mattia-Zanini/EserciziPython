from typing import cast


name = input("ciao come ti chiami?")
print(name)

grandpa_age = input("quanti anni ha tuo nonno?")
# python non è tipizzato, cioè non bisogna specificare a
# priori il valore di una variabile

var = "ciao"
type(var)# per vedere il tipo della variabile
print(var)

var = 3.5# riassegno la variabile ad un altro tipo di dato
type(var)
print(var + 5)

var = True
type(var)
print(var)
# si può convertire un tipo di dato in un altro tipo

var = 5
var = str(5)
type(var)
print(var)

var = "10"
var = int(var)
type(var)

var = "4.89"
var = float(var)
type(var)

num = input("inserisci un numero: ")
try:
    type(num)
    num = int(num)
    print("Il numero che hai inserito è",num)
except ValueError: # nel caso si dovesse presentare l'errore di tipo
                   # ValueError succede questo
    print("Il dato che non hai inserito non è un numero")
    
