#
# เขียนฟังก์ชั่น Shuffle string 2 ชุดให้กลายเป็นชุดเดียว เช่น
# input = "abc","def"
# output = "adbecf"
# โดยใช้ queue 2 ชุด ช่วยในการสลับตัวอักษร
#

from queue import Queue


def shuffle(string1, string2):
    q1 = Queue(maxsize=50)
    for s in string1:
        q1.put(s)

    q2 = Queue(maxsize=50)
    for s in string2:
        q2.put(s)

    ret = ""

    if len(string1) >= len(string2):
        for i in range(len(string1)):
            if not q1.empty() and not q2.empty():
                ret += q1.get() + q2.get()
            else:
                ret += q1.get()
    else:
        for i in range(len(string2)):
            if not q2.empty() and not q1.empty():
                ret += q1.get() + q2.get()
            else:
                ret += q2.get()

    return ret


st1 = "abcdefghhhhhhhhhhhhh"
st2 = "ABCDEFGasssssssssssssssdasdw"
print(shuffle(st1, st2))  # aAbBcCdDeEfFgG




############ข้อ 1 #################
class Queue:
    def __init__(self):
        self.items1 = []
        self.items2 =[]

    def is_empty(self):
        return len(self.items1) == 0 and len(self.items2) == 0

    def enqueue(self, item1,item2):
        for i in item1:
            self.items1.append(i)
        for n in item2:
            self.items2.append(n)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def shuffle(self):
        stack = ""
        if not self.is_empty():
            for i in range(len(self.items1)):
                stack += self.items1[i] + self.items2[i]
            return stack
        else:
            return None
