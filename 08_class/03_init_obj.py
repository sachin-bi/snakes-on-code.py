class Dog:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summery(self):
        return f"the type is: {self.type} and size is: {self.size}"


german = Dog("german", "big")
print(german.summery())

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        return f"This is a {self.year} {self.make} {self.model}."
    
tata = Car("tata","nano",2000)
# print(tata.d)