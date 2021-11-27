# Set
# insieme di elementi unici non ordinati

names = {"Giuseppe", "Federico", "Antonino", "Matteo", "Federico"}
print(names)# viene rimosso l'elemetno doppio e gli elementi vengono mostrati a caso
            # non nell'ordine in cui sono scritti nel Set
            
# aggiunta di un elemento

names.add("Lorenzo")
print(names)# l'elemento verrà aggiunto in una posizione casuale


# rimuovere un elemento

names.remove("Antonino")
print(names)
#names.remove("Paolo")# restituisce un errore, questo perchè
                     # l'elemento non è presente all'interno del set
names.discard("Paolo")# quando non siamo sicuri che l'elemento
                      # che volgiamo rimuovere dal set sia presente

# estrazione di un elemento

name = names.pop()# l'elemento verrà estratto casualmente
print(name)
print(names)

# svuotamento di un Set
names.clear()
print(names)

# questa invece è una lista
names_List = ["Giuseppe", "Federico", "Antonino", "Matteo", "Federico"]
print(names_List)

names_set = set(names_List)# convertiamo la lista in un set
print(names_set)

# da set a lista

names_List = list(names_set)
print(names_List)

# frozenset ---> set immutabili

names = frozenset({"Giuseppe", "Federico", "Antonino", "Matteo", "Federico"})
#names.pop()# restituisce un errore di tipo AttributeError
           # questo perchè il frozenset è immutabile e quindi non
           # è possibili estrarre degli elementi







