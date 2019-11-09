class MinStack:
    
    def __init__(self, cap):
        self.cap = cap
        self.stack = []
        self.minelem = None
    
    def push(self, elem):
        if len(self.stack) >= self.cap:
            print("Capacity exceeded.")
            return
        if not self.stack:
            self.stack.append(elem)
            self.minelem = elem
        else:
            if elem >= self.minelem:
                self.stack.append(elem)
            else:
                self.stack.append(2*elem - self.minelem)
                self.minelem = elem
    
    def pop(self):
        if not self.stack:
            return
        if self.stack[-1] >= self.minelem:
            self.stack.pop()
        else:
            self.minelem = 2 * self.minelem - self.stack[-1]
            self.stack.pop()
    
    def top(self):
        return self.stack[-1]