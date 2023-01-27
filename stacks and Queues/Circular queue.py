from sys import maxsize

class Queue:
    def __init__(self,cap):
        self.queue = [None]*cap
        self.front = -1
        self.rear = -1
        self.capacity = cap

    def is_empty(self):
        if self.front == -1:
            print('Queue is empty')
        return self.front == -1
    
    def is_full(self):
        return (self.front == self.rear + 1) or (self.front==0 and self.rear==self.capacity-1)
    
    def enqueue(self,item):
        if self.is_full():
            print('Queue is full')
            return
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
            print('Item added: ',item)
    
    def dequeue(self):
        if self.is_empty():
            return
        else:
            item = self.queue[self.front]

            if self.front == self.rear:
                self.rear, self.front = -1, -1
            else:
                self.front = (self.front + 1) % self.capacity
            
            print('Item dequeued: ',item)

    def display(self):
            i = 0
            if self.is_empty():
                print("Empty Queue")
            else:
                print("\nQueue: ")
                i = self.front
                while i != self.rear:
                    print(self.queue[i], end=" ")
                    i = (i + 1) % self.capacity

                print(self.queue[i])


q = Queue(6)
q.dequeue()  # Underflow condition

q.enqueue(12)
q.enqueue(14)
q.enqueue(16)
q.enqueue(18)
q.enqueue(20)

q.display()
q.dequeue()
q.dequeue()

q.display()

q.enqueue(22)
q.enqueue(24)
q.enqueue(26)
q.enqueue(28)  # Overflow condition
q.display()