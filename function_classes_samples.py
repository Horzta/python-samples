def say_hello(someone="World"):
    print("Hello " + someone)

say_hello() #Hello World
say_hello("Carl") #Hello Carl

class HelloService:
    def say_hello(self):
        print('Hi I’m Carl')


class Car:
    def __init__(self, make = "Toyota", model = "Vios"):
        self.make = make
        self.model = model

    def info(self):
        print("Make:" + self.make + " Model:" + self.model)


hello_service = HelloService()
hello_service.say_hello() #Hi I’m Carl

car1 = Car() 
car2 = Car("Mitsubishi", "Pajero")
car3 = Car(model="Fortuner")

car1.info() #Make:Toyota Model:Vios
car2.info() #Make:Mitsubishi Model:Pajero
car3.info() #Make:Toyota Model:Fortuner
