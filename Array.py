
import ctypes

class MeraList:

    def __init__(self):
        self.size=1
        self.n=0
        #creat a ctype array with size  = self.size
        self.A = self.__make_array(self.size)

    # def __len__(self):
    #     return self.n 
    

    def __str__(self):
         #[1,2,3,4]
         result = ''
         for i in range (self.n):
             result = result + str(self.A[i]) + ','
         return '['  + result[:-1] + ']'   
    
    def __getitem__(self,index):
        if 0 <= index < self.n:
           return self.A[index]
        else:
            return  'IndexError -  Index out of range' 
      
    def append(self,item):
        if self.n == self.size:
            #resize
            self.__resize(self.size*2) 


        #append
        self.A[self.n]= item
        self.n = self.n + 1  
        


    def __resize(self,new_capacity):
        #create a mew array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity 
        #copy the content of A and B 
        for i in range(self.n):
            B[i] = self.A[i]
        #reassign    
        self.A = B


    def __make_array(self,capacity):
        #create a c type array(static,referential) with size capacity
        return(capacity*ctypes.py_object)()    
L= MeraList() 
L.append('hello')
L.append(34)
L.append(True)
L.append(1000)
L.append(45)
L[1]
# print(L)