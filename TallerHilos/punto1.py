import threading
import time

# JUAN PABLO PEREZ SANTOS

class MyThread(threading.Thread):
    def __init__(self, i):
        super(MyThread, self).__init__()
        self.i = i
        self.i_next = i + 1
        self.result = 0

    def run(self):
        for i in range(self.i,self.i_next + 1): self.result += 2 ** i


if __name__ == "__main__":
    i = 1
    threads = []
    while(i <= 10):
        t = MyThread(i)
        t.start()
        threads.append(t)
        i += 2
    for t in threads:
        t.join()
    total = 0
    for t in threads:
        total += t.result
    print("Total de la suma es: {}".format(total))
