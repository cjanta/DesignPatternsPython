
class Stack_Impl:

    def __init__(self):
        self.data_stack = []

    def push(self, element_to_push):
        self.data_stack.append(element_to_push)

    def pop(self):
        return self.data_stack.pop(len(self.data_stack)-1)