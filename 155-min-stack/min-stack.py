class MinStack(object):

    def __init__(self):
        self.s = []
        self.stack = []

    def push(self, value):
        self.s.append(value)

        if not self.stack or value <= self.stack[-1]:
            self.stack.append(value)

    def pop(self):
        if self.s.pop() == self.stack[-1]:
            self.stack.pop()

    def top(self):
        if not self.s:
            return -1
        else:
            return self.s[-1]

    def getMin(self):
        if not self.stack:
            return -1
        else:
            return self.stack[-1]