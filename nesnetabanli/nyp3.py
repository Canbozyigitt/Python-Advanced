# Inheritance 

class Animal:
    def __init__(self,türler):
        self.türler=türler

    def ses(self):
        print("some  generic sound")

class Dog(Animal):  # miras alma işlemi

    def __init(self,name,breed):
        super().__init__("Dog") # init metotundaki tür parametresinden miras aldık 
        self.name=name
        self.breed=breed

    def ses(self):
        print("bark!")    



        