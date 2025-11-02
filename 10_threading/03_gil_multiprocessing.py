from multiprocessing import Process
import time


def crunch_number():
    print(f"Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"---Ended the count process...")


p1 = Process(target=crunch_number, name="Barista-1")
p2 = Process(target=crunch_number, name="Barista-2")

if __name__ == "__main__":
    print(
        "\n the global interpreter lock (GIL) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. \n"
    )

    start = time.time()

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"The process took {end - start:.2f} sec time..")
