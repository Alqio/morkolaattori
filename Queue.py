class Queue:
    def __init__(self, max_length):
        self.data = []
        self.max_length = max_length
        
    def _enqueue(self, point):
        self.data.append(point)
        return point

    def _dequeue(self):
        return self.data.pop(0)
    
    def add(self, point):
        self._enqueue(point)
        while len(self.data) > self.max_length:
            self._dequeue()
    
    def average(self):
        if len(self.data) < 1:
            return 0
        else:
            return sum(self.data) / len(self.data)

