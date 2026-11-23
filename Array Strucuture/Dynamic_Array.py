import ctypes

class Array: 

    def __init__ (self, size):
        self._size = size 
        if size==0:
            self._capacity = 1 
        else:     
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

    def print_Array(self):
        for i in range(0,self._size):
            print(self.Memory[i] , end=" ")
        print('\n')
    def append (self , value):
        if self._size == self._capacity : 
            self.expand_capacity() 
        self.Memory[self._size] = value
        self._size +=1 



    def insertion(self, index, value):

        if not isinstance(index, int):
            raise TypeError("Index must be an integer")

        if self._size == self._capacity:
            self.expand_capacity()

        if index < 0:
            index = self._size + index  

        if index > self._size : 
            index = self._size
        for i in range(self._size-1, index-1, -1):
            self.Memory[i+1]= self.Memory[i]

        self.Memory[index]= value
        self._size +=1

    def right_rotate(self):
        head = self.Memory[self._size-1]
        for i in range(self._size-2,-1,-1):
            self.Memory[i+1]= self.Memory[i]
        self.Memory[0]= head
        
    def left_rotate(self):
        tail = self.Memory[0]
        for i in range(1,self._size):
            self.Memory[i-1]= self.Memory[i]
        self.Memory[self._size-1] = tail 

    def right_rotate_times (self,times) :
           times %= self._size
           for i in range(times):
               self.right_rotate()

    def pop(self , index ):
        if not (index >= - self._size and index <= self._size -1) : 
            raise ('out of range')
        if index < 0 : 
            index = self._size + index 
        pop_item = self.Memory[index]
        for i in range(index+1 , self._size):
            self.Memory[i-1] = self.Memory[i]
        self.Memory[self._size -1]= None 
        self._size -= 1 
        return pop_item

    def index_transposition (self , value):
        location = -1
        for i in range (self._size):
            if self.Memory[i] == value and i != 0  :
                temp = self.Memory[i-1]
                self.Memory[i-1] = self.Memory[i]
                self.Memory [i] = temp 
                location = i-1
        if value == self.Memory[0] :
            return 0 
        return location






array = Array(0)
array.append(10)
array.append(20)
array.append(30)
array.append(40)
array.append(50)
array.print_Array()


print(array.index_transposition(30))

array.print_Array()
print(array.index_transposition(10))
array.print_Array()
print(array.index_transposition(50))
print(array.index_transposition(50))
print(array.index_transposition(60))




# print(array.pop(0))
# array.print_Array()

# print(array.pop(2))
# array.print_Array()

# array.append(60)
# array.append(70)
# array.append(80)
# array.print_Array()

# print(array.pop(-1))

# array.print_Array()
# print(array.pop(-4))

# array.print_Array()
# array.pop(-4)



# array.right_rotate_times(3)
# array.print_Array()

# array.right_rotate_times(7)
# array.print_Array()

# array.right_rotate_times(123456789)
# array.print_Array()


# array.print_Array()
# print("-----------------------")
# array.left_rotate()
# array.print_Array()
# print("-----------------------")
# array.left_rotate()
# array.print_Array()


# array.right_rotate()
# array.print_Array()
# print("-----------------------")
# array.right_rotate()
# array.print_Array()


# array.print_Array()
# print("----------------")
# array.insertion(-1,-10)

# array.print_Array()
# print("--------------------------")
# array.insertion(-2,-20)

# array.print_Array()
# print("--------------------------")


# array.insertion(-3,-30)
# array.print_Array()
# print("--------------------------")

# array.insertion(-4,-40)

# array.print_Array()
# print("--------------------------")

# array.insertion(-5,-50)

# array.print_Array()
# print("--------------------------")

# array.insertion(8,80)

# array.print_Array()
# print("--------------------------")

# array.insertion(20,90)

# array.print_Array()
# print("--------------------------")

