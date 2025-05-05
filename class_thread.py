import threading
import time


class MyThread(threading.Thread):
    def run(self):
        print("Bežím v inom vlákne!")
        time.sleep(1)
        print("po pospinkani si")

t = MyThread()
t.start()
print("ahoj")
t.join()
print("joinol som sa")