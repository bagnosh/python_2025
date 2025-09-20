class Matrix:
    def __init__(self, rows, columns, default = 0):
        self.rows = rows
        self.columns = columns
        self.data = [[default for _ in range(columns)] for _ in range(rows)]
    
    def __getitem__(self, index):
        r, c = index
        if not (0 <= r <self.rows and 0 <= c < self.columns):
            raise IndexError(f"Index [{r}][{c}] is out of range")
        return self.data[r][c]
    
    def __setitem__(self, index, value):
        r, c = index
        if not (0 <= r <self.rows and 0 <= c < self.columns):
            raise IndexError(f"Index [{r}][{c}] is out of range")
        self.data[r][c] = value
    
    def __str__(self):
        return '\n'.join(' '.join(str(item) for item in row) for row in self.rows)