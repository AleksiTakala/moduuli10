class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry(self, Siirry):
        if Siirry > self.kerros:
            siirrä = Siirry - self.kerros
            for i in range(siirrä):
                if self.kerros == self.ylin:
                    return
                else:
                    self.kerros_ylös()
        elif self.kerros > Siirry:
            siirrä = self.kerros - Siirry
            for i in range(siirrä):
                if self.kerros == self.alin:
                    return
                else:
                    self.kerros_alas()

    def kerros_alas(self):
        self.kerros -= 1
        print(f"kerroksesi on {self.kerros}")
        return
    def kerros_ylös(self):
        self.kerros += 1
        print(f"kerroksesi on {self.kerros}")
        return
class Talo:
    def __init__(self, alinkerros, ylinkerros, hissit):
        self.hissilkm = []
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros

        for i in range(hissit):
            määrä = Hissi(self.alinkerros, self.ylinkerros)
            määrä.num = i + 1
            self.hissilkm.append(määrä)
    def aja_hissiä(self, hissinum, kerros):
        nykyhissi = self.hissilkm[hissinum-1]
        print(f"Olet hississä {nykyhissi.num}")
        nykyhissi.siirry(kerros)


H = Talo(0 , 5 ,3)
H.aja_hissiä(3, 4)