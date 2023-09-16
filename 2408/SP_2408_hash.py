class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.table = {}
        self.id_count = {}
        for index, name in enumerate(names):
            self.table[name] = {}
            self.id_count [name] = 0

    def insertRow(self, name: str, row: List[str]) -> None:
        """
        Adds a row to the table name. It is guaranteed that the table will exist, and the size of the array row is equal to the number of columns in the table.
        """
        self.id_count[name] += 1
        self.table[name][self.id_count[name]] = row
        # print(self.table)
        return None

    def deleteRow(self, name: str, rowId: int) -> None:
        self.table[name].pop(rowId)
        return None

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.table[name][rowId][columnId-1]
