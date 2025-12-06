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

"""class Animal:
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
        print("how are you bro")  #static method"""

'''class Factory: #parent class
    a="I am an attribute inside Factory class"
    def hello(self):
        print("Hi I am a method inside Factory class")

class FactoryPune(Factory):  #inheritance  chlid class 
    pass

obj = Factory()
obj2 = FactoryPune()
print(obj2.a)'''


'''class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Animal Name: {self.name}")

class Human(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    def show(self):
        print(f"Your Name, Age: {self.name}, {self.age}")


animal1 = Animal("wagh")
        
person1 = Human("Aditya", 30)

animal1.show()  # Output: Animal Name: wagh
person1.show()  # Output: Your Name, Age: Aditya, 30'''

'''class Animal:
    def __init__(self,name):
        pass

class Human:
    def __init__(self,name,age):
        pass

class Robot(Animal, Human):  #multiple inheritance
    name3 = "Chitti"  #class attribute

obj = Robot(Gekko)'''



class Factory:
    def __init__(self,materail,zips):
        self.materail = materail
        self.zips = zips

class BhopalFactory(Factory):
    def __init__(self,materail,zips,color):
        super().__init__(materail,zips) 
        self.color = color

class PuneFactory(BhopalFactory):
    def __init__(self,materail,zips,color,pockets):
        super().__init__(materail,zips,color)
        self.pockets = pockets  
        