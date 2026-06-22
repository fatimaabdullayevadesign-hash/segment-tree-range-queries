class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node, start, mid)
            self.build(arr, 2 * node + 1, mid + 1, end)
            self.tree[node] = (
                self.tree[2 * node] + self.tree[2 * node + 1]
            )

    def query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2

        p1 = self.query(
            2 * node, start, mid, left, right
        )
        p2 = self.query(
            2 * node + 1, mid + 1, end, left, right
        )

        return p1 + p2

    def update(self, node, start, end, idx, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2

            if idx <= mid:
                self.update(
                    2 * node, start, mid, idx, value
                )
            else:
                self.update(
                    2 * node + 1,
                    mid + 1,
                    end,
                    idx,
                    value,
                )

            self.tree[node] = (
                self.tree[2 * node]
                + self.tree[2 * node + 1]
            )


arr = [1, 3, 5, 7, 9, 11]

segment_tree = SegmentTree(arr)

print(
    "Range Sum (1,4):",
    segment_tree.query(
        1, 0, len(arr) - 1, 1, 4
    ),
)

segment_tree.update(
    1, 0, len(arr) - 1, 2, 10
)

print(
    "After Update:",
    segment_tree.query(
        1, 0, len(arr) - 1, 1, 4
    ),
)