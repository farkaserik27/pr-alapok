class Negyzet:
    def __init__(self, oldal_hossz):
        self.oldal_hossz = oldal_hossz
    
    def kerulet(self):
        return 4 * self.oldal_hossz
    
    def terulet(self):
        return self.oldal_hossz ** 2

if __name__ == "_main_":
    negyzet = Negyzet(5)
    print("A négyzet kerülete:",negyzet.kerulet())
    print("A négyzet területe:",negyzet.terulet())