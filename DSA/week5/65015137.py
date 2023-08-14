""" ACTIVITY 1
ให้นักศึกษาเขียนโปรแกรมสร้าง Stack แล้ว Push เก็บข้อมูล ABCDEF 
Pop ออกจน empty
"""
class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:   
            self.items = list
        self.size = len(self.items)
        
    def push(self, i):
        self.items.append(i)
        self.size += 1
        
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        
        return self.items == []
    
s = Stack()

s.push('A')
s.push('B')
s.push('C')
s.push('D')
s.push('E')
s.push('F')

print("\nActivities 1 \n",s.items)

for i in range(len(s.items)):
    print('Remove:', s.pop(), 'success!.', 'empty yet?', s.isEmpty())
    
    


""" ACTIVITY 2 
ให้นักศึกษาเขียนโปรแกรมสร้าง Queue แล้ว เก็บข้อมูล ABCDEF 
หลังจากนั้นให้แสดงผล ขนาดของข้อมูลท่ีเก็บใน Queue 
"""

class Queue:
    def __init__(self, items = []):
        self.items = items
        self.size = len(self.items)
    
    def enQueue(self, i):
        self.items.append(i)
        self.size += 1
    
    def deQueue(self):
        self.size -= 1
        return self.items.pop(0)
        
    def isEmpty(self):
        return self.items == []
    

q = Queue()
q.enQueue('A')
q.enQueue('B')
q.enQueue('C')
q.enQueue('D')
q.enQueue('E')
q.enQueue('F')

print('\n\n#Activities 2 \nAdded!', q.items, '\nTotal size :',len(q.items))


"""
!TODO ACTIVITY 3
ให้นักศึกษาเขียนโปรแกรมสร้าง Link List แล้ว เก็บข้อมูล ABCDEF 
หลังจากนั้นให้ แทรกข้อมูล XYZ ระหว่าง C,D
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        
        if next is None:
            self.next = None
        else:
            self.next = next

class List:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            s_now = self.head
            while s_now.next:
                s_now = s_now.next
            s_now.next = new_node
    
    def node_print(self):
        elements = []
        s_now_node = self.head
        while s_now_node:
            elements.append(s_now_node.data)
            s_now_node = s_now_node.next
        return elements

    def insert_after(self, target_data, data):
        if self.head is None:
            return
        s_now = self.head
        while s_now and s_now.data != target_data:
            s_now = s_now.next
        new_node = Node(data)
        new_node.next = s_now.next
        s_now.next = new_node

ll = List()
for i in "ABCDEF":
    ll.append(i)
    
print("\n\n#Activities 3 \nList:", ll.node_print())

ll.insert_after("C", "X")
ll.insert_after("X", "Y")
ll.insert_after("Y", "Z")

print("Insert LL After", ll.node_print())


"""#LAB : 04"""

print("\n\nLAB : 4")


class tempStack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:   
            self.items = list
        self.size = len(self.items)
        
    def isEmpty(self):
        return self.items == []
    
    
    def left_push(self, item):
        self.items.insert(0, item)
        self.size += 1
    
    def left_pop(self):
        if not self.isEmpty():
            self.size -= 1
            return self.items.pop(0)

    def right_push(self, item):
        self.items.append(item)
        self.size += 1
    
    def right_pop(self):
        if not self.isEmpty():
            self.size -= 1
            return self.items.pop()


ts = tempStack()

print("################ 1 #################")

# Push_left
for i in "ABCD":
    ts.left_push(i)
    print(ts.items)
    
# Pop_left
while not ts.isEmpty():
    print(ts.left_pop()) 

print("################ 2 #################")

#Push_right
for i in "ABCD":
    ts.right_push(i)
    print(ts.items)

#Pop_right
while not ts.isEmpty():
    print(ts.right_pop())
    
print("################ 3 #################")

# Push_left
for i in "ABCD":
    ts.left_push(i)
    print(ts.items)

#Pop_right
while not ts.isEmpty():
    print(ts.right_pop())
    
print("################ 4 #################")

#Push_right
for i in "ABCD":
    ts.right_push(i)
    print(ts.items)

# Pop_left
while not ts.isEmpty():
    print(ts.left_pop()) 
class tempNode :
    def __init__(self, data, next = None):
        self.data = data
        
        if next is None:
            self.next = None
        else:
            self.next = next

class tempList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = tempNode(data)
        if self.head is None:
            self.head = new_node
        else:
            s_now = self.head
            while s_now.next:
                s_now = s_now.next
            s_now.next = new_node
    
    def node_print(self):
        elements = []
        s_now_node = self.head
        while s_now_node:
            elements.append(s_now_node.data)
            s_now_node = s_now_node.next
        return elements
    
    def insert_after(self, target_data, data):
        if self.head is None:
            return
        s_now = self.head
        while s_now and s_now.data != target_data:
            s_now = s_now.next
        new_node = Node(data)
        new_node.next = s_now.next
        s_now.next = new_node
    