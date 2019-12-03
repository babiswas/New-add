import multiprocessing as mp

def calc_square(numbers,q):
    for n in numbers:
       q.put(n*n)

if __name__=="__main__":
   numbers=[1,2,3,4,5]
   q=mp.Queue()
   p=mp.Process(target=calc_square,args=(numbers,q))
   p.start()
   p.join()
   while q.empty() is False:
       print(q.get())

