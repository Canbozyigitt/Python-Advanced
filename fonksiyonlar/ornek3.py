# Bankmatik uygulaması 

CanHesap={
    'ad': 'Can Bozyiğit',
    'hesapNo': '12345678',
    'bakiye': 3000,
    'ekhesap': 2000
}
İremHesap={
    'ad': 'İrem Topal',
    'hesapNo': '13245678',
    'bakiye': 2000,
    'ekhesap': 1000
}


def paraCek(hesap,miktar):
    print(f'Merhaba {hesap['ad']} ')
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        
        print("paranızı alabilirsiniz")
    else:
        toplam=hesap['bakiye'] + hesap['ekhesap']
        if toplam>miktar:

            ekhesapKullanimi=input("ek hesap kullanılsın mı e/h : ")
            if ekhesapKullanimi == 'e':
                kalanPara=toplam-miktar
                print(f'kalan paranız: {kalanPara}')

        else:
            print("bakiye yetersiz")   
           


paraCek(CanHesap,4000)    
