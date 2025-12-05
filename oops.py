"""class Aditya:
    a=111 #attribute
    def hello(self):
        print("Hello, Aditya here!") #method  

    print("This is Aditya's class")  
print(Aditya().a)   
Aditya().hello()

obj=Aditya() #object creation
print(obj.a)  #accessing attribute using object
obj.hello()   #accessing method using object    """

"""class Factory:
    def __init__(self,materail,zips,pockets):
        self.materail = materail
        self.zips = zips
        self.pockets = pockets           #constructor method
    def show(self):
        print(f"Object details are {self.materail}, {self.zips}, {self.pockets}")  #method


Adidas = Factory("leather","5","3")  #object creation with arguments
Nike = Factory("Nylon","7","5")
print(Adidas.materail)
Nike.show()  #method calling using object"""

class Animal:
    name = "Lion"  #class attribute

    def __init__(self,age):
        self.age = age  #instance attribute

    def display(self):
        print("How are you") #Instance method
    

    @classmethod
    def class_method(cls):  #cls points to class
        print("This is a class method")  #class method

    @staticmethod  
    def static():
        print("how are you bro")  #static method