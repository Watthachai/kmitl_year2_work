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

print(s.items)

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

print('\nAdded!', q.items, '\nTotal size :',len(q.items))


""" ACTIVITY 3
ให้นักศึกษาเขียนโปรแกรมสร้าง Link List แล้ว เก็บข้อมูล ABCDEF 
หลังจากนั้นให้ แทรกข้อมูล XYZ ระหว่าง C,D
"""

class node:
    def __init__(self, data, next = None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = None

class list:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        
        p = node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p