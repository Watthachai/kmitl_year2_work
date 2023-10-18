"""
Program 1:
ให้นักศึกษาเขียนโปรแกรม สร้าง Class Queue และรับ input เป็น string แล้วทำการสลับตำแหน่งตัวอักษร
แบบกรีดไพ่ โดยใช้ Queue 2 Queue
ตัวอย่าง
Input: ABCDEFGH
Output : AEBFCGDH
"""

#Program 1
import queue

class QueueString:
    def __init__(self, string):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        for char in string:
            self.q1.put(char)

    def shuffle(self):
        result = ''
        while not self.q1.empty():
            result += self.q1.get()  # Take one character from the front of q1
            if not self.q1.empty():  # If there are still characters left in q1
                self.q2.put(self.q1.get())  # Take the next character from q1 and put it in q2
        while not self.q2.empty():
            result += self.q2.get()  # Take all remaining characters from q2
        return result

# Test the class
q = QueueString('ABCDEFGH')
print(q.shuffle())  # Output: AEBFCGDH



"""
Program 2:
ให้นักศึกษาเขียนโปรแกรม สร้าง Class Stack และรับ input เป็น expression ทางคณิตศาสตร์ แล้วทำการตรวจสอบ expression ว่ามีการเติมวงเล็บถูกต้องหรือไม่โดยใช้ Stack
ตัวอย่าง
Input : (1+(2-3))
Output : True
ตัวอย่าง
Input : 1+(2*3)-4)
Output : False
"""
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def is_balanced(expression):
    s = Stack()
    for char in expression:
        if char == "(":
            s.push(char)
        elif char == ")":
            if s.is_empty():
                return False
            s.pop()
    return s.is_empty()


# Test the function
print(is_balanced("(1+(2-3))"))  # Should print: True
print(is_balanced("1+(2*3)-4)"))  # Should print: False



"""
Program 3:
เขียนโปรแกรมรับ input เป็น string และ keyword แล้วหาตำแหน่งของ Keyword ใน string ถ้าไม่พบให้ แสดงผล -1
Input string : hello world
Input Keyword: world
Output : 6
Input string : hello world
Input Keyword: word
Output: -1
"""