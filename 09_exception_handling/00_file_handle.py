# file = open("order.txt", "w")
# try:
#     file.write("1. writing it with py code...")
# except Exception as e:
#     print(f"somthing wrong!")
# finally:
#     file.close()
#     print(f"write done!")


with open("order2.txt","w") as file:
    file.write("mordern way to write the file is this..")