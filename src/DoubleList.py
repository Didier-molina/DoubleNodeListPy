from Node import DoubleNode

class DoubleList:
    def __init__(self):
        self.head:DoubleNode = None
    
    def add(self,data):
        pass

    def get(self,index):
        pass

    def size(self):
        pass
    
    def exist(self,data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False


    def delete(self,data):
        if data is None:
            raise ValueError("The element to remove cannot be None")
        
        if self.head is None:
            raise RuntimeError("Canot remove from an empty list")
        
        current = self.head
        while current is not None:
            if current.value == data:
                if current.previous is None:
                    self.head = current.next
                    if self.head is not None:
                        self.head.previous = None
                    else:
                        self.tail = None
                elif current.next is None:
                    self.tail = current.previous
                    self.tail.next = None
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                return True
            current = current.next
        return False

    def is_empty(self):
        return self.head is None

    def show(self):
        pass

    def __str__(self):
        pass


