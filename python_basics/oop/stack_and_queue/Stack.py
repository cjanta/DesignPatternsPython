
class Stack(list):

    def push(self, item):
        super().append(item)

    def pop(self):
        if(len(self) > 0):
            return super().pop()
        return None