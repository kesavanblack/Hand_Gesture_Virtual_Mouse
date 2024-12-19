from collections import deque

class Smoother:
    def __init__(self, buffer_size=5):
        self.buffer = deque(maxlen=buffer_size)

    def smooth(self, x, y):
        self.buffer.append((x, y))
        avg_x = sum([p[0] for p in self.buffer]) / len(self.buffer)
        avg_y = sum([p[1] for p in self.buffer]) / len(self.buffer)
        return int(avg_x), int(avg_y)
