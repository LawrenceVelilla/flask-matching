class BondedStack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if self.isEmpty():
            raise Exception('Cannot pop: List is empty')
        
        return self.items.pop()
    
    def peek(self):
        if self.isEmpty():
            raise Exception('List is empty')
        
        return self.items[self.size()-1]

    def peek_index(self,index):
        if self.isEmpty():
            raise Exception('List is Empty')
        
        return self.items[index]
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)

    def clear(self):
        self.items = []

    def __str__(self):
        strRepresentation = ''
        for items in self.items:
            strRepresentation += items + ' '
        return strRepresentation
    