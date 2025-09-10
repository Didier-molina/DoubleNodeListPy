from Node import DoubleNode

class DoubleList:
    def __init__(self):
        self.head:DoubleNode = None
        self.tail:DoubleNode = None
    
    def add(self,data):
        if self.head is None: # esto se cambia por self.is_empty()
            self.head = DoubleNode(data)
            self.tail = self.head
            return
        self.tail.next = DoubleNode(data)
        self.tail = self.tail.next
        

    def get(self,index): 
        if self.head is None:# esto se cambia por self.is_empty()
            return None
        if index<0 or index>=self.size():
            raise IndexError("Index out of range (index<0 or index>=self.size())")
        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def size(self): 
        if self.head is None: # esto se cambia por self.is_empty()
            return 0
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count+=1
        return count
    
    def exist(self,data):
        pass

    def delete(self,data):
        pass

    def is_empty(self,data):
        pass

    def show(self):
        return f"[{self.head}]"

    def __str__(self):
        return self.show()