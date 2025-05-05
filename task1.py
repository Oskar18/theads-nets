"""
Vytvor program, ktorý spustí 5 vláken. Každé vlákno vypíše svoje číslo 10-krát s krátkou pauzou (napr. time.sleep(0.1)).
"""

import threading
import time


def foo(index):
    for i in range(10):
        print(f"ja som vlakno cislo {i} a toto je moj {i}ty výpis")
        time.sleep(0.1)


for i in range(5):
    t = threading.Thread(target=foo, args=(i,))
    t.start()


print("hlavne vlakno skoncilo")