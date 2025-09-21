# Pitati korisnika da unese ime proizvoda
# Kada unese ime proizvoda dodati proizvod u "kasu"
# -> Korisnik mora uneti 3 proizvoda ukupno

kasa = list()

while len(kasa) < 3:
    item = input("Unesite ime proizvoda: ")
    kasa.append(item)
print(kasa)