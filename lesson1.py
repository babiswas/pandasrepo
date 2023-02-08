from __future__ import annotations

class A:
    
    ''' Checking type hint for a member function returning object of its class type'''
    
    def __init__(self)->None:
        self.a=2
        
    def myfunc(self)->A:
        
        '''Checking if the function works if the return type is object of the same class'''
        
        return A()

if __name__=="__main__":
    a=A()
    b=a.myfunc()
    print(b.__dict__)