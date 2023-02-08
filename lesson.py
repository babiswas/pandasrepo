import asyncio

async def task1():
   print("Executing task1:")
   await asyncio.sleep(2)
   print("Completed task")
   return "Task1 complete"

async def task2():
   print("Executing task2:")
   await asyncio.sleep(2)
   print("Completed task")
   return "Task2 complete"

async def collect():
   t1=asyncio.create_task(task1())
   t2=asyncio.create_task(task2())
   l=await asyncio.gather(t1,t2)
   print(l)

if __name__=="__main__":
   print("=====================")
   l=asyncio.run(collect())
   print("======================")
    

