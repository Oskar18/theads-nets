import threading

FILE = "counter.txt"

# Inicializácia counter súboru
with open(FILE, "w") as f:
    f.write("0")

def increment():
    for _ in range(100000):
        with open(FILE, "r") as f:
            data = f.read()
            value = 0 if data == "" else int(data)
        value += 1
        with open(FILE, "w") as f:
            f.write(str(value))

threads = [threading.Thread(target=increment) for _ in range(2)]

for t in threads:
    t.start()

for t in threads:
    t.join()

with open(FILE, "r") as f:
    print("Výsledok:", f.read())  # Výsledok bude menší než 200000 kvôli race condition