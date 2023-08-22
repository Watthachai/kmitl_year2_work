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
                
    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.data, end=" ")
        if self.right:
            self.right.inOrder()

    def preOrder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.data, end=" ")

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


print("Inorder traversal:")
root.inOrder()
print()

print("Preorder traversal:")
root.preOrder()
print()

print("Postorder traversal:")
root.postOrder()