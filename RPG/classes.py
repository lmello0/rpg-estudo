class Classes:
    def __init__(self, vNOME, vHP, vSP):
        self.nome = vNOME
        self.hp = vHP
        self.sp = vSP
    
    def getInfos(self):
        print('----- ATRIBUTOS -----')
        print('- NOME: {}'.format(self.nome))
        print('- HP: {}'.format(self.hp))
        print('- SP: {}'.format(self.sp))

    def getNome(self):
        return self.nome

    def setHP(self, vHP):
        self.hp = vHP
    
    def setNome(self, vNOME):
        self.nome = vNOME
    
    def setSP(self, vSP):
        self.sp = vSP
    
class Mago(Classes):
    def __init__(self, vNOME, vHP, vSP):
        super().__init__(vNOME, vHP, vSP)
        self.mp = vSP * 0.5

    def getInfos(self):
        super().getInfos()
        print('- AP: {}'.format(self.mp))
        print('---------------------')

    def getMP(self):
        return self.mp

class Cavaleiro(Classes):
    def __init__(self, vNOME, vHP, vSP):
        super().__init__(vNOME, vHP, vSP)
        self.ad = vSP * 0.75

    def getInfos(self):
        super().getInfos()
        print('- AD: {}'.format(self.ad))
        print('---------------------')

    def getAD(self):
        return self.ad

class Arqueiro(Classes):
    def __init__(self, vNOME, vHP, vSP):
        super().__init__(vNOME, vHP, vSP)
        self.rp = vSP * 0.6

    def getInfos(self):
        super().getInfos()
        print('- RP: {}'.format(self.rp))
        print('---------------------')

    def getRP(self):
        return self.rp