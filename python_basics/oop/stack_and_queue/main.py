from Stack import Stack
from Queue import Queue

######### Stack
data = Stack()
data.push(1)
data.push(2)
data.push(3)
print(data)

poped_element = data.pop()
print("poped:", poped_element)

######### Queue
data = Queue()
data.enqueue(1)
data.enqueue(2)
data.enqueue(3)
print(data)

dequed_element = data.dequeue()
print("dequeued:", dequed_element)