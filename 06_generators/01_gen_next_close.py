# def team():
#     yield "Alice"
#     yield "Bob"
#     yield "Charlie"


# t = team()
# print(next(t))
# print(next(t))

# for n in t:
#     print(n)


def fullname():
    print(f"Hi, wlc to full name")
    order = yield
    while True:
        print(f"ok your order is: {order}")
        order = yield


s = fullname()
next(s)

try:
    s.send("Jamun")
    s.send("mango")
    s.send("Jamun-shake")
except:
    print(f"somthing is wrong")
finally:
    s.close()
