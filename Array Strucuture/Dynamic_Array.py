import ctypes

class Array: 

    def __init__ (self, size):
        self._size = size 
        self._capacity = size * 2  
        array_datatype = ctypes.py_object*self._capacity
        self.Memory = array_datatype()
        for i in range(self._capacity):
            self.Memory[i] = None
    def expand_capacity(self):

        self._capacity = self._capacity*2 
        array_datatype = ctypes.py_object * self._capacity
        new_memory = array_datatype()
        for i in range(self._capacity):
            new_memory[i] = None
            
        for i in range(self._size):
            new_memory[i] = self.Memory[i]

        del self.Memory
        self.Memory = new_memory 

    def __getitem__(self, key):
        return self.Memory[key]

    def __setitem__(self, key, value):
        self.Memory[key] = value

    def __len__(self):
        return self._size

    def append (self , value):
        if self._size == self._capacity : 
            self.expand_capacity() 
        self.Memory[self._size] = value
        self._size+=1  


    def inseration(self, index, value):
        if self._size == self._capacity:
            self.expand_capacity()
        for i in range(self._size-1, index-1, -1):
                if i != index : 
                    self.Memory[i+1]= self.Memory[i]
        self.Memory[index]= value
        self._size +=1


        

arr = Array(3)

arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)

print(len(arr))
print(arr[3])