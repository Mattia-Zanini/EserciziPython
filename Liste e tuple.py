# Liste
# le liste posso contenere tipi diversi di dati
# tipo my_ListPython = [10, 5.345, "ciao", False]

my_List = [10, 5, 8, 3 , 11, 2]
type(my_List)
len(my_List)

# indexing

my_List[0]
my_List[1]
my_List[-1]

# slicing (seleziona una parte della lista)

my_List[0:3] # 10, 5, 8
my_List[:5] # 10, 5, 8, 3, 11
my_List[2:] # 8, 3 ,11, 2
my_List[:] # 10, 5, 8, 3, 11, 2

# è possibile mettere un terzo valore per indicare il senso della lista
my_List[::] # di default è impostato su [::1] --> 10, 5, 8, 3, 11, 2 da sinistra verso destra
my_List[::-1] # 2, 11, 3, 8 , 5, 10 da destra verso sinistra

# modifica

my_List[0] = 0
print(my_List)

my_List[-2:] = [7,1]
print(my_List) # 0, 5, 8, 3, 7, 1, abbiamo modificato gli ultimi due valori

# verific

animals = ["cane","gatto","topo"]
"uomo" in animals # mostra valore false
"gatto" in animals# mostra valore true

# rimozione per valore

animals.remove("gatto")
print(animals)# "cane" "topo"

# estrazione per valore

animal = animals.pop(1)# andiamo ad estrarre il secondo elemento della lista
print(animals)# "cane"
print(animal)# "topo"


# aggiunta degli elementi ad una lista

animals.append("bestia demoniaca")
print(animals)# "cane" "bestia demoniaca"

# inserimento di elementi

animals.insert(1, "topo")
print(animals)# "cane" "topo" "bestia demoniaca"


# Tuple
# sono simili ad una lista però una volta definite non si può più
# modificare il loro contenuto

my_Tuple = (10, 5, 8, 3, 9, "ciao", False, "ciao")
type(my_Tuple)
print(my_Tuple)
 
my_Tuple[1]# 5
my_Tuple[:3]# 10, 5, 8

#my_Tuple[0] = 0# restituisce un errore di tipo: TypeError

# ottenere l'indice di un elemento

my_Tuple.index("ciao")

# conta degli elementi

my_Tuple.count("ciao")

len(my_Tuple)# mostra la lunghezza della lista

hello = "ciao python"
len(hello)# mostra il numero di caratteri che contiene
hello[6]
print(hello[:4])# ciao, lo slicing esclude
                # l'elemento alla posizione indicata dopo i due punti




































































































































































































