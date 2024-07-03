# gönderilen  2 sayı  arasındaki asal sayıları bul.
 
def asalBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1): # +1 yapmamızın sebebi for döngüsü son parametreyi -1 olarak alır.
        if sayi>1:
            for i in range(2,sayi):
               if sayi%i==0:
                break
            else:
                print(sayi)
sayi1=int(input("sayi1: "))
sayi2=int(input("sayi2: "))         
asalBul(sayi1,sayi2)       