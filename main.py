from laptop import Komputer
from laptop import Laptop
from pracownik import Kasjer
from pracownik import Menager
from pracownik import Asystent
from pracownik import Pracownik

produkty = []
pracownicy = []

print("Witamy w sklepie")
pk1= Pracownik("Grazyna", "Jezyna", 5000)
p1 = Kasjer(pk1,pk1,pk1,1)
pk2 = Pracownik("Marcin", "Parowa", 5000)
p2 = Kasjer(pk2,pk2,pk2,2)
pk3 = Pracownik("Mariusz", "Kozlowski", 10000)
p3 = Menager(pk3,pk3,pk3,5)
pk4 = Pracownik("Adrian", "Kozlowski", 6500)
p4 = Asystent(pk4,pk4,pk4,5)
k1 = Komputer("Lenovo", 3000, "Windows 11")
k2 = Komputer("HP", 2000, "Windows 10")
l2 = Laptop(k2,k2,k2,"15000 mAh")
k3 = Komputer("Apple", 7000, "MacOS Pro Max")
l3 = Laptop(k3,k3,k3, "100 mAh")

dziala = True

print("Wyswietl pracownikow - p")
print("Wyswietl produkty - k")
inp = input()
if inp == "p":
    p1.info()
    p2.info()
    p3.info()
    p4.info()
if inp == "k":
    k1.wyswietlinfo()
    l2.wyswietlinfo()
    l3.wyswietlinfo()
