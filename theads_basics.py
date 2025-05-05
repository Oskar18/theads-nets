import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(1)  # Simulace časově náročné operace
        print(f"Vlákno {threading.current_thread().name}: {i}")

# Vytvoření dvou vláken
thread1 = threading.Thread(target=print_numbers, name="Vlákno 1")
thread2 = threading.Thread(target=print_numbers, name="Vlákno 2")

# Spuštění vláken
thread1.start()
thread2.start()

# Čekání na dokončení obou vláken
thread1.join()
thread2.join()

print("Hlavní vlákno skončilo.")