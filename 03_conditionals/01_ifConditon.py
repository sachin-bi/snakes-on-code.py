# kettle_boiled = False

# if kettle_boiled:
#     print("Kettle Done! Time to make the chai..")
# else:
#     print("Kettle NOT Done! ..")


# order = input("enter your preferred snack: ").lower()

# if order == "cookies" or order == "samosa":
#     print(f"order Done! Time to make the {order}..")
# else:
#     print("order NOT available! ..")


# order_size = input("Enter chai cup size(S,M,L): ").lower()
# if order_size == "s":
#     print(f"Your amt. is 10")
# elif order_size == "m":
#     print(f"Your amt. is 15")
# elif order_size == "l":
#     print(f"Your amt. is 20")
# else:
#     print(f"unknown cup size...")


# order_amt = int(input("Enter order amt: "))

# del_fee = 30;
# total = order_amt if order_amt<=300 else order_amt+del_fee
# print(f"ur total amt is {total}")


seat_type = input("enter seat type (sl, ac, gen): ").lower()

match seat_type:
    case "sl":
        print("sleeper - available")
    case "ac":
        print("ac - ac available")
    case "gen":
        print("gen - NOT available")
    case _:
        print(f"invalid seat type { (9000*700)}")
