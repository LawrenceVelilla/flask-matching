class BondedQueue:
    def __init__(self, capacity):
        assert type(capacity) == int, ('Error: Type error')
        assert capacity >= 0, ('Error: Illegal Capacity')

        self.__items = []
        self.__capacity = capacity


    def size(self):
        return len(self.__items)

    def isFull(self):
        return self.size() == self.__capacity
    
    def isEmpty(self):
        return self.size() == 0
    
    def capacity(self):
        return self.__capacity
    
    def clear(self):
        self.__items = []

    def enqueue(self,item):
        if self.isFull():
            raise Exception('Error: List is Full')
       
        self.__items.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Error: List is Empty')
        
        return self.__items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            raise Exception('Error: List is Empty')
        
        return self.__items[self.size()-1]
    
    def __str__(self) -> str:
        str_repr = ''
        for item in self.__items:
            str_repr += (str(item) + ' ')
        return str_repr
    
    def __repr__(self) -> str:
        return str(self) + " Max=" + str(self.__capacity)
    