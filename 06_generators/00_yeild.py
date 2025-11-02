
# eg of generator
def generator():
    yield 1
    yield 2


g = generator()
print(next(g))
print(next(g))


# infinite generator
def whatChai():
    print(f" what chai would u like to have??")
    order = yield
    while True:
        print(f"Your order is {order}")
        order = yield
    
result = whatChai()
next(result)  # gen started

result.send("veg")
result.send("chicken")

