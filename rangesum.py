class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self.build(data, 2 * node + 1, start, mid)
            self.build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(2 * node + 1, start, mid, left, right) + \
               self.query(2 * node + 2, mid + 1, end, left, right)

    def update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if index <= mid:
                self.update(2 * node + 1, start, mid, index, value)
            else:
                self.update(2 * node + 2, mid + 1, end, index, value)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]


# Example data: student marks
marks = [85, 90, 78, 88, 92, 76, 95, 89]

seg = SegmentTree(marks)

# Range Sum Query: total marks from index 2 to 5
print("Sum from index 2 to 5:", seg.query(0, 0, seg.n - 1, 2, 5))

# Update: change marks of student at index 3 to 91
seg.update(0, 0, seg.n - 1, 3, 91)

# Query again after update
print("After update, sum from index 2 to 5:", seg.query(0, 0, seg.n - 1, 2, 5))