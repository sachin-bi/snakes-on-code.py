# 🔒 Understanding `Lock` in Python (Threading)

---

### 🧩 What is a Lock?

A **Lock** in Python is like a **key to a room** — it ensures that **only one thread** can access a shared resource at a time.

It helps prevent problems when multiple threads try to use or modify the same data simultaneously.

---

### 💡 Simple Meaning

When multiple threads work on the same data, they can interfere with each other.  
A **Lock** makes sure that only **one thread** can use that data at a time — others must wait until it’s free.

---

### 🚦 Real-Life Example

Imagine there’s **one washroom (shared resource)** and **two people (threads)**.  
A **lock on the door** ensures that only one person uses it at a time 😄  

---

### 🧠 Code Example

```python
import threading
import time

lock = threading.Lock()

def print_numbers(name):
    for i in range(1, 4):
        # Acquire the lock before printing
        lock.acquire()
        try:
            print(f"{name} printing {i}")
            time.sleep(1)
        finally:
            # Release the lock after work is done
            lock.release()

t1 = threading.Thread(target=print_numbers, args=("Thread-1",))
t2 = threading.Thread(target=print_numbers, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")
```

---

# 🧾 What Happens Here?

- Both threads want to print numbers.
- The lock ensures only one thread prints at a time.
- Without the lock, their outputs could get mixed or jumbled together.

### ✅ In Short
- Command	Description
- lock.acquire()	Thread takes the lock (starts using the resource)
- lock.release()	Thread releases the lock (done using it)

# Use Case 
- To avoid race conditions and data corruption

# 🧠 Remember:
    "Locks are essential in multithreading when threads share data — they keep your program’s behavior safe and predictable."

