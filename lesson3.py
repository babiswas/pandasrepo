from __future__ import annotations
class A:
   def __init__(self,start:int,end:int)->None:
      self.start=start
      self.end=end

   def __iter__(self)->A:
       return self

   def __next__(self)->int:
       if self.start>self.end:
          raise StopIteration
       self.start+=1
       return self.start

if __name__=="__main__":
   print("===================")
   print("Iterating through the iterator:")
   obj=A(0,12)
   obj=iter(obj)
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print("====================")
   