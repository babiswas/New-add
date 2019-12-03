import multiprocessing as mp

def calc_square(numbers,result,v):
    v.value=12.0
    for idx,n in enumerate(numbers):
       result[idx]=n*n

if __name__=="__main__":
   numbers=[1,2,3]
   result=mp.Array('i',3)
   val=mp.Value('d',0.0)
   p=mp.Process(target=calc_square,args=(numbers,result,val))
   p.start()
   p.join()
   print(result[:])
   print(val.value)


    
