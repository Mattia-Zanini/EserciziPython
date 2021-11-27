n = int(input("Fino a che numero vuoi stampare?"))

for i in range(0,n):
    print(i)

n = int(input("Quanti numeri di Fibonacci vuoi stampare"))

fib_num = 0
next_fib_num = 1

for i in range(n):
    fib_num,next_fib_num = next_fib_num,next_fib_num+fib_num
    print("%d° numero di Fibonacci = %d" % (i + 1, fib_num))


a = "gatto"
b = "cane"
print(f"Valori iniziali, valore di a: {a}, valore di b: {b}")

# Swapping delle variabili (old school)
tmp = a
a = b
b = tmp
print(f"vecchia scuola, valore di a: {a}, valore di b: {b}")

# Swapping delle variabili (new school)
# a prende il valore di b = b prende il valore di a12

a,b = b,a
print(f"nuova scuola, valore di a: {a}, valore di b: {b}")

# Iterazione sulle liste

shopping_List = ["tofu", "latte di soia", "riso basmati", "yougurt greco"]
     
print("Vecchia scuola")            
for i in range(len(shopping_List)):
    print(f"{i + 1} {shopping_List[i]}")

print("Nuova scuola")
for entry in shopping_List:
    print(f"- {entry}")
    
print("Alternativa")
for i, entry in enumerate(shopping_List):
    print(f"{i + 1} {entry}")