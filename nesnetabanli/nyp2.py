# dairenin alanı ve çevresi 
class Circle:
    pi=3.14

    def __init__(self,yaricap):
        self.yaricap=yaricap

    def alanHesapla(self):
        return self.pi*(self.yaricap*self.yaricap)
    def cevreHesapla(self):
        return 2*self.pi + self.yaricap
c1=Circle(5)
print(f'dairenin alanı : {c1.alanHesapla()}\n dairenin çevresi: {c1.cevreHesapla()}')
