
class Grid():
    
    def __init__(self, rows, columns):
        
        self.rows = rows
        self.columns = columns

        self.grid = []
    
    def make_grid(self):
        
        for row in range(self.rows):
            self.grid.append([])
            for col in range(self.columns):
                self.grid[row].append(0)
        
    def print_cell(self, row, col):
        print(f"Row: {row}, Col: {col}")
    
    def select_cell(self, row, col):
        if self.grid[row][col] == 0:
            self.grid[row][col] = 1
            print(f"Row: {row}, Col: {col} SELECTED")
    
    def deselect_cell(self, row, col):
        if self.grid[row][col] == 1:
            self.grid[row][col] = 0
        

