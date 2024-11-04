# Tražimo unos koliko brojeva ćemo provjeriti
n = int(input("koliko brojeva želite unijeti za provjeru parnosti?"))

# Varijable za brojanje parnih i neparnih brojeva
parni_brojevi = 0
neparni_brojevi = 0

# Petlja za unos i provjeru svakog broja
for i in range(n):
    broj = int(input(f"unesite broj {i+1}:"))

    # Provjera parnosti broja
    if broj % 2 == 0:
        print(f"Broj {broj} je paran.")
        parni_brojevi += 1
    else:
        print(f"Broj {broj} je neparan.")
        neparni_brojevi += 1

# Ispis konačnog broja parnih i neparnih brojeva
print("/nUkupno parnih brojeva:", parni_brojevi)
print("Ukupno neparnih brojeva:", neparni_brojevi)
