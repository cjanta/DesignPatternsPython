
class Stack(list):

    def push(self, item):
        super().append(item)

    def pop(self):
        return super().pop()