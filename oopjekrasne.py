'''
#bojovnik1
zivoty1 = 100
utok1 = 12
obrana1 = 5

#bojovnik2
zivoty2 = 100
utok2 = 10
obrana2 = 5

while zivoty1 > 0 and zivoty2 > 0:
    zivoty1 -= (utok2 - obrana1)
    zivoty2 -= (utok1 - obrana2)
    print("bojovnik1 ma ", zivoty1, " zivotu")
    print("bojovnik2 ma ", zivoty2, " zivotu")
if zivoty2 < zivoty1:
    print("bojovnik1 vyhral")
else:
    print("bojovnik2 vyhral")
'''
class Bojovnik:
    def __init__(self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence

    def podej_hlaseni(self):
        print(f"{self.name} má {self.health} životů")
              
    def bran_se(self, utok):
        self.health -= (utok - self.defence)

    def utoc(self, souper)


bojovnik1 = Bojovnik("Vilma", 100, 10, 5)
bojovnik2 = Bojovnik("Jachym", 100, 12, 5)
