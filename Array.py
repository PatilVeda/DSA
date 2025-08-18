
import ctypes

class MeraList:

    def __init__(self):
        self.size=1
        self.n=0
        #creat a ctype array with size  = self.size
        self.A = self.__make_array(self.size)

    def __make_array(self,capacity):
        #create a c type array(static,referential) with size capacity
        return(capacity*ctypes.py_object)()    
L= MeraList() 
print(L)