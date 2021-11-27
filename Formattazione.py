cat = "Elon"
age = 2
weight = 5.678


print("Il mio gatto si chiama" + cat + "e ha " + str(age) + " anni")

# Formattazione (old school)

print("Il mio gatto si chiama %s ed ha %d anni e pesa %f kg" % (cat, age, weight))

print("Il mio gatto si chiama %s ed ha %d anni e pesa %.2f kg" % (cat, age, weight))

# formattazione (new school)
print("Il mio gatto si chiama {cat}, ha {age} anni e pesa {weight} kg".format(cat = cat, age = age, weight = weight))

# Formattazione Python 3.6 +
print(f"Il mio gatto si chiama {cat}, ha {age} anni e pesa {weight} kg")