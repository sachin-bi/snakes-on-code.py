suger_amt= 2
print(f"Initial sugar: {suger_amt}")
print(f"ID of 12:{id(suger_amt)}")

suger_amt= 32
print(f"second Initial sugar: {suger_amt}")

print(f"ID of 2:{id(2)}")
print(f"ID of 12:{id(suger_amt)}")


def modify(x):
    x.append(100)
    print("Inside:", x)

nums = [1, 2, 3]
modify(nums)
print("Outside:", nums)


def modify2(x):
    x = x + 100
    print("Inside:", x)

num = 5
modify2(num)
print("Outside:", num)
