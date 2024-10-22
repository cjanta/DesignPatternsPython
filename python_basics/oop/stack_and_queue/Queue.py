
class Queue_Impl:
    def __init__(self):
        self.data_queue = []

    def enqueue(self, element_to_enqueue):
        self.data_queue.append(element_to_enqueue)

    def dequeue(self):
        if(len(self.data_queue) > 0):
            return self.data_queue.pop(0)
        return None
