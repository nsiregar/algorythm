class CircularBuffer(object):
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full\n")

        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear - 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty\n")

        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):
        if self.front == -1:
            print("Queue is empty\n")

        elif self.rear >= self.front:
            print("Element in circular buffer are:", end=" ")
            for item in range(self.front, self.rear + 1):
                print(self.queue[item], end=" ")
            print()

        else:
            print("Element in circular buffer are:", end=" ")
            for idx in range(self.front, self.size):
                print(self.queue[idx], end=" ")
            for idx in range(0, self.rear + 1):
                print(self.queue[idx], end=" ")
            print()

        if (self.rear + 1) % self.size == self.front:
            print("Queue is full\n")
