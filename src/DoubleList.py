from Node import DoubleNode

class DoubleList:
    def __init__(self):
        self.head:DoubleNode = None
        self.tail:DoubleNode = None
    
    def add(self,data):
        if self.is_empty():
            self.head = DoubleNode(data)
            self.tail = self.head
            return
        newNode = DoubleNode(data)
        self.tail.next = newNode
        newNode.previous = self.tail
        self.tail = newNode

    def get(self,index): 
        if self.is_empty():
            return None
        if index<0 or index>=self.size():
            raise IndexError("Index out of range (index<0 or index>=self.size())")
        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def size(self): 
        if self.is_empty():
            return 0
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count+=1
        return count
    
    def exist(self,data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self,data):
        if self.is_empty():
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
        return f"[{self.head}]"

    def __str__(self):
        return self.show()