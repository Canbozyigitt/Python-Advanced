class Kullanici:
    def __init__(self,adi,soyadi,numara):
        print("Kullanıcı sınıfı fonksiyonu")
        self.adi = adi
        self.soyadi = soyadi
        self.numara = numara


    def giris(self):
        print("Giriş Yapıldı")

    def cikis(self):
        print("Çıkış yapıldı")



class Akademisyen(Kullanici):
    def __init__(self,adi,soyadi,numara,dogum_tarihi):
        print("Akademisyen sınıfı fonksiyonu")
        super().__init__(adi,soyadi,numara) #super().__init__(ust_sinif_parametreleri)
        self.dugum_tarihi = dogum_tarihi

akademisyen = Akademisyen("Can","Bozyiğit",1236521,1997)