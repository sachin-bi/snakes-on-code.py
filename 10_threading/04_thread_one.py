import threading
import time

def boil_milk():
    print(f"boinling milk..")
    time.sleep(2)
    print(f"-- ends boinling milk..")

def toast_bun():
    print(f"Toasting bun..")
    time.sleep(3)
    print(f"-- Done toasting bun..")

# this main thread by default
# boil_milk()
# toast_bun()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)


start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(f"breakfast is ready in {end - start:.2f} sec time..")