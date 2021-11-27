# Espressioni booleane

# ugualianza
5 == 5

# disuguaglianza
"casa" != "gatto"

# maggioranza
6 > 9
6 >= 6# maggiore o uguale

# minoranza
6 < 9
6 <= 9# minore o uguale

# ciclo while

n = int(input("Fino a che numero vuoi contare?"))

i = 0

while i < n:
    if(i % 3 == 0):
        i += 2
        continue
    print(i)
    i += 1

i = 0
while i < n:
    if( i >= 25):
        break# ferma il ciclo più vicino
    print(i)
    i += 1