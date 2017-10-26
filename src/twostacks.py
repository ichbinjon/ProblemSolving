class MyQueue(object):
    def __init__(self):
        self.stackA = []
        self.stackB = []
    
    def pop(self):
        stackA = self.stackA
        stackB = self.stackB

        if not stackB:
            while stackA:
                stackB.append(stackA.pop())
            stackB.pop()
        else:
            stackB.pop()
        
    def put(self, value):
        stackA = self.stackA
        stackB = self.stackB

        stackA.append(value)

    def peek(self):
        stackA = self.stackA
        stackB = self.stackB

        if not stackB:
            while stackA:
                stackB.append(stackA.pop())

        peekv = stackB.pop()
        stackB.append(peekv)
        return peekv
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
