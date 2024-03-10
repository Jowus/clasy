class Pracownik:
    def __init__(self, aimie, anazwisko, astawka) -> None:
        self.imie = aimie
        self.nazwisko = anazwisko
        self.stawka = astawka

    def zmien_wyplate(self, nowa_wyplata):
        self.stawka = nowa_wyplata
        self.wyplataroczna = self.stawka*12

    def info(self):
        print("---"*10)
        print(f"Imie i Nazwisko: {self.imie} {self.nazwisko}")
        print(f"Wyplata miesieczna: {self.stawka}")
        print(f"Wypłataroczna: {self.stawka*12}")
        print("---"*10)

class Kasjer:
    def __init__(self, aimie, anazwisko, astawka, akasa) -> None:
        self.imie = aimie
        self.nazwisko = anazwisko
        self.stawka = astawka
        self.kasa = akasa
    def info(self):
        print("---"*10)
        print(f"Imie i Nazwisko: {self.imie} {self.nazwisko}")
        print(f"Wyplata miesieczna: {self.stawka}")
        print("---"*10)
    def zmien_kase(self, nowakasa):
        self.kasa = nowakasa

class Menager:
    def __init__(self, abiuro,aimie, anazwisko, astawka) -> None:
        self.biuro = abiuro
        self.imie = aimie
        self.nazwisko = anazwisko
        self.stawka = astawka
    def info(self):
        print("---"*10)
        print(f"Imie i Nazwisko: {self.imie} {self.nazwisko}")
        print(f"Wyplata miesieczna: {self.stawka}")
        print("---"*10)
    def zmien_biuro(self, nowebiuro):
        self.biuro = nowebiuro

class Asystent:
    def __init__(self, adzial,aimie, anazwisko, astawka) -> None:
        self.dzial = adzial
        self.imie = aimie
        self.nazwisko = anazwisko
        self.stawka = astawka
    def zmien_dzial(self, nowydzial):
        self.dzial = nowydzial
    def info(self):
        print("---"*10)
        print(f"Imie i Nazwisko: {self.imie} {self.nazwisko}")
        print(f"Wyplata miesieczna: {self.stawka}")
        print("---"*10)