class Queue:
    def __init__(self,cap):
        self.queue = [None] * cap
        self.front = None
        self.rear = None
        self.capacity = cap
    
    def is_full(self):
        if self.rear == self.capacity - 1:
            print('Overflowed')
        return self.rear == self.capacity - 1

    def is_empty(self):
        if self.front is None:
            print('Underflowed')
        return self.front is None
    
    def enqueue(self,item):
        if self.is_full():
            return
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1
        self.queue[self.rear] = item
        print(item,' Enqueued')
    
    def dequeue(self):
        if self.is_empty():
            return

        temp = self.queue[self.front]
        self.front += 1

        if self.front > self.rear:
            self.front, self.rear = None, None
        
        print(temp,' Dequeued')

    def display(self):
        if self.rear is None:
            print("Queue was Empty!!!")
        else:
            i = self.front
            print("Queue : ", end="")

            while i <= self.rear:
                print(self.queue[i], end=" ")
                i += 1


# Driver Code
q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print()
q.dequeue()
q.dequeue()
print()

q.display()