Apple_price = 45.56
name = "Aman"
print("Hi .. \n..Python! apple price is ", Apple_price)
print("Hello!", "enjoy python",sep=":()")

# name = input("what is ur name?")
# print("Name is ",name)


# age = input("ur age? ")
# print("age = ", age-10)
# print("age = ", int(age)-10)

print(type(Apple_price))
print(type(name))


# Lists []
countries = ["uk", "us","ind","pak","sri"]
print("countries len = ",len(countries))
print("- 1 ", countries[2])
# countries.sort()
print(countries[2:4])
print(countries[:-1])
print(countries[-1:])
print(countries[-1])
print("\n")
# List is mutable data type


# Tuple ()
# Tuple is unmutable data type
# Tuple elements can be of diff types
tuple1 = (1,"dj",[4,6],("raj"))
print(tuple1)


# Dictionary {key : value}
username = {
    "ram" : "32gb",
    "ssd" : "1024gb",
    "ram2" : "32gb",
}
print(username.keys())
print(username.values())