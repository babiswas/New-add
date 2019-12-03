from multiprocessing import Pool

def f(n):
  sum=0
  for x in range(100):
     sum+=x*x
  return n*n

if __name__=="__main__":
  array=[1,2,3,4,5]
  p=Pool()
  result=p.map(f,range(1000))
  print(result)
