class SnapshotArray:

    def __init__(self, length: int):
        self.array = [0] * length
        self.snap_num = 0
        self.modify = {}
        self.modifies = []

    def set(self, index: int, val: int) -> None:
        self.array[index] = val
        self.modify[index] = val

    def snap(self) -> int:
        self.snap_num += 1
        self.modifies.append(self.modify)
        self.modify = {}
        return self.snap_num - 1

    def get(self, index: int, snap_id: int) -> int:
        for i in range(snap_id, -1, -1):
            if index in self.modifies[i]:
                return self.modifies[i][index]
        return 0

