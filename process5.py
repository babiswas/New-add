import multiprocessing as mp
import time


def deposit(balance,lock):
   for i in range(100):
      time.sleep(0.01)
      lock.acquire()
      balance.value=balance.value+1
      lock.release()

def withdraw(balance,lock):
   for i in range(100):
     time.sleep(0.01)
     lock.acquire()
     balance.value=balance.value-1
     lock.release()

if __name__=="__main__":
   balance=mp.Value('i',200)
   lock=mp.Lock()
   d=mp.Process(target=deposit,args=(balance,lock))
   w=mp.Process(target=withdraw,args=(balance,lock))
   d.start()
   w.start()
   d.join()
   w.join()
   print(balance.value)


       