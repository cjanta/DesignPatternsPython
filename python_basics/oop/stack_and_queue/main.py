from Stack import Stack_Impl
from Queue import Queue_Impl

data = Stack_Impl()
data.push(1)
data.push(2)
data.push(3)
print(data.data_stack)

poped_element = data.pop()
print("poped:",poped_element )

data = Queue_Impl()
data.enqueue(1)
data.enqueue(2)
data.enqueue(3)
print(data.data_queue)

dequed_element = data.dequeue()
print("dequeued:",dequed_element )