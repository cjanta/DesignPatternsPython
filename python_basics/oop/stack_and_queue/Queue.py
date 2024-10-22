
class Queue(list):

    def enqueue(self, item):
        super().append(item)

    def dequeue(self):
        if(len(self) > 0):
            return super().pop(0)
        return None
