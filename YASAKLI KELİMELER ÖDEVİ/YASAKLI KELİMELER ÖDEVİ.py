yasakli_liste = ["Mehmet", "Murat", "Hacı", "Hasan"]

metin: str = input("Lütfen Metin giriniz: ")

for i in yasakli_liste:
    if i in metin:
        metin = metin.replace(i, len(i)*"*")
print(metin)
