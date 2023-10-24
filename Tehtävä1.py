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



H = Hissi(0, 5)
H.siirry(4)
H.siirry(0)




