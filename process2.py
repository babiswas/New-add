import time
import multiprocessing as mp

square=[]

def calc_square(numbers):
    global square
    for n in numbers:
      time.sleep(5)
      print('square'+str(n*n))
      square.append(n*n)


if __name__=="__main__":
   arr=[1,2,3,4,5,6]
   p1=mp.Process(target=calc_square,args=(arr,))
   p1.start()
   p1.join()
   while True:
     print("hello")
   print("result"+str(square))
   print("Done")
