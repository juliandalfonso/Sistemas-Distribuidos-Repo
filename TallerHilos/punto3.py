import threading
import time
import math

# JUAN PABLO PEREZ SANTOS


class MyThread(threading.Thread):
    def __init__(self, inicio,fin):
        super(MyThread, self).__init__()
        self.inicio = inicio
        self.fin = fin
        self.result = 0

    def cal_factorial(self):
        suma_fac = 0
        for i in range(self.inicio,self.fin):
            factorial = 1
            numero = i
            for j in range(i):
                factorial *= numero
                numero -= 1
            suma_fac += factorial
        self.result = suma_fac
              
        
    def run(self):
        self.cal_factorial()


if __name__ == "__main__":
    n = int(input("Introduzca n: "))
    num = int(input("Numero de hilos: "))
    if(n % num == 0):
        num_div = int(n / num)
        inicio = 1
        fin = num_div + 1
        threads = []
        for i in range(num):
            t = MyThread(inicio,fin)
            t.start()
            threads.append(t)
            inicio += num_div
            fin += num_div
        for t in threads:
            t.join()
        total = 0
        for t in threads:
            total += t.result
        print("La suma de los factoriales es {} ".format(total))
    else: print("ERROR")