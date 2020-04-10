'''
[0,0,0,0]

[5,0,0,0] => snap {}
[6,0,0,0]

'''


class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[-1, 0]] for _ in range(length)]
        self.snaps = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snaps, val])

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.arr[index]
        idx = len(arr) - 1

        while idx >= 0 and arr[idx][0] != snap_id:
            idx -= 1

        if idx < 0:
            return 0

        return arr[idx][1]


arr = SnapshotArray(2)

arr.snap()
arr.get(1, 0)
arr.get(0, 0)
arr.set(1, 8)
print(
    arr.get(1, 0)
)