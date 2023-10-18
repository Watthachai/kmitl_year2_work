class Queue:
    def __init__(self):
        self.queue = []

    def addJob(self, ID, jobName):
        # เพิ่มงานเข้าคิว โดยตรวจสอบสิทธิของพนักงาน
        # ID ที่ 100-199 มีสิทธิสูงสุด
        # 200-299 มีสิทธิรองสูงสุด
        # 300-399 ...
        # 800-899 มีสิทธิกอนกลุมต่ำสุด
        # 900-999 มีสิทธิต่ำสุด
        priority = int(ID) // 100
        if priority < 1 or priority > 9:
            print("Invalid priority")
            return
        self.queue.append((ID, jobName, priority))
        print(f"Job submitted for ID {ID}")

    def listJobs(self):
        # แสดงรายการงานที่รอในคิว
        self.queue.sort(key=lambda x: x[2])
        print("ID\tJob Name")
        for job in self.queue:
            print(f"{job[0]}\t{job[1]}")

    def runJob(self):
        # รันงานที่มีสิทธิสูงสุด
        self.queue.sort(key=lambda x: x[2])
        if self.queue:
            ID, jobName, _ = self.queue.pop(0)
            print(f"ID: {ID} Job: {jobName} starts running.")
        else:
            print("No jobs in the queue.")

    def cancelJob(self, ID, jobName):
        # ยกเลิกงานที่รอในคิว
        for job in self.queue:
            if job[0] == ID and job[1] == jobName:
                self.queue.remove(job)
                print(f"ID: {ID} Job: {jobName} has been cancelled.")
                return
        print(f"No matching job found for ID {ID} and job {jobName}.")

    def urgentJob(self, ID, jobName):
        # กำหนดงานที่มีสิทธิต่ำสุดเป็นงานแรกในคิว
        for job in self.queue:
            if job[0] == ID and job[1] == jobName:
                job = self.queue.pop(self.queue.index(job))
                self.queue.insert(0, job)
                print(f"ID: {ID} Job: {jobName} has first priority.")
                return
        print(f"No matching job found for ID {ID} and job {jobName}.")

# สร้างคิว
queue = Queue()

# รับคำสั่งและดำเนินการตามคำสั่ง
while True:
    command = input()
    if command == "A":
        ID, jobName = input().split()
        queue.addJob(ID, jobName)
    elif command == "L":
        queue.listJobs()
    elif command == "R":
        queue.runJob()
    elif command == "C":
        ID, jobName = input().split()
        queue.cancelJob(ID, jobName)
    elif command == "U":
        ID, jobName = input().split()
        queue.urgentJob(ID, jobName)
