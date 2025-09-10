class DoubleNode:
    def __init__(self, value, previous_node=None, next_node=None):
        self.value = value
        self.next:DoubleNode = next_node
        self.previous:DoubleNode = previous_node
    
    def __repr__(self):
        return f"{self.value}, {self.next}" if self.next is not None else f"{self.value}"
