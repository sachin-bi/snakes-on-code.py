import threading
import time

print("the global interpreter lock (GIL) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. \n")

def brewL_chai():
    print(f"{threading.current_thread().name} started..")
    count = 0
    for _ in range(110_000_000):
        count += 1
    print(f"{threading.current_thread().name} ended..")

thread1 = threading.Thread(target=brewL_chai, name="Barista-1")
thread2 = threading.Thread(target=brewL_chai, name="Barista-2")

start = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()

print(f"The process took {end - start:.2f} sec time..")