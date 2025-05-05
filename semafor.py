import threading
import time

sema = threading.Semaphore(2)  			# max 2 vlákna môžu vstúpiť naraz

def task(name):
    print(f"{name} čaká na vstup")
    with sema:
        print(f"{name} beží")
        time.sleep(2)
        print(f"{name} končí")

threads = [threading.Thread(target=task, args=(f"Thread-{i}",)) for i in range(4)]

for t in threads:
    t.start()
for t in threads:
    t.join()