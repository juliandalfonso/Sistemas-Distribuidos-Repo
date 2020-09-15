import threading
import time

# JUAN PABLO PEREZ SANTOS


class MyThread(threading.Thread):
    def __init__(self, num1,num2,operacion):
        super(MyThread, self).__init__()
        self.num1 = num1
        self.num2 = num2
        self.operacion = operacion
        self.result = 0

    def suma(self,x,y):
        return x + y

    def resta(self,x,y):
        return x - y
    
    def mult(self,x,y):
        return x * y

    def div(self,x,y):
        return x / y
        
    def run(self):
        if(self.operacion == 1): self.result = self.suma(self.num1,self.num2)
        elif(self.operacion == 2): self.result = self.resta(self.num1,self.num2)
        elif(self.operacion == 3): self.result = self.mult(self.num1,self.num2)
        else: self.result = self.div(self.num1,self.num2)


if __name__ == "__main__":
    x =  10
    y = 5
    threads = []
    for i in range(1,5):
        t = MyThread(x,y,i)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    total = 0
    for t in threads:
        operacion = t.operacion
        resultado = t.result 
        if(operacion == 1): print("Total de la suma es: {}".format(resultado))
        elif(operacion == 2): print("Total de la resta es: {}".format(resultado))
        elif(operacion == 3): print("Total de la multiplicacion es: {}".format(resultado))
        else: print("Total de la division es: {}".format(resultado))