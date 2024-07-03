# constructor(yapıcı method)
class Person :  # class isimleri her zaman büyük harfle başlar. 


 def __init__(self,name,year): # init metodu oluşturulan her p1 objesi için çalıştırılır.
    self.name=name
    self.year=year

 # instance methods
 def intro(self):
   print("Hello there. I am " + self.name)   

p1=Person('can',1907)    
p1.intro()
