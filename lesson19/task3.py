class Table:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[None] * columns for _ in range(rows)]

    def __getitem__(self, index):
        row, column = index
        return self.data[row][column]

    def __setitem__(self, index, value):
        row, column = index
        self.data[row][column] = value

    def __iter__(self):
        self.row_index = 0
        self.column_index = 0
        return self

    def __next__(self):
        if self.row_index >= self.rows:
            raise StopIteration

        value = self.data[self.row_index][self.column_index]
        self.column_index += 1

        if self.column_index >= self.columns:
            self.row_index += 1
            self.column_index = 0

        return value
table = Table(3, 4)
table[0, 0] = 1
table[0, 1] = 2
table[1, 2] = 3

for value in table:
    print(value)