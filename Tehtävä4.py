import random
class Auto:
    def __init__(self, rkt, hn):
        self.rkt = rkt
        self.hn = int(hn)
        self.nopeus = 0
        self.kuljettu = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.hn:
            self.nopeus = self.hn
        elif self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, tunti):
        self.kuljettu += self.nopeus * tunti

    def __str__(self):
        return f'{self.rkt}, {self.hn}, {self.nopeus}, {self.kuljettu}'


class kilpailu:
    def __init__(self, kilpailunnimi, pituuskm):
        self.autot = []
        self.kilpailunimi = kilpailunnimi
        self.pituuskm = pituuskm



autolista = []
for i in range(10):
    auto = Auto(f'ABC-{i+1}', random.randint(100, 200))
    autolista.append(auto)
kilpailu = True
while kilpailu:
    for i in autolista:
        i.kiihdytä(random.randint(-10, 15))
        i.kulje(1)
        if i.kuljettu > 10000:
            kilpailu = False

for i in autolista:
    print(f'{i}\n')