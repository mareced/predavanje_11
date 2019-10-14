stevila = [ 5, 2, 8, 3]

#izpis vseh števil
print(stevila)

stevila.sort()
print("Števila smo uredili")
#izpis urejenih števil
print(stevila)

#izpis števila na mestu 1
print("Število na mestu 1 je: ")
print(stevila[1])

#Izpis števila vseh elementov
print("število vseh elementov je " + str(len(stevila)))

stevila.append(7)
stevila.remove(3)
del stevila [0]
print("spremenjen seznam: ")
print(stevila)

print ("vsi elementi prek for zanke")
for stevilo in stevila:
    print("Sedaj je število " + str(stevilo))