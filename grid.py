
class Grid():
    
    def __init__(self, rows, columns):
        
        self.rows = rows
        self.columns = columns

        self.grid = []
        
        self.start_count = 0
        self.finish_count = 0
    
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
    
    def deselect_cell(self, row, col):
        if self.grid[row][col] == 1:
            self.grid[row][col] = 0
    
    def clear_grid(self):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                self.grid[i][j] = 0
        self.start_count = 0
        self.finish_count = 0

        print("Grid cleared")
    
    def place_start(self, row, col):

        if self.grid[row][col] == 6:
            self.grid[row][col] = 0
            self.start_count = 0
        elif self.start_count != 1 and self.grid[row][col] == 0:
            self.grid[row][col] = 6
            self.start_count = 1

        
    
    def place_finish(self, row, col):
        
        if self.grid[row][col] == 9:
            self.grid[row][col] = 0
            self.finish_count = 0
        elif self.finish_count != 1 and self.grid[row][col] == 0:
            self.grid[row][col] = 9
            self.finish_count = 1
        
        
        

