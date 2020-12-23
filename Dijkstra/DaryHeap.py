class D_aryHeap:
    def __init__(self, d):
        self.items = []
        self.d = d

    def size(self):
        return len(self.items)

    def parent(self, i):
        return (i - 1)//self.d

    def child(self, index, position):
        return index*self.d + (position + 1)

    def get(self, i):
        return self.items[i]

    def get_min(self):
        if self.size() == 0:
            return None
        return self.items[0]

    def extract_min(self):
        if self.size() == 0:
            return None
        smallest = self.get_min()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.min_heapify(0)
        return smallest

    def min_heapify(self, i):
        smallest = i
        for j in range(self.d):
            c = self.child(i, j)
            if (c < self.size() and self.get(c) < self.get(smallest)):
                smallest = c
        if (smallest != i):
            self.swap(smallest, i)
            self.min_heapify(smallest)

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def insert(self, key):
        index = self.size()
        self.items.append(key)
        while (index != 0):
            p = self.parent(index)
            if self.get(p) > self.get(index):
                self.swap(p, index)
            index = p
