import random
import json
skrito_stevilo = random.randint (1,10)
stevec = 0

with open ("tocke.txt") as datoteka:
    tocke = json.loads(datoteka.read())

print("tocke do sedaj: ")

for tocka in tocke:
    print(" " + str(tocka))

while True:
    stevilo = int(input("vpisi stevilo: "))
    stevec = stevec +1

    if stevilo == skrito_stevilo:
        print("čestitke")
        break
    elif stevilo > skrito_stevilo:
        print("stevilo je manjše")
    else:
        print("stevilo je večje")

print("stevilo poskusov je bilo: " + str(stevec))

tocke.append(stevec)

with open("tocke.txt", "w") as datoteka:
    datoteka.write(json.dumps(tocke))