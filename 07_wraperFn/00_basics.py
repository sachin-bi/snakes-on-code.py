from functools import wraps

def myshop(func):
    @wraps(func)
    def rapper(*args, **kwargs):
        print(f" welcome to our ship.")
        func(*args, **kwargs)
        print(f" Goodbye! ship.")
    return rapper


@myshop
def man(name, item="IRON Toy"):
    print(f"i'm {name} want {item}.")


man("hitesh", "Car Toy")
man("girlJoti", "barbi")
