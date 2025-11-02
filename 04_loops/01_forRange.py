
for token in range(6):
    print(f"your token num. is: {token}")


# enumerate(list, start=0) -> returns tuple inside list with numbered
orders = ["hitesh", 45, 21.250, "car", "cicd"]
for item in orders:
    print(f"items: {item} {type(item)}")

print(f"Orders size is : {len(orders)}")
print(list(enumerate(orders, start=4)))


# zip(list1, list2) -> returns tuple
names = ["aman" , "rahaul", "sona", "sid"]
amts = [14,5,21,36]

for item in zip(names,amts):
    print(item)

for person,amt in zip(names,amts):
    print(f"{person} paid {amt}")



# while loop
temp = 40
while temp<100:
    temp+=15
    print(f"currnt temp is: {temp}")



# Fallback logic
employees = [("aman",16),("Ram",12),("shyame",15),("nr",16),("we",13),("ry",15)]

for name,age in employees:
    if age>17:
        print(f"Emp can vote: {name}")
        break
else:                #else part only run if the loop didn't break/
    print("No one is eligible for vote...")



# Walrus operator :=
value = 13
if value := value % 5:
    print(f"Value is not divisible..")


flavours = ["masala", "lemon", "ginger"]
print(f"Available flavours are: {flavours}")

while ( ip := input("Enter prefered flavour: ") ) not in flavours:
    print(f"Sry, {ip} flavour not available/ select another flavour.")
print(f"You choose {ip} chai..!")

