class Komputer:
    def __init__(self, model, cena, system):
        self.model = model
        self.cena = cena
        self.system = system

    def zmiencene(self, nowacena):
        self.cena = nowacena
    
    def aktualzacja(self, nowysystem):
        self.system = nowysystem
    
    def wyswietlinfo(self):
        print(f"""
        Laptop
        Model: {self.model}
        Cena: {self.cena}
        System: {self.system}
            """)
        
class Laptop():
    def __init__(self,model , cena , system, bateria) -> None:
        self.model = model
        self.cena = cena
        self.system = system
        self.bateria = bateria

    def wyswietlinfo(self):
        print(f"""
        Laptop
        Model: {self.model}
        Cena: {self.cena}
        System: {self.system}
        Bateria: {self.bateria}
            """)
