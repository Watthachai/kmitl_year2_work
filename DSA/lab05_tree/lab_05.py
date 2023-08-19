class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
                    
            else: 
                self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
            
root = Node(15)

root.insert(15)
root.insert(3)
root.insert(16)
root.insert(9)
root.insert(23)
root.insert(11)
root.insert(7)
root.insert(5)
root.insert(34)
root.insert(19)
root.insert(2)

root.PrintTree()
