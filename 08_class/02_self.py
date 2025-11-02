
class Car:
    price = "high"

    def describe(self):
        return f"the price is {self.price}"
    

wagonr = Car()
wagonr.price = "low"
print(wagonr.describe())
print(Car.describe(wagonr))