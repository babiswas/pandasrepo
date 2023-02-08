from __future__ import annotations
import asyncio

class A:
   def __init__(self,start:int,end:int)->None:
       self.start=start
       self.end=end

   def __aiter__(self)->A:
      return self

   async def __anext__(self)->int:
      if self.start<self.end:
         self.start+=1
         return self.start
      else:
         raise StopIteration

async def myiterator():
      async for obj in A(0,12):
          print(obj)

if __name__=="__main__":
   print("===========START============")
   try:
       asyncio.run(myiterator())
   except StopIteration as e:
     print(f"Excception occured")
   print("============COMPLETE===========")